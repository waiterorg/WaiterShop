# Generated by Django 3.2.6 on 2021-08-28 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_auto_20210828_1604'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teammember',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='teammember',
            name='name',
        ),
        migrations.RemoveField(
            model_name='teammember',
            name='social_media',
        ),
    ]
