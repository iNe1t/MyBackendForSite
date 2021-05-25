# Generated by Django 3.1.6 on 2021-05-25 10:45

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('article_maker', '0007_auto_20210525_1147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='Short_text',
        ),
        migrations.RemoveField(
            model_name='post',
            name='img_for_post',
        ),
        migrations.AddField(
            model_name='post',
            name='content',
            field=tinymce.models.HTMLField(default='text'),
            preserve_default=False,
        ),
    ]
