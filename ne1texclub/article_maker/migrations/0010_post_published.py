# Generated by Django 3.1.6 on 2021-05-25 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article_maker', '0009_auto_20210525_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='published',
            field=models.BooleanField(default=True),
        ),
    ]
