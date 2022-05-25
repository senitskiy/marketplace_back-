from django.db import models


class User(models.Model):
    address = models.CharField(max_length=300,  unique=True, primary_key=True)
    image = models.CharField(max_length=300, null=True, blank=True)
    name = models.CharField(max_length=300, null=True, blank=True)
    email = models.CharField(max_length=300, null=True, blank=True)


class MNFT(models.Model):
    types_blockchain = (
        (0, "ETHEREUM"),
        (1, "SOLANA"),
        (2, "TEZOS"),
        (3, "EVERSCALE"),
    )

    types_standart = (
        (721, "ERC721"),
        (1155, "ERC1155"),
    )
    address = models.CharField(max_length=300, unique=True, primary_key=True,)
    blockchain = models.IntegerField(default=0, choices=types_blockchain)
    symbol = models.CharField(max_length=300, null=True, blank=True)
    standart = models.IntegerField(default=721, choices=types_standart)
    lastUpdate = models.DateField(auto_now=True)
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=300, null=True, blank=True)
    image = models.CharField(max_length=300)
    cost = models.FloatField(default=0.0)
    costAd = models.FloatField(default=0.0)
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="mnfts_creator")
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="mnfts_owner")
    sponsor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="mnfts_lord", null=True, blank=True)
