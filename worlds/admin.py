from django import forms
from django.contrib import admin

from .models import Character, Episode, Medium, Series, UnitOfFiction, Universe


class CharacterAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['appearances'].queryset = UnitOfFiction.objects.filter(universe=self.instance.universe)
        self.fields['friends'].queryset = Character.objects.filter(universe=self.instance.universe).exclude(id=self.instance.id)

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
    list_display = [ 'label', 'parent_label' ]
    list_select_related = [ 'parent' ]                                      # optimize queries
#    ordering = [ 'parent__label' ]


@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
#    pass
    readonly_fields = ('universe',)


@admin.register(UnitOfFiction)
class UnitOfFictionAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'
#    list_display = [ 'universe', 'ordinal', 'title', 'pub_date' ]
#    list_display = [ 'orderable_universe', 'ordinal', 'title', 'pub_date' ]
#    list_display = [ 'universe_name', 'ordinal', 'medium_label', 'title', 'pub_date' ]
#    list_display_links = [ 'title' ]
#    list_filter = [ 'pub_date' ]
    list_filter = [ 'pub_date', 'medium', 'universe', 'length' ]
#    list_select_related = [ 'medium', 'universe' ]                          # optimize queries
#    ordering = [ 'universe', 'ordinal' ]
#    ordering = [ 'universe__name', 'ordinal' ]
    readonly_fields = [ 'universe' ]


class CharacterInline(admin.StackedInline):
#class CharacterInline(admin.TabularInline):
    model = Character
    extra = 0
#    show_change_link = True
    fields = [ 'name', 'friends' ]
    readonly_fields = [ 'friends' ]
#    fieldsets = [
#        ( None, { 'fields': [ 'name' ] } ),
#        ( 'Associations', { 'fields': [ 'friends' ] } ),
#    ]
#    def has_change_permission(self, request, obj=None):
#        return False

@admin.register(Universe)
class UniverseAdmin(admin.ModelAdmin):
#    pass
#    fields = [ 'name', 'creator', 'birth_year' ]
#    fields = [ 'name', ( 'creator', 'birth_year' ) ]
#    fields = [ 'name', [ 'creator', 'birth_year' ] ]
#    fieldsets = [
#        ( None, { 'description': "Optional description.", 'fields': [ 'name' ] } ),
#        ( 'Creation', { 'description': "Optional description.", 'fields': [ 'creator', 'birth_year' ] } ),
#        ( 'Creation', { 'classes': ('collapse',), 'description': "Optional description.", 'fields': [ 'creator', 'birth_year' ] } ),
#    ]
#    list_display = [ 'birth_year', 'name', 'creator' ]
#    list_display_links = None
#    list_display_links = [ 'name' ]
#    list_editable = [ 'creator' ]
#    list_filter = [ 'birth_year', 'creator' ]
#    ordering = [ 'name' ]
#    readonly_fields = [ 'creator' ]
#    save_as = True
#    save_on_top = True
#    search_fields = [ 'name', 'creator' ]
    inlines = [ CharacterInline ]
