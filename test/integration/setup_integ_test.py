import os
import subprocess
import sys

import docker
import shutil
from pathlib import Path


def test_setup_integ_tests():
    build_plugin_artifact()
    opensearch_image = build_plugin_container()
    server_image = build_service_container()
    network, opensearch_container, rps_container = run_compose(server_image, opensearch_image)
    network_calls()
    opensearch_container.stop()
    rps_container.stop()
    network.remove()


def build_plugin_artifact():
    create_commondir()
    path = (Path(".") / "opensearch-remote-processor")
    p = subprocess.Popen(args=["./gradlew", "assemble"], cwd=path)
    p.wait()


def create_commondir():
    """
    The opensearch plugin gradle plugin expects to be able to find this file.
    Git submodule shenanigans mess it up, so I have to create it manually
    """
    commondir = Path(".git/modules/opensearch-remote-processor/commondir")
    with open(commondir, "w") as f:
        f.write(".")


def build_plugin_container():
    shutil.copyfile("opensearch-remote-processor/build/distributions/remote-processor-2.12.0-SNAPSHOT.zip", "docker/remote-processor-2.12.0-SNAPSHOT.zip")
    image, logs = docker.DockerClient().images.build(path="docker", tag="test-rps-os", dockerfile="Dockerfile.os")
    return image


def build_service_container():
    image, logs = docker.DockerClient().images.build(path=".", tag="test-rps")
    return image


def run_compose(server_image, opensearch_image):
    client = docker.DockerClient()
    nets = client.networks.list(names=["test-net"])
    if len(nets) == 0:
        network = client.networks.create("test-net")
    else:
        network = nets[0]
    opensearch_container = client.containers.run(
        image=opensearch_image,
        name="test-opensearch",
        network=network.id,
        detach=True,
        ports={"9200/tcp": 9200, "9600/tcp": 9600, "9300/tcp": 9300},
        environment={"discovery.type": "single-node"},
        remove=True
    )
    rps_container = client.containers.run(
        image=server_image,
        name="test-rps",
        network=network.id,
        detach=True,
        ports={"2796/tcp": 2796},
        remove=True
    )
    return network, opensearch_container, rps_container


def network_calls():
    pass

