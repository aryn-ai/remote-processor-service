#!/bin/bash

die() {
    echo "ERROR:" "$@" 1>&2
    if [[ ${NOEXIT} -gt 0 ]]; then
        echo "Not dying due to NOEXIT.  Feel free to poke around container."
        sleep inf
    fi
    exit 1
}

create_certificates() {
    local HOST="${SSL_HOSTNAME:-localhost}"
    local DAYS=10000
    local LOG="config/openssl.err"
    truncate -s 0 "${LOG}"

    # 1. Make fake certificate authority (CA) certificate.  OpenSearch
    # requires a root certificate to be specified.
    if [[ (! -f config/cakey.pem) || (! -f config/cacert.pem) ]]; then
        openssl req -batch -x509 -newkey rsa:4096 -days "${DAYS}" \
        -subj "/C=US/ST=California/O=Aryn.ai/CN=Fake CA" \
        -extensions v3_ca -noenc -keyout config/cakey.pem -out config/cacert.pem \
        2>> "${LOG}" || die "Failed to create CA certificate"
        echo "Created CA certificate"
    fi

    # 2a. Create certificate signing request (CSR) for the node certificate.
    if [[ (! -f config/rps-key.pem) || (! -f config/rps-cert.pem) ]]; then
        openssl req -batch -newkey rsa:4096 \
        -subj "/C=US/ST=California/O=Aryn.ai/CN=${HOST}" \
        -extensions v3_req -addext "basicConstraints=critical,CA:FALSE" \
        -addext "subjectAltName=DNS:${HOST}" \
        -noenc -keyout config/rps-key.pem -out config/rps-req.pem \
        2>> "${LOG}" || die "Failed to create RPS CSR"

        # 2b. Use the fake CA to sign the node CSR, yielding a certificate.
        openssl x509 -req -CA config/cacert.pem -CAkey config/cakey.pem \
        -copy_extensions copy -days "${DAYS}" \
        -in config/rps-req.pem -out config/rps-cert.pem \
        2>> "${LOG}" || die "Failed to create RPS certificate"
        echo "Created RPS certificate"
    fi

    rm -f config/rps-req.pem
    for X in cakey.pem cacert.pem rps-key.pem rps-cert.pem; do
        chmod 600 "config/${X}"
    done
}

main() {
    export GRPC_PYTHON_BUILD_SYSTEM_OPENSSL=1
    create_certificates
    poetry run server config/pipelines.yml --keyfile config/rps-key.pem --certfile config/rps-cert.pem
}

main
