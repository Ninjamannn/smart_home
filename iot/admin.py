from django.contrib import admin
from iot.models import Dht22


@admin.register(Dht22)
class PostAdmin(admin.ModelAdmin):
    pass
