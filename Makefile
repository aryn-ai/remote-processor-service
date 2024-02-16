help:
	@echo "No help for you"

install_poetry:
	apt update
	DEBIAN_FRONTEND=noninteractive apt -y install --no-install-recommends python3-poetry gcc python3-dev
	apt clean
	-rm -rf /var/lib/apt/lists/*
	poetry config virtualenvs.path /rps/poetry_venv

clean:
	-rm -rd proto_remote_processor

build_proto:
	poetry run python -m grpc_tools.protoc -I protocols/ --python_out=. --pyi_out=. --grpc_python_out=. protocols/proto-remote-processor/*.proto

common_build:
	poetry install --no-root --without test

full_build:
	poetry install --without test
