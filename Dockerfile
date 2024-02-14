FROM mwalbeck/python-poetry:1.7-3.11

WORKDIR /rps
# Selectively bring in the minimal things to run the service
COPY ./protocols /rps/protocols/
COPY ./genrpc /rps/genrpc
COPY ./service /rps/service/
COPY ./lib /rps/lib/
COPY ./pyproject.toml /rps/pyproject.toml
COPY ./poetry.lock /rps/poetry.lock
COPY ./configs /rps/configs/

RUN poetry install --no-root --without test
RUN ./genrpc
RUN poetry install --without test
EXPOSE 2796
CMD ["poetry", "run", "server", "configs/cfg1.yml"]
