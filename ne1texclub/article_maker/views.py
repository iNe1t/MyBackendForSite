from django.shortcuts import render
from .models import Post
 
 
def article_maker(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, "posts/articles.html", context)
 
 
def post_page(request, post_id):
    context = {
        'post': Post.objects.get(id=post_id)
    }
    return render(request, "posts/post.html", context)
