from django.shortcuts import render

def article_maker(request):
    return render(request, 'some_app/article.html')
