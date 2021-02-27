from django.shortcuts import render

def article_maker(request):
    return render(request, 'posts/articles.html')
