# Generated by Django 3.0.7 on 2020-06-19 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0029_comments_comment_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='comment_author',
            new_name='commet_author',
        ),
        migrations.RenameField(
            model_name='comments',
            old_name='comment_content',
            new_name='commet_content',
        ),
    ]
