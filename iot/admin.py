from django.contrib import admin
from iot.models import Dht22Bathroom


@admin.register(Dht22Bathroom)
class PostAdmin(admin.ModelAdmin):
    pass
