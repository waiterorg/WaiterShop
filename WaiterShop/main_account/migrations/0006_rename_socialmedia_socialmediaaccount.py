# Generated by Django 3.2.6 on 2021-08-28 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_auto_20210828_2231'),
        ('main_account', '0005_auto_20210828_2231'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SocialMedia',
            new_name='SocialMediaAccount',
        ),
    ]
