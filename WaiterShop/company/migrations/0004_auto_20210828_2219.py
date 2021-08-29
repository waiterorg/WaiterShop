# Generated by Django 3.2.6 on 2021-08-28 17:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('company', '0003_auto_20210828_2132'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='name',
            field=models.CharField(default='none', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='company',
            name='social_media',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.socialmedia'),
        ),
        migrations.AlterField(
            model_name='company',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='socialmedia',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]