from django.db import models

title = models.TextField(max_length=30, default="Новая статья")
text = models.TextField(max_length=500, default="Предположим тут есть текст. Не трогай его!")

# Create your models here.
