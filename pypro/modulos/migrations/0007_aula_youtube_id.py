# Generated by Django 3.1.5 on 2021-02-10 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0006_aula'),
    ]

    operations = [
        migrations.AddField(
            model_name='aula',
            name='youtube_id',
            field=models.CharField(default='1', max_length=32),
        ),
    ]
