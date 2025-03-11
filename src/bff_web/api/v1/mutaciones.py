from typing import Any
import uuid

import strawberry

from strawberry.types import Info

from bff_web import utils
from bff_web.api.v1.contexto import Context
from bff_web.api.v1.eventos import EventoDatosImportados, EventoDatosImportadosPayload
from bff_web.config import Config
from bff_web.despachadores import Despachador

from .esquemas import IngestaRespuesta

config = Config()


@strawberry.type
class Mutation:

    @strawberry.mutation
    async def simular_ingesta(
        self, ruta_imagen: str, ruta_metadatos: str, info: Info[Context, Any]
    ) -> IngestaRespuesta:
        if info.context.user is None:
            return IngestaRespuesta(
                mensaje="No tienes permisos para realizar esta acción",
                codigo=401,
            )

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
