from django.contrib import admin
from .models import Character, Race, Technique, Planet, Location
# Register your models here.
admin.site.register(Character)
admin.site.register(Race)
admin.site.register(Technique)
admin.site.register(Planet)
admin.site.register(Location)