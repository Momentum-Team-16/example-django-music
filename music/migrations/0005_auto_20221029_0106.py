# Generated by Django 4.1.2 on 2022-10-29 01:06
# This is a data migration.
# Its purpose is to populate the Genres table in the database.
# https://docs.djangoproject.com/en/4.1/topics/migrations/#data-migrations

from django.db import migrations
import genres as genre_data
from django.utils.text import slugify


def create_genres(apps, schema_editor):
    Genre = apps.get_model("music", "Genre")
    for genre_name in genre_data.genres:
        Genre.objects.get_or_create(name=genre_name, slug=slugify(genre_name))

class Migration(migrations.Migration):

    dependencies = [
        ("music", "0004_album_genre"),
    ]

    operations = [migrations.RunPython(create_genres)]