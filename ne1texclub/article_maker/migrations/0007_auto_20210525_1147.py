# Generated by Django 3.1.6 on 2021-05-25 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article_maker', '0006_post_published'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='text',
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default='category', on_delete=django.db.models.deletion.CASCADE, to='article_maker.category'),
        ),
    ]
