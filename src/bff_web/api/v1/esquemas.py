import typing
import strawberry
import requests
import os

from datetime import datetime

from bff_web.config import Config


AEROALPES_HOST = os.getenv("AEROALPES_ADDRESS", default="localhost")
FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

config = Config()

def obtener_reservas(root) -> typing.List["Ingesta"]:
    reservas_json = requests.get(f'http://{config.MEDICAL_HISTORY_MS_URL}:5000/vuelos/reserva').json()
    reservas = []

    for reserva in reservas_json:
        reservas.append(
            Ingesta(
                fecha_creacion=datetime.strptime(reserva.get('fecha_creacion'), FORMATO_FECHA), 
                fecha_actualizacion=datetime.strptime(reserva.get('fecha_actualizacion'), FORMATO_FECHA), 
                id=reserva.get('id'), 
                id_usuario=reserva.get('id_usuario', '')
            )
        )

    return reservas

@strawberry.type
class Itinerario:
    # TODO Completar objeto strawberry para incluir los itinerarios
    ...

@strawberry.type
class Ingesta:
    id: str
    id_usuario: str
    fecha_creacion: datetime
    fecha_actualizacion: datetime
    #itinerarios: typing.List[Itinerario]

@strawberry.type
class IngestaRespuesta:
    mensaje: str
    codigo: int

@strawberry.type
class Usuario:
    name: str
