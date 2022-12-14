import graphene
from django.db.models import QuerySet

# user modules
from core.graphql.types import UserGraphQLType, MNFTCollectionGraphQLType, MNFTGraphQLType, BlockchainGraphQLType
from core.models import User,  MNFTCollection, MNFT, Blockchain

def _resolve_objects(cls):
    return cls.objects.all()

def _resolve_object_by_address(cls, address) -> MNFT | MNFTCollection | User | None:
    if address:
        try:
            return cls.objects.get(pk=address)
        except Exception as err:
            print(f"ERROR: {err}")
            return None
    else:
        return None


def _resolve_object_by_name_id(cls, name, chainId) -> QuerySet | None:
    if name and chainId:
        try:
            return cls.objects.filter(name=name, chainId=chainId)
        except Exception as err:
            print(f"ERROR: {err}")
            return None
    else:
        return None


class Query(graphene.ObjectType):
    getUsers = graphene.List(UserGraphQLType, description='Получить список пользователей')
    getMNFTCollections = graphene.List(MNFTCollectionGraphQLType, description='Получить список коллекций')
    getMNFTs = graphene.List(MNFTGraphQLType, description='Получить список MNFT')
    getBlockchains = graphene.List(BlockchainGraphQLType, description='Получить список блокчейнов')
    getUser = graphene.Field(UserGraphQLType, address=graphene.String(), description='Получить данные пользователя')
    getMNFTCollection = graphene.Field(MNFTCollectionGraphQLType, address=graphene.String(), description='Получить данные коллекции')
    getMNFT = graphene.Field(MNFTGraphQLType, address=graphene.String(), description='Получить данные о MNFT')
    getBlockchain = graphene.Field(BlockchainGraphQLType, name=graphene.String(), idChain=graphene.Int(), description='Получить данные о блокчейне')

    def resolve_getUsers(root, info) -> QuerySet:
        return _resolve_objects(User)

    def resolve_getMNFTCollections(root, info) -> QuerySet:
        return _resolve_objects(MNFTCollection)

    def resolve_getMNFTs(root, info) -> QuerySet:
        return _resolve_objects(MNFT)

    def resolve_getBlockchains(root, info) -> QuerySet:
        return _resolve_objects(Blockchain)

    def resolve_getUser(root, info, address):
        return _resolve_object_by_address(User, address)

    def resolve_getMNFTCollection(root, info, address):
        return _resolve_object_by_address(MNFTCollection, address)

    def resolve_getMNFT(root, info, address):
        return _resolve_object_by_address(MNFT, address)

    def resolve_getBlockchain(root, info, name, chainId):
        return _resolve_object_by_name_id(Blockchain, name, chainId)

    class Meta:
        description = "Запросы к MNFT, MNFTCollection, User, Blockchain"
