# Generated by Django 3.1.6 on 2021-02-27 14:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('data', models.DateTimeField(auto_now=True)),
                ('author', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article_maker.category')),
            ],
        ),
    ]