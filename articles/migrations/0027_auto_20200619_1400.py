# Generated by Django 3.0.7 on 2020-06-19 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0026_auto_20200619_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment_author',
            field=models.CharField(max_length=50),
        ),
    ]
