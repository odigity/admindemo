from django import forms
from django.contrib import admin

from .models import Character, Episode, Medium, Series, UnitOfFiction, Universe


class CharacterAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['friends'].queryset = Character.objects.filter(universe=self.instance.universe)

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    form = CharacterAdminForm


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
#    pass
#    fields = ('name', ('creator', 'birth_year'))
    fieldsets = (
        ( None, { 'description': "Optional description.", 'fields': ('name',) } ),
#        ( 'Creation', { 'description': "Optional description.", 'fields': ('creator', 'birth_year') } ),
        ( 'Creation', { 'classes': ('collapse',), 'description': "Optional description.", 'fields': ('creator', 'birth_year') } ),
    )
