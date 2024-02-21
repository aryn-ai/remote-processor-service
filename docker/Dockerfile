FROM gradle:jdk17 AS assemble_plugin

WORKDIR /build
COPY ./opensearch-remote-processor/ ./opensearch-remote-processor/
WORKDIR /build/opensearch-remote-processor
RUN ./gradlew assemble

FROM opensearchproject/opensearch:2.12.0 AS opensearch
COPY --from=assemble_plugin /build/opensearch-remote-processor/build/distributions/remote-processor-2.12.0-SNAPSHOT.zip /tmp/
RUN /usr/share/opensearch/bin/opensearch-plugin install --batch file:///tmp/remote-processor-2.12.0-SNAPSHOT.zip

COPY docker/opensearch.yml /usr/share/opensearch/config/

ENV DISABLE_SECURITY_PLUGIN=true
ENV DISABLE_INSTALL_DEMO_CONFIG=true
ENV discovery.type=single-node