# Generated by Django 3.1.6 on 2021-03-06 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article_maker', '0003_post_img_for_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Short_text',
            field=models.TextField(max_length=75, null=True),
        ),
    ]
