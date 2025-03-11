from strawberry.fastapi import GraphQLRouter
from .consultas import Query
from .mutaciones import Mutation
from .contexto import Context

import strawberry


async def get_context() -> Context:
    return Context()

schema = strawberry.Schema(query=Query, mutation=Mutation)
router = GraphQLRouter(schema, context_getter=get_context)
