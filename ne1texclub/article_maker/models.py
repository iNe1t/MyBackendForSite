from django.contrib.auth.models import User
from django.db import models
 
 
class Category(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    name = models.CharField(max_length=50)
 
    def __str__(self):
        return self.name
 
 
class Post(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    author = models.ManyToManyField(User)
    title = models.CharField(max_length=50)
    text = models.TextField()
    Short_text = models.TextField(max_length=75, null=True)
    date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    img_for_post = models.ImageField(upload_to='images/', null=True, blank=True)
 
    def __str__(self):
        return self.title

# Create your models here.
