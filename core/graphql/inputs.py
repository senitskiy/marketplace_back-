import graphene


class UserInput(graphene.InputObjectType):
    address = graphene.String(required=True)
    alias = graphene.String()
    displayName = graphene.String()
    description = graphene.String()
    avatar = graphene.String()
    avatarMNFT = graphene.ID()


class BlockchainInput(graphene.InputObjectType):
    id = graphene.Int(required=True)
    name = graphene.String()
    idChain = graphene.Int()
    rpcURL = graphene.String()
    browserURL = graphene.String()


class MNFTCollectionInput(graphene.InputObjectType):
    address = graphene.String(required=True)
    alias = graphene.String()
    displayName = graphene.String()
    description = graphene.String()
    symbol = graphene.String()
    blockchain = graphene.ID()

class MNFTInput(graphene.InputObjectType):
    address = graphene.String(required=True)
    alias = graphene.String()
    displayName = graphene.String()
    description = graphene.String()
    collection = graphene.ID()
    tokenId = graphene.Int()
    creatorAddress = graphene.ID()
    ownerAddress = graphene.ID() 
    sponsorAddress = graphene.ID()
    price = graphene.Float()
    priceAd = graphene.Float()
    startRent = graphene.DateTime()
    endRent = graphene.DateTime()
    OriginCID = graphene.String()
    AdvCID = graphene.String()