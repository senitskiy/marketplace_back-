import graphene
from django.db.models import QuerySet

# user modules
from graphql.types import UserGraphQLType, MNFTCollectionGraphQLType, MNFTGraphQLType, BlockchainGraphQLType
from core.models import User,  MNFTCollection, MNFT, Blockchain


class Query(graphene.ObjectType):
    getUsers = graphene.List(UserGraphQLType)
    getMNFTCollections = graphene.List(MNFTCollectionGraphQLType)
    getMNFTs = graphene.List(MNFTGraphQLType)
    getBlockchains = graphene.List(BlockchainGraphQLType)
    getUser = graphene.Field(UserGraphQLType, address=graphene.String())
    getMNFTCollection = graphene.Field(MNFTCollectionGraphQLType, address=graphene.String())
    getMNFT = graphene.Field(MNFTGraphQLType, address=graphene.String())
    getBlockchain = graphene.Field(BlockchainGraphQLType, name=graphene.String(), idChain=graphene.Int())

    def _resolve_objects(self, cls):
        return cls.objects.all()

    def _resolve_object_by_address(self, cls, address) -> MNFT | MNFTCollection | User | None:
        if address:
            try:
                return cls.objects.get(pk=address)
            except Exception as err:
                print(f"ERROR: {err}")
                return None
        else:
            return None

    
    def _resolve_object_by_name_id(self, cls, name, chainId) -> QuerySet | None:
        if name and chainId:
            try:
                return cls.objects.filter(name=name, chainId=chainId)
            except Exception as err:
                print(f"ERROR: {err}")
                return None
        else:
            return None


    def resolve_getUsers(self, info) -> QuerySet:
        print(info)
        return self._resolve_objects(User)

    def resolve_getMNFTCollections(self, info) -> QuerySet:
        return self._resolve_objects(MNFTCollection)

    def resolve_getMNFTs(self, info) -> QuerySet:
        return self._resolve_objects(MNFT)

    def resolve_getBlockchains(self, info) -> QuerySet:
        return self._resolve_objects(Blockchain)

    def resolve_getUser(self, info, address):
        return self._resolve_object_by_address(User, address)

    def resolve_getMNFTCollection(self, info, address):
        return self._resolve_object_by_address(MNFTCollection, address)

    def resolve_getMNFT(self, info, address):
        return self._resolve_object_by_address(MNFT, address)

    def resolve_getBlockchain(self, info, name, chainId):
        return self._resolve_object_by_name_id(Blockchain, name, chainId)
