from pydoc import describe
from django.db import models


class User(models.Model):
    address = models.CharField(max_length=300,  unique=True, primary_key=True)
    alias = models.CharField(max_length=300, unique=True) 

    displayName = models.CharField(max_length=300, null=True, blank=True)
    avatar = models.CharField(max_length=300, null=True, blank=True)
    avatarMNFT = models.ForeignKey(to='MNFT', on_delete=models.CASCADE, related_name='avatars', null=True, blank=True)
    #TODO: сделать логику заполнения alias если пусто то =address
    #TODO: сделать логику выдачи аватара


class Blockchain(models.Model):
    name = models.CharField(max_length=30)
    idChain = models.IntegerField(default=0)
    rpcURL = models.URLField()
    browserURL = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}"


class MNFTCollection(models.Model):
    alias = models.CharField(max_length=300, unique=True)
    address = models.CharField(max_length=50)
    displayName = models.CharField(max_length=300)
    symbol = models.CharField(max_length=10)
    description = models.TextField(null=True, blank=True)
    alias = models.CharField(max_length=300, unique=True)
    #TODO: сделать логику заполнения alias если пусто то =address

    blockchain = models.ForeignKey(to="Blockchain", on_delete=models.CASCADE, related_name='mnft_collections')

class MNFT(models.Model):
    collection = models.ForeignKey(to='MNFTCollection', on_delete=models.CASCADE, related_name='mnfts')
    tokenId = models.IntegerField(default=0)
    creatorAddress = models.ForeignKey(to='User', on_delete=models.CASCADE, related_name="mnfts_creator")
    ownerAddress = models.ForeignKey(to='User', on_delete=models.CASCADE, related_name="mnfts_owner")  
    sponsorAddress = models.ForeignKey(to='User', on_delete=models.CASCADE, related_name="mnfts_lord", null=True, blank=True)
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=300, null=True, blank=True)
    price = models.FloatField(default=0.0)
    priceAd = models.FloatField(default=0.0)
