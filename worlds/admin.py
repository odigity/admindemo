from django.contrib import admin

from .models import Character, Episode, Medium, Series, UnitOfFiction, Universe


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    pass


@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    pass


@admin.register(Medium)
class MediumAdmin(admin.ModelAdmin):
    pass


@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    pass


@admin.register(UnitOfFiction)
class UnitOfFictionAdmin(admin.ModelAdmin):
    pass


@admin.register(Universe)
class UniverseAdmin(admin.ModelAdmin):
    pass


