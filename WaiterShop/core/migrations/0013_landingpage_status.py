# Generated by Django 3.2.6 on 2021-08-29 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_rename_landingpagepicture_landingpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='landingpage',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]