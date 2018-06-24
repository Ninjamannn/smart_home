from django.contrib import admin
from iot.models import Dht22Bathroom, Liveroom


@admin.register(Dht22Bathroom)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Liveroom)
class PostAdmin(admin.ModelAdmin):
    pass
