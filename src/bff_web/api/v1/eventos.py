from pulsar.schema import *
import time as time_module
import uuid

class EventoIngestaPayload(Record):
    ruta_imagen = String()
    ruta_metadatos = String()

class EventoIngesta(Record):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=int(time_module.time() * 1000))
    specversion = String()
    type = String()
    datacontenttype = String()
    service_name = String()
    data = EventoIngestaPayload()

