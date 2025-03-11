from pulsar.schema import *
import time as time_module
import uuid

class Mensaje(Record):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=int(time_module.time() * 1000))
    specversion = String()
    type = String()
    datacontenttype = String()
    service_name = String()

class EventoIntegracion(Mensaje):
    ...

class EventoDatosImportadosPayload(Record):
    id_imagen_importada = String(default=str(uuid.uuid4()))
    ruta_imagen_importada=String()
    ruta_metadatos_importados=String()
    evento_a_fallar=String()

class EventoDatosImportados(EventoIntegracion):
    data = EventoDatosImportadosPayload()

