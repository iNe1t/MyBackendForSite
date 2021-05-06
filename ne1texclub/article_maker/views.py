from django.shortcuts import render
from article_maker.models import Post

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

def about(request):
        # get the blog posts that are published
        posts = Post.objects.filter(published=True).order_by('-date')[0:3]
        # now return the rendered template
        return render(request, 'some_app/index.html', {'post': posts})
