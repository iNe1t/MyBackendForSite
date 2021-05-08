from django.shortcuts import render
from article_maker.views import last_post

def index(request):
    return render(request, 'some_app/index.html', last_post(request))
# Create your views here.
