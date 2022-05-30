import graphene
from core.graphql.types import MNFTCollectionGraphQLType, MNFTGraphQLType, UserGraphQLType, BlockchainGraphQLType
from core.graphql.inputs import MNFTCollectionInput, MNFTInput, UserInput, BlockchainInput
from core.models import MNFTCollection, MNFT, User, Blockchain


class CreateUser(graphene.Mutation):
    class Arguments:
        user = UserInput(required=True)
    
    class Meta:
        description = 'Создает пользователя'
    
    user = graphene.Field(UserGraphQLType, description='Данные о пользователе')
    isCreated = graphene.Boolean(description='Равен истина если пользователь был создан, иначе ложь')

    @classmethod
    def mutate(cls, root, info, user):
        userInstance = User.objects.create(**user)
        userInstance.save()
        return CreateUser(user=userInstance, isCreated=True)


class CreateOrUpdateUser(graphene.Mutation):
    class Arguments:
        user = UserInput(required=True)
    
    class Meta:
        description = 'Обновляет данные о пользователе, если его нет то создает'
    
    user = graphene.Field(UserGraphQLType, description='Данные о пользователе')
    isCreated = graphene.Boolean(description='Равен истина если пользователь был создан, иначе ложь')
    
    @classmethod
    def mutate(cls, root, info, user):
        (userInstance, isCreated) = User.objects.update_or_create(defaults=user, pk=user.address)
        return CreateOrUpdateUser(user=userInstance, isCreated=isCreated)


class DeleteUser(graphene.Mutation):
    class Arguments:
        address = graphene.String(required=True, description='Адрес')
    
    class Meta:
        description = 'Удаляет пользователя'
    
    isDeleted = graphene.Boolean(description='Результат удаления')

    @classmethod
    def mutate(cls, root, info, address):
        isDeleted = (User.objects.get(pk=address).delete()) is not None
        return DeleteUser(isDeleted=isDeleted)


class CreateMNFT(graphene.Mutation):
    class Arguments:
        mnft = MNFTInput(required=True)
    
    class Meta:
        description = 'Создает MNFT'
    
    mnft = graphene.Field(MNFTGraphQLType, description='Данные о MNFT')
    isCreated = graphene.Boolean(description='Равен истина если MNFT был создан, иначе ложь')

    @classmethod
    def mutate(cls, root, info, mnft):
        mnftInstance = MNFT.objects.create(**mnft)
        mnftInstance.save()
        return CreateMNFT(mnft=mnftInstance, isCreated=True)


class CreateOrUpdateMNFT(graphene.Mutation):
    class Arguments:
        mnft = MNFTInput(required=True)
    
    class Meta:
        description = 'Обновляет данные о MNFT, если его нет то создает'
    
    mnft = graphene.Field(MNFTGraphQLType, description='Данные о MNFT')
    isCreated = graphene.Boolean(description='Равен истина если MNFT был создан, иначе ложь')

    @classmethod
    def mutate(cls, root, info, mnft):
        (mnftInstance, isCreated) = MNFT.objects.update_or_create(defaults=mnft, pk=mnft.address)
        return CreateOrUpdateMNFT(user=mnftInstance, isCreated=isCreated)


class DeleteMNFT(graphene.Mutation):
    class Arguments:
        address = graphene.String(required=True, description='Адрес')
    
    class Meta:
        description = 'Удаляет MNFT'
    
    isDeleted = graphene.Boolean(description='Результат удаления')

    @classmethod
    def mutate(cls, root, info, address):
        isDeleted = (MNFT.objects.get(pk=address).delete()) is not None
        return DeleteMNFT(isDeleted=isDeleted)


class CreateMNFTCollection(graphene.Mutation):
    class Arguments:
        mnftCollection = MNFTCollectionInput(required=True)
    
    class Meta:
        description = 'Создает коллекцию'
    
    mnftCollection = graphene.Field(MNFTCollectionGraphQLType, description='Данные о коллекции')
    isCreated = graphene.Boolean(description='Равен истина если коллекция была создана, иначе ложь')

    @classmethod
    def mutate(cls, root, info, mnftCollection): 
        mnftCollectionInstance = User.objects.create(**mnftCollection)
        mnftCollectionInstance.save()
        return CreateMNFTCollection(MNFTCollection=mnftCollectionInstance, isCreated=True)


