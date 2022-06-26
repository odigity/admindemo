# Generated by Django 3.2.13 on 2022-06-26 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worlds', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='universe',
            name='birth_year',
            field=models.IntegerField(help_text='help_text for birth_year', verbose_name='verbose_name for birth_year'),
        ),
        migrations.AlterField(
            model_name='universe',
            name='creator',
            field=models.CharField(help_text='help_text for creator', max_length=30, verbose_name='verbose_name for creator'),
        ),
        migrations.AlterField(
            model_name='universe',
            name='name',
            field=models.CharField(help_text='help_text for name', max_length=30, verbose_name='verbose_name for name'),
        ),
    ]