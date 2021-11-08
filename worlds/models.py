from django.contrib import admin
from django.db import models
from django.db.models.fields.related import ManyToManyField


# multi-root hierarchy
class Medium(models.Model):
    label = models.CharField(max_length=30)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.label

    @admin.display(description='parent', ordering='parent__label')
    def parent_label(self):                                 # to facilitate column in Admin
        return self.parent and self.parent.label or None


class Universe(models.Model):
    """Docstring for model Universe."""
    name = models.CharField(max_length=30, verbose_name="verbose_name for name", help_text="help_text for name")
    creator = models.CharField(max_length=30, verbose_name="verbose_name for creator", help_text="help_text for creator")
    birth_year = models.IntegerField(verbose_name="verbose_name for birth_year", help_text="help_text for birth_year")

    def my_instance_method(self):
        """Docstring for my_instance_method."""
        pass

    def my_instance_method_with_params(self, param1):
        """Docstring for my_instance_method_with_params."""
        pass

    def __str__(self):
        return self.name


# orderable both by release (pub_date) or in-world chronology (ordinal)
class UnitOfFiction(models.Model):
    universe = models.ForeignKey(Universe, on_delete=models.CASCADE)
    ordinal = models.IntegerField()
    medium = models.ForeignKey(Medium, on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    length = models.IntegerField(null=True)                 # can represent pages or minutes
    pub_date = models.DateField()

    class Meta:
        verbose_name_plural = 'units of fiction'

    def __str__(self):
        return f"{self.title} ({self.pub_date})"

    @admin.display(description='medium', ordering='medium__label')
    def medium_label(self):                                # to facilitate column in Admin
        return self.medium.label

    @admin.display(description='universe', ordering='universe__name')
    def universe_name(self):                                # to facilitate column in Admin
        return self.universe.name


class Character(models.Model):
    universe = models.ForeignKey(Universe, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    appearances = ManyToManyField(UnitOfFiction)            # +table:worlds_character_appearances
    friends = ManyToManyField('self', symmetrical=True)     # +table:worlds_character_friends

    def __str__(self):
        return self.name


class Series(models.Model):
    universe = models.ForeignKey(Universe, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'series'

    def __str__(self):
        return self.title


class Episode(UnitOfFiction):
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    number = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.number} - {self.title} ({self.pub_date})"
