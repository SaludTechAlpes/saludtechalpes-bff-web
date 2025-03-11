import uuid

import strawberry

from bff_web import utils
from bff_web.api.v1.eventos import EventoDatosImportados, EventoDatosImportadosPayload
from bff_web.config import Config
from bff_web.despachadores import Despachador

from .esquemas import IngestaRespuesta

config = Config()


@strawberry.type
class Mutation:

    @strawberry.mutation
    async def simular_ingesta(
        self, ruta_imagen: str, ruta_metadatos: str
    ) -> IngestaRespuesta:

        print(f"Ruta Imagen: {ruta_imagen}, Ruta Metadatos: {ruta_metadatos}")

        payload = EventoDatosImportadosPayload(
            ruta_imagen=ruta_imagen,
            ruta_metadatos=ruta_metadatos,
        )
        payload = EventoDatosImportadosPayload(
            ruta_imagen_importada=ruta_imagen,
            ruta_metadatos_importados=ruta_metadatos,
            evento_a_fallar=None,
        )

        evento = EventoDatosImportados(
            id=str(uuid.uuid4()),
            time=utils.time_millis(),
            specversion="v1",
            type="DatosImportadosEvento",
            ingestion=utils.time_millis(),
            datacontenttype="AVRO",
            service_name="BFF Web",
            data=payload,
        )

        despachador = Despachador()

        await despachador.publicar_mensaje(
            evento, "datos-importados", EventoDatosImportados
        )

        return IngestaRespuesta(mensaje="Procesando Mensaje", codigo=203)
