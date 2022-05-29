from django.contrib import admin
from core.models import MNFT, User, MNFTCollection, Blockchain
# Register your models here.

admin.site.register(MNFT)
admin.site.register(User)
admin.site.register(MNFTCollection)
admin.site.register(Blockchain)