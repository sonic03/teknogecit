# Generated by Django 3.0.7 on 2020-06-19 10:02

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0017_auto_20200619_1258'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Coments',
        ),
    ]
