from pydoc import describe
from django.db import models
from time import time

class Web3Model(models.Model):
    ''' Абстрактная модель для всех сущностей web3.0 
        address - адрес кошелька, первичный ключ
        alias - ссылка на профиль, если не указано равняется address, обязательный, уникальный
        displayName - удобочитаемое имя, необязательный
        description - описание, необязательный
    '''
    address = models.CharField(max_length=300,  unique=True, primary_key=True)
    alias = models.CharField(max_length=300, unique=True, blank=True) 
    displayName = models.CharField(max_length=300, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    
    def save(self, *args, **kwargs) -> None:
        if not self.alias:
           self.alias = self.address
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        display = self.displayName if self.displayName else self.address
        return f"{display}"

    class Meta:
        abstract = True


class User(Web3Model):
    ''' Класс пользователя (владельца, создателя, спонсора):
        address - адрес кошелька, первичный ключ
        alias - ссылка на профиль, если не указано равняется address, обязательный, уникальный
        displayName - удобочитаемое имя, необязательный
        description - описание, необязательный
        avatar - URL ссылка на аватар пользователя, необязательный
        avatartMNFT - MNFT в качестве аватара, с текущим состоянием, необязательный
    '''
    avatar = models.URLField(null=True, blank=True)
    avatarMNFT = models.ForeignKey(to='MNFT', on_delete=models.CASCADE, related_name='avatars', null=True, blank=True)

    def get_avatar(self) -> str:
        if self.avatarMNFT:
            return self.avatarMNFT.get_image()
        else:
            return self.avatar


class Blockchain(models.Model):
    ''' Класс описания блокчейн сети (сделан на основе полей metamask):
        id - автоинкремент, первичный ключ
        name - название сети (etherium, polygon), обязательный
        idChain - идентификационный номер сети, обязательный
        rpcURL - URL для доступа к сети, обязательный
        symbol - название токена, обязательный
        browserURL - URL просмотрщика сети, необязательный
    '''
    name = models.CharField(max_length=30)
    idChain = models.IntegerField(default=0)
    rpcURL = models.URLField()
    browserURL = models.URLField(blank=True, null=True)
    symbol = models.CharField(max_length=10)   

    def __str__(self):
        return f"{self.name}"


class MNFTCollection(Web3Model):
    ''' Колекция MNFT: 
        address - адрес коллекции, первичный ключ
        alias - ссылка на профиль, если не указано равняется address, обязательный, уникальный
        displayName - удобочитаемое имя, необязательный
        description - описание, необязательный
        blockchain - в каком блокчейне размещается, обязательный
    '''
    blockchain = models.ForeignKey(to="Blockchain", on_delete=models.CASCADE, related_name='mnft_collections')


class MNFT(Web3Model):
    ''' MNFT: 
        address - адрес MNFT, первичный ключ
        alias - ссылка на профиль, если не указано равняется address, обязательный, уникальный
        displayName - удобочитаемое имя, необязательный
        description - описание, необязательный
        collection - к какой коллекции отностися MNFT, обязательный
        tokenId - id mnft, необязательный, поумолчанию равен 0
        creatorAddress - адрес создателя, обязательный
        ownerAddress - адрес владельца, обязательный, если не указан, равняется createrAddress
        sponsorAddress - адрес спонсора, необязательный
        price - рекомендуемая цена продажи, необязательный, поумолчанию равен 0.0
        priceAd - рекомендуемая цена аренды, необязательный, поумолчанию равен 0.0
        startRent - время старта аренды MNFT для рекламы, необязаетльный
        endRent - время окончания аренды MNFT для рекламы, необязаетльный
        OriginCID - CID оригинального изображения, обязательный
        AdvCID - CID оригинального изображения с рекламной вставкой, необязательный
    '''
    collection = models.ForeignKey(to='MNFTCollection', on_delete=models.CASCADE, related_name='mnfts')
    tokenId = models.IntegerField(default=0)
    creatorAddress = models.ForeignKey(to='User', on_delete=models.CASCADE, related_name="created_MNFTs")
    ownerAddress = models.ForeignKey(to='User', on_delete=models.CASCADE, related_name="owned_MNFTs")  
    sponsorAddress = models.ForeignKey(to='User', on_delete=models.CASCADE, related_name="sponsored_MNFTs", null=True, blank=True)
    price = models.FloatField(default=0.0)
    priceAd = models.FloatField(default=0.0)
    startRent = models.DateTimeField(null=True, blank=True)
    endRent = models.DateTimeField(null=True, blank=True)
    originCID = models.CharField(max_length=300)
    advCID = models.CharField(max_length=300, null=True, blank=True)

    def save(self, *args, **kwargs) -> None:
        if not self.ownerAddress:
           self.ownerAddress = self.creatorAddress
        super().save(*args, **kwargs)

    def get_image(self):
        now = time()
        if self.startRent is None or self.endRent is None:
            return self.originCID
        if now < self.endRent.timestamp() and now > self.startRent.timestamp():
            return self.advCID
        else:
            return self.originCID

