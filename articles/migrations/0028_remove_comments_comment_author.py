# Generated by Django 3.0.7 on 2020-06-19 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0027_auto_20200619_1400'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='comment_author',
        ),
    ]
