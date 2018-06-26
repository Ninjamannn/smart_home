from django.contrib import admin
from iot.models import Bathroom, Liveroom


@admin.register(Bathroom)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Liveroom)
class PostAdmin(admin.ModelAdmin):
    pass
