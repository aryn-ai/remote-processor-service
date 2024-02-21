# Remote Processor Service
Service and library for remote processors

## Instructions 
Setting this up takes a couple steps. First, get the protocols submodule with
```
git submodule update --init --remote
```

Also install the poetry packages and stuff
```
poetry install --no-root
```

Next, generate the grpc/protobuf code. This will create a subdirectory called `proto_remote_processor` that contains the generated code.
Once the grpc code is generated you can install the package itself.
```
make build_proto
poetry install
```

Now, build an opensearch image with the [remote-processor-plugin](https://github.com/aryn-ai/opensearch-remote-processor) installed.
```
docker build -t rps-os -f docker/Dockerfile .
```

Also build a docker image for the remote processor service itself
```
docker build -t rps .
```

Finally, docker compose up
```
docker compose -f docker/compose.yml up
```
Alternately, one can start the OpenSearch container and run RPS locally.
Be sure to change `rps` to `localhost` in the endpoint below.
```
docker run -d --rm --network=host -e discovery.type=single-node rps-os
poetry run server configs/cfg1.yml
```

And you should have an opensearch with the remote processor plugin installed and a remote processor service (running the config at `configs/cfg1.yml` - just the debug processor atm)

Now, to create a remote processor
```
curl -X PUT http://localhost:9200/_search/pipeline/remote_pipeline --json '
{
    "response_processors": [
        {
            "remote_processor": {
                "endpoint": "rps:2796/RemoteProcessorService/ProcessResponse",
                "processor_name": "debug"
            }
        }
    ]
}'
```

Test the processor server in pure python with:
```
from gen.response_processor_service_pb2_grpc import RemoteProcessorServiceStub
import grpc
from gen.response_processor_service_pb2 import ProcessResponseRequest

chan = grpc.insecure_channel('localhost:2796')
stub = RemoteProcessorServiceStub(chan)
req = ProcessResponseRequest()
req.processor_name = "debug"
res = stub.ProcessResponse(req)
print(res)
```
```
search_response {
}
```

Or, test the processor via OpenSearch:
```
curl 'http://localhost:9200/demoindex0/_search?search_pipeline=remote_pipeline&pretty' --json '
{
  "query": {
    "match": {
      "text_representation": "armadillo"
    }
  }
}'
```
