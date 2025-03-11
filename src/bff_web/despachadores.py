import pulsar
from pulsar.schema import AvroSchema

from . import utils

class Despachador:
    def __init__(self):
        ...

    async def publicar_mensaje(self, mensaje, topico, schema):
        host = "host.docker.internal"
        print(f"Host: {host}")

        pulsar_url = f'pulsar://{host}:6650'

        print(f"pulsar_url: {pulsar_url}")

        cliente = pulsar.Client(pulsar_url)
        print("cliente creado")
        print(f"Topico: {topico}")
        print(f"Schema: {schema}")
        publicador = cliente.create_producer(topico, schema=AvroSchema(schema))
        print("publicador creado")
        publicador.send(mensaje)
        print("mensaje publicado")
        cliente.close()
