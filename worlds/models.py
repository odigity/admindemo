from django.db import models
from django.db.models.fields.related import ManyToManyField


# multi-root hierarchy
class Medium(models.Model):
    label = models.CharField(max_length=30)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.label


class Universe(models.Model):
    name = models.CharField(max_length=30)
    creator = models.CharField(max_length=30)
    birth_year = models.IntegerField()

    def __str__(self):
        return self.name


# orderable both by release (pub_date) or in-world chronology (_order)
class UnitOfFiction(models.Model):
    universe = models.ForeignKey(Universe, on_delete=models.CASCADE)
    medium = models.ForeignKey(Medium, on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    length = models.IntegerField(null=True)                 # can represent pages or minutes
    pub_date = models.DateField()

    class Meta:
        order_with_respect_to = 'universe'                  # +column:_order
        verbose_name_plural = 'units of fiction'

    def __str__(self):
        return f"{self.title} ({self.pub_date})"


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
