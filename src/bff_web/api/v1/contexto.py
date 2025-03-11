from functools import cached_property
from typing import Union

import strawberry
from fastapi import FastAPI
from strawberry.fastapi import BaseContext, GraphQLRouter

from bff_web.api.v1.esquemas import Usuario


class Context(BaseContext):
    @cached_property
    def user(self) -> Union[Usuario, None]:
        if not self.request:
            return None

        token = self.request.headers.get("Authorization", None)

        if token == "Bearer usuario_valido":
            return Usuario(name="Usuario Valido")
        else:
            return None
