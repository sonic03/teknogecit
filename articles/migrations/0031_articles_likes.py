# Generated by Django 3.0.7 on 2020-06-24 08:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0030_auto_20200619_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
