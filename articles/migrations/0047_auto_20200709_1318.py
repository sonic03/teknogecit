# Generated by Django 3.0.7 on 2020-07-09 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0046_auto_20200709_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='slug',
            field=models.SlugField(editable=False, max_length=300, unique=True),
        ),
    ]
