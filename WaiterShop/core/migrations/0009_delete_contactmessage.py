# Generated by Django 3.2.6 on 2021-08-28 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_rename_contactmassage_contactmessage'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ContactMessage',
        ),
    ]
