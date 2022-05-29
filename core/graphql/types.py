from graphene_django import DjangoObjectType
from core.models import MNFTCollection, MNFT, User, Blockchain


class UserGraphQLType(DjangoObjectType):
    class Meta:
        model = User


class MNFTCollectionGraphQLType(DjangoObjectType):
    class Meta:
        model = MNFTCollection


class BlockchainGraphQLType(DjangoObjectType):
    class Meta:
        model = Blockchain


class MNFTGraphQLType(DjangoObjectType):
    class Meta:
        model = MNFT