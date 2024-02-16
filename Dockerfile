
ARG POETRY_NO_INTERACTION=1
ARG POETRY_VIRTUALENVS_IN_PROJECT=1
ARG POETRY_VIRTUALENVS_CREATE=1 \
ARG POETRY_CACHE_DIR=/tmp/poetry_cache
ARG RPS_PORT=2796

##########
# Common: resolve dependencies
FROM python:3.11 AS rps_common

WORKDIR /rps
COPY ./poetry.lock ./pyproject.toml ./Makefile /rps/
RUN make install_poetry
RUN make common_build

##########
# Build: build package, compile protobufs
FROM rps_common AS rps_build

# Build the proto files into python
COPY ./protocols /rps/protocols
RUN make build_proto

##########
# Run: run the server
FROM rps_common AS rps_server

COPY --from=rps_build /rps/proto_remote_processor /rps/proto_remote_processor
COPY ./lib /rps/lib/
COPY ./service /rps/service
COPY ./README.md /rps/README.md
RUN make full_build

EXPOSE $RPS_PORT
COPY ./configs /rps/configs

CMD ["poetry", "run", "server", "configs/cfg1.yml"]
