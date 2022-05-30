import graphene
from core.models import MNFTCollection, MNFT, User, Blockchain


class MNFTInput(graphene.InputObjectType):
    address = graphene.String(required=True, description='адрес MNFT')
    alias = graphene.String(required=False, description='Уникальное имя MNFT')
    displayName = graphene.String(description='Удобочитаемое имя')
    description = graphene.String(description='Описание')
    collection = graphene.ID(description='Ссылка на коллекцию')
    tokenId = graphene.Int(description='ID MNFT')
    creatorAddress = graphene.ID(description='адрес создателя')
    ownerAddress = graphene.ID(description='адрес владельца, если не указан, равняется createrAddress') 
    sponsorAddress = graphene.ID(description='адрес спонсора')
    price = graphene.Float(description='Рекомендуемая цена продажи')
    priceAd = graphene.Float(description='Рекомендуемая цена аренды')
    startRent = graphene.DateTime(description='Время старта аренды MNFT для рекламы')
    endRent = graphene.DateTime(description='Время окончания аренды MNFT для рекламы')
    OriginCID = graphene.String(description='CID оригинального изображения')
    AdvCID = graphene.String(description='CID оригинального изображения с рекламной вставкой')

    class Meta:
        model = MNFT
        description = 'MNFT'


class UserInput(graphene.InputObjectType):
    address = graphene.String(required=True, description='Адрес кошелька')
    alias = graphene.String(required=False, description='Уникальное имя профиля')
    displayName = graphene.String(description='Отображаемое имя')
    description = graphene.String(description='Описание')
    avatar = graphene.String(description='Изображение аватара протокол http')
    avatarMNFT = graphene.ID(description='Ссылка на MNFT в качестве аватара')
    createdMnfts = graphene.List(description='Список MNFT, где пользователь автор', of_type=MNFTInput)
    ownedMnfts = graphene.List(description='Список MNFT, где пользователь владелец', of_type=MNFTInput)
    sponsoredMnfts = graphene.List(description='Список MNFT, где пользователь спонсор', of_type=MNFTInput)
    class Meta:
        model = User
        description = 'Пользователь (создатель, владелец, спонсор)'



class MNFTCollectionInput(graphene.InputObjectType):
    address = graphene.String(required=True, description='Адрес коллекции')
    alias = graphene.String(required=False, description='Уникальное имя коллекции')
    displayName = graphene.String(description='Удобочитаемое имя')
    description = graphene.String(description='Описание')
    blockchain = graphene.ID(description='Ссылка на описание блокчейна')
    mnfts = graphene.List(description='Список MNFT в коллекции', of_type=MNFTInput)
    class Meta:
        model = MNFTCollection
        description = 'MNFT коллекция'


class BlockchainInput(graphene.InputObjectType):
    id = graphene.Int(required=True, description='Идентификатор в БД')
    name = graphene.String(description='Имя сети')
    idChain = graphene.Int(description='ID цепочки')
    rpcURL = graphene.String(description='URL-адрес RPC')
    browserURL = graphene.String(description='URL-адрес проводника блоков')
    symbol = graphene.String(description='Символ валюты')
    mnftCollections = graphene.List(description='Коллекции MNFT в этой сети', of_type=MNFTCollectionInput)
    class Meta:
        model = Blockchain
        description = 'Описание блокчейна (как у Metamask)'


