# Generated by Django 3.1.5 on 2021-02-08 19:43

from django.db import migrations
from django.template.defaultfilters import slugify


def popular_slug(apps, schema_editor):
    Modulo = apps.get_model('modulos', 'Modulo')
    for modulo in Modulo.objects.all():
        modulo.slug = slugify(modulo.titulo)
        modulo.save(())


class Migration(migrations.Migration):
    dependencies = [
        ('modulos', '0003_modulo_slug'),
    ]

    operations = [
        migrations.RunPython(popular_slug)
    ]
