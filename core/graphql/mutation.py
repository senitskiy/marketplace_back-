import graphene
from core.graphql.inputs import MNFTCollectionInput, MNFTInput, UserInput, BlockchainInput
from core.graphql.types import MNFTCollectionGraphQLType, MNFTGraphQLType, UserGraphQLType, BlockchainGraphQLType
from core.models import MNFTCollection, MNFT, User, Blockchain

class createMNFT(graphene.Mutation):
    class Arguments:
        # address = graphene.String(required=True)
        input = MNFTInput()
    ok = graphene.Boolean()
    MNFT = graphene.Field(MNFTGraphQLType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        print(input.sponsor)
        uCreator = User.objects.get(pk=input.creator)
        uOwner = User.objects.get(pk=input.owner)
        uSponsor = User.objects.get(
            pk=input.sponsor) if input.sponsor is not None else None
        print(uCreator, uOwner, uSponsor)

        mnft_instanse = MNFT(address=input.address,
                             blockchain=input.blockchain,
                             symbol=input.symbol,
                             standart=input.standart,
                             lastUpdate=input.lastUpdate,
                             name=input.name,
                             description=input.description,
                             image=input.image,
                             cost=input.cost,
                             costAd=input.costAd,
                             creator=uCreator,
                             owner=uOwner,
                             sponsor=uSponsor
                             )
        mnft_instanse.save()
        s = requests.Session()
        answ = s.request(
            "DELETE", f"https://api-staging.rarible.org/v0.1/items/ETHERIUM:{input.address}:0/resetMeta")
        print("RESET RARRIBLE: ", answ)
        answ = s.request(
            "GET", f"https://api-staging.rarible.org/v0.1/items/ETHERIUM:{input.address}:0")
        print("GETELEMENTID RARRIBLE: ", answ)
        return createMNFT(ok=ok, MNFT=mnft_instanse)


class updateMNFT(graphene.Mutation):
    class Arguments:
        address = graphene.String(required=True)
        input = MNFTInput()
    ok = graphene.Boolean()
    MNFT = graphene.Field(MNFTGraphQLType)

    @staticmethod
    def mutate(root, info, address, input=None):
        ok = False
        uCreator = User.objects.get(pk=input.creator) if input.creator is not None else None
        uOwner = User.objects.get(pk=input.owner) if input.owner is not None else None
        uSponsor = User.objects.get(pk=input.sponsor) if input.sponsor is not None else None
        mnft_instance = MNFT.objects.get(pk=address)
        if mnft_instance:
            ok = True
            mnft_instance.address = input.address if input.address is not None else mnft_instance.address 
            mnft_instance.blockchain = input.blockchain if input.blockchain is not None else mnft_instance.blockchain
            mnft_instance.symbol = input.symbol if input.symbol is not None else mnft_instance.symbol
            mnft_instance.standart = input.standart if input.standart is not None else mnft_instance.standart
            mnft_instance.lastUpdate = input.lastUpdate if input.lastUpdate is not None else mnft_instance.lastUpdate
            mnft_instance.name = input.name if input.name is not None else mnft_instance.name
            mnft_instance.description = input.description if input.description is not None else mnft_instance.description
            mnft_instance.image = input.image if input.image is not None else mnft_instance.image
            mnft_instance.cost = input.cost if input.cost is not None else mnft_instance.cost
            mnft_instance.costAd = input.costAd if input.costAd is not None else mnft_instance.costAd
            mnft_instance.creator = uCreator if uCreator is not None else mnft_instance.creator
            mnft_instance.owner = uOwner if uOwner is not None else mnft_instance.owner
            mnft_instance.sponsor = uSponsor if uSponsor is not None else mnft_instance.sponsor
            mnft_instance.save()
            s = requests.Session()

            answ = s.request(
                "DELETE", f"https://api-staging.rarible.org/v0.1/items/ETHERIUM:{input.address}:0/resetMeta")
            print("RESET RARRIBLE: ", answ)
            answ = s.request(
                "GET", f"https://api-staging.rarible.org/v0.1/items/ETHERIUM:{input.address}:0")
            print("GETELEMENTID RARRIBLE: ", answ)
            return updateMNFT(ok=ok, MNFT=mnft_instance)
        return updateMNFT(ok=ok, MNFT=None)


class createUser(graphene.Mutation):
    class Arguments:
        input = UserInput()
    ok = graphene.Boolean()
    user = graphene.Field(UserGraphQLType)

    @ staticmethod
    def mutate(root, info, input=None):
        ok = True
        user_instance = User(address=input.address,
                             image=input.image,
                             name=input.name,
                             email=input.email)
        user_instance.save()
        return createUser(ok=ok, user=user_instance)


class updateUser(graphene.Mutation):
    class Arguments:
        address = graphene.String(required=True)
        input = UserInput()
    ok = graphene.Boolean()
    user = graphene.Field(UserGraphQLType)

    @staticmethod
    def mutate(root, info, address, input=None):
        ok = False
        user_instance = User.objects.get(pk=address)
        if user_instance:
            ok = True
            user_instance.image = image = input.image
            user_instance.name = image = input.name
            user_instance.email = image = input.email
            user_instance.save()
            return updateUser(ok=ok, user=user_instance)
        return updateUser(ok=ok, user=None)


class createOrUpdateUser(graphene.Mutation):
    class Arguments:
        input = UserInput()
    ok = graphene.Boolean()
    user = graphene.Field(UserGraphQLType)

    @ staticmethod
    def mutate(root, info, input=None):
        ok = True
        user_instance, create = User.objects.update_or_create(address=input.address,
                                                              image=input.image,
                                                              name=input.name,
                                                              email=input.email)
        user_instance.save()
        return createUser(ok=ok, user=user_instance)


class Mutation(graphene.ObjectType):
    createMNFT = createMNFT.Field()
    updateMNFT = updateMNFT.Field()
    createUser = createUser.Field()
    updateUser = updateUser.Field()
    createOrUpdateUser = createOrUpdateUser.Field()