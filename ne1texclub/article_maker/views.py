from django.shortcuts import render
from article_maker.models import Post
from django.views.generic import DetailView

class post(DetailView):
    model = Post
    template_name  = 'post.html'
    slug_field = 'pk'

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

def last_post(request):
        # get the blog posts that are published
        last_post = Post.objects.filter(published=True).order_by('-date')[0:1]
        # now return the rendered template
        return {'last_post': last_post}