class CreateOrUpdateMNFTCollection(graphene.Mutation):
    class Arguments:
        mnftCollection = MNFTCollectionInput(required=True)
    class Meta:
        description = 'Обновляет данные о коллекции, если ее нет то создает'
    
    mnftCollection = graphene.Field(MNFTCollectionGraphQLType, description='Данные о коллекции')
    isCreated = graphene.Boolean(description='Равен истина если коллекция была создана, иначе ложь')

    @classmethod
    def mutate(cls, root, info, mnftCollection):
        (mnftCollectionInstance, isCreated) = MNFTCollection.objects.update_or_create(defaults=mnftCollection, pk=mnftCollection.address)
        return CreateOrUpdateMNFTCollection(user=mnftCollectionInstance, isCreated=isCreated)


class DeleteMNFTCollection(graphene.Mutation):
    class Arguments:
        address = graphene.String(required=True, description='Адрес')
    
    class Meta:
        description = 'Удаляет коллекцию'
    
    isDeleted = graphene.Boolean(description='Результат удаления')

    @classmethod
    def mutate(cls, root, info, address):
        isDeleted = (MNFTCollection.objects.get(pk=address).delete()) is not None
        return DeleteMNFTCollection(isDeleted=isDeleted)


class CreateBlockchain(graphene.Mutation):
    class Arguments:
        blockchain = BlockchainInput(required=True)
    
    class Meta:
        description = 'Создает блокчейн'
    
    blockchain = graphene.Field(BlockchainGraphQLType, description='Данные о блокчейне')
    isCreated = graphene.Boolean(description='Равен истина если блокчейн был создан, иначе ложь')

    @classmethod
    def mutate(cls, root, info, blockchain): 
        blockchainInstance = User.objects.create(**blockchain)
        blockchainInstance.save()
        return CreateBlockchain(blockchain=blockchainInstance, isCreated=True)


class CreateOrUpdateBlockchain(graphene.Mutation):
    class Arguments:
        blockchain = BlockchainInput(required=True)
    class Meta:
        description = 'Обновляет данные о блокчейне, если его нет то создает'
    
    blockchain = graphene.Field(BlockchainGraphQLType, description='Данные о блокчейне')
    isCreated = graphene.Boolean(description='Равен истина если блокчейн был создан, иначе ложь')

    @classmethod
    def mutate(cls, root, info, blockchain):
        (blockchainInstance, isCreated) = Blockchain.objects.update_or_create(defaults=blockchain, pk=blockchain.id)
        return CreateOrUpdateMNFTCollection(blockchain=blockchainInstance, isCreated=isCreated)


class DeleteBlockchain(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True, description='ID')
    
    class Meta:
        description = 'Удаляет блокчейн'
    
    isDeleted = graphene.Boolean(description='Результат удаления')

    @classmethod
    def mutate(cls, root, info, address):
        isDeleted = (Blockchain.objects.get(pk=id).delete()) is not None
        return DeleteBlockchain(isDeleted=isDeleted)

class Mutation(graphene.ObjectType):
    createUser = CreateUser.Field()
    createOrUpdateUser = CreateOrUpdateUser.Field()
    deleteUser = DeleteUser.Field()
    createMNFT = CreateMNFT.Field()
    createOrUpdateMNFT = CreateOrUpdateMNFT.Field()
    deleteMNFT = DeleteMNFT.Field()
    createMNFTCollection = CreateMNFTCollection.Field()
    createOrUpdateMNFTCollection = CreateOrUpdateMNFTCollection.Field()
    deleteMNFTCollection = DeleteMNFTCollection.Field()
    createBlockchain = CreateBlockchain.Field()
    CreateOrUpdateBlockchain = CreateOrUpdateBlockchain.Field()
    DeleteBlockchain = DeleteBlockchain.Field()