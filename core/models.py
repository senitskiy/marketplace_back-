from pydoc import describe
from django.db import models


class Web3Model(models.Model):
    ''' Абстрактная модель для всех сущностей web3.0 
        address - адрес кошелька,
        alias - ссылка на профиль, если не указано равняется address
        displayName - удобочитаемое имя
        description - описание
    '''
    address = models.CharField(max_length=300,  unique=True, primary_key=True)
    alias = models.CharField(max_length=300, unique=True) 
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
        address - адрес кошелька,
        alias - ссылка на профиль, если не указано равняется address
        displayName - удобочитаемое имя
        description - описание
        avatar - URL ссылка на аватар пользователя
        avatartMNFT - MNFT в качестве аватара, с текущим состоянием
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
        name - название сети (etherium, polygon)
        idChain - идентификационный номер сети
        rpcURL - URL для доступа к сети
        browserURL - URL просмотрщика сети
    '''
    name = models.CharField(max_length=30)
    idChain = models.IntegerField(default=0)
    rpcURL = models.URLField()
    browserURL = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}"


class MNFTCollection(Web3Model):
    ''' Колекция MNFT: 
        address - адрес кошелька,
        alias - ссылка на коллекцию, если не указано равняется address
        displayName - удобочитаемое имя
        description - описание
        symbol - хз че такое, но вроде нужная вещь
        blockchain - в каком блокчейне размещается
    '''

    symbol = models.CharField(max_length=10)
    blockchain = models.ForeignKey(to="Blockchain", on_delete=models.CASCADE, related_name='mnft_collections')


class MNFT(Web3Model):
    ''' MNFT: 
        address - адрес кошелька,
        alias - ссылка на коллекцию, если не указано равняется address
        displayName - удобочитаемое имя
        description - описание
        collection - к какой коллекции отностися MNFT
        tokenId - id mnft
        creatorAddress - адрес создателя
        ownerAddress - адрес владельца
        sponsorAddress - адрес спонсора
        price - цена продажи
        priceAd - цена аренды
        startRent - старт аренды MNFT для рекламы
        endRent - окончание аренды MNFT для рекламы
        OriginCID - CID оригинального изображения
        AdvCID - CID оригинального изображения с рекламной вставкой
    '''
    collection = models.ForeignKey(to='MNFTCollection', on_delete=models.CASCADE, related_name='mnfts')
    tokenId = models.IntegerField(default=0)
    creatorAddress = models.ForeignKey(to='User', on_delete=models.CASCADE, related_name="mnfts_creator")
    ownerAddress = models.ForeignKey(to='User', on_delete=models.CASCADE, related_name="mnfts_owner")  
    sponsorAddress = models.ForeignKey(to='User', on_delete=models.CASCADE, related_name="mnfts_lord", null=True, blank=True)
    price = models.FloatField(default=0.0)
    priceAd = models.FloatField(default=0.0)
    startRent = models.DateTimeField(null=True, blank=True)
    endRent = models.DateTimeField(null=True, blank=True)
    OriginCID = models.CharField(max_length=300, null=True, blank=True)
    AdvCID = models.CharField(max_length=300, null=True, blank=True)

    def save(self, *args, **kwargs) -> None:
        if not self.ownerAddress:
           self.ownerAddress = self.creatorAddress
        super().save(*args, **kwargs)

    def get_image(self):
        pass

