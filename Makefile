

help:
	@echo "No help for you"

clean:
	-rm -rd proto_remote_processor

build_proto: clean
	poetry run python -m grpc_tools.protoc -I protocols/ --python_out=. --pyi_out=. --grpc_python_out=. protocols/proto-remote-processor/*.proto
