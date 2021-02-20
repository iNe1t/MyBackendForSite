from django.shortcuts import render

def index(request):
    return render(request, 'some_app/articles.html')

# Create your views here.
