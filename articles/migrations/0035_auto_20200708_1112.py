# Generated by Django 3.0.7 on 2020-07-08 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0034_auto_20200708_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='category',
            field=models.CharField(choices=[('green', 'green'), ('red', 'red')], max_length=80, verbose_name='Kategori'),
        ),
    ]