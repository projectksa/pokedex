# Generated by Django 4.2.7 on 2023-11-26 20:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0002_alter_pokemon_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='img',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
