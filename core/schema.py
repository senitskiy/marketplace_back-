from cmath import log
import graphene
from core.graphql.query import Query
from core.graphql.mutation import Mutation

schema = graphene.Schema(query=Query, mutation=Mutation)