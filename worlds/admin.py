from django import forms
from django.contrib import admin

from .models import Character, Episode, Medium, Series, UnitOfFiction, Universe


class CharacterAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['friends'].queryset = Character.objects.filter(universe=self.instance.universe)

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
#    pass
    form = CharacterAdminForm
    readonly_fields = ('universe',)


@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    pass


@admin.register(Medium)
class MediumAdmin(admin.ModelAdmin):
#    pass
    list_display = ('label', 'parent', 'parent_id')
    list_select_related = ('parent',)   # optimize queries

@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
#    pass
    readonly_fields = ('universe',)


@admin.register(UnitOfFiction)
class UnitOfFictionAdmin(admin.ModelAdmin):
#    date_hierarchy = 'pub_date'
    readonly_fields = ('universe',)


@admin.register(Universe)
class UniverseAdmin(admin.ModelAdmin):
    pass
#    fields = ('name', ('creator', 'birth_year'))
#    fieldsets = (
#        ( None, { 'description': "Optional description.", 'fields': ('name',) } ),
#        ( 'Creation', { 'description': "Optional description.", 'fields': ('creator', 'birth_year') } ),
#        ( 'Creation', { 'classes': ('collapse',), 'description': "Optional description.", 'fields': ('creator', 'birth_year') } ),
#    )
#    list_display = ('birth_year', 'name', 'creator')
#    list_display_links = None
#    list_display_links = ('name',)
#    list_editable = ('creator',)
#    list_filter = ('birth_year', 'creator')
#    readonly_fields = ('creator',)
#    save_as = True
#    save_on_top = True
#    search_fields = ('name', 'creator')
