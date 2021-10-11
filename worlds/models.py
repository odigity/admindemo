from django.db import models
from django.db.models.fields.related import ManyToManyField


# multi-root hierarchy
class Medium(models.Model):
    label = models.CharField(max_length=30)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)


class Universe(models.Model):
    name = models.CharField(max_length=30)


# orderable both by release (pub_date) or in-world chronology (_order)
class UnitOfFiction(models.Model):
    universe = models.ForeignKey(Universe, on_delete=models.CASCADE)
    medium = models.ForeignKey(Medium, on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    length = models.IntegerField(null=True)                 # can represent pages or minutes
    pub_date = models.DateField()

    class Meta:
        order_with_respect_to = 'universe'                  # adds column `_order`
        verbose_name_plural = 'units of fiction'


class Character(models.Model):
    name = models.CharField(max_length=30)
    appearances = ManyToManyField(UnitOfFiction)            # adds table `worlds_character_appearances`
    friends = ManyToManyField('self', symmetrical=True)     # adds table `worlds_character_friends`


class Series(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'series'


class Episode(UnitOfFiction):
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    number = models.CharField(max_length=10)
