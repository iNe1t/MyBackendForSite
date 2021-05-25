"""ne1texclub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from article_maker import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include('some_app.urls')),
    path('admin/', admin.site.urls),
    path('articles/', include('article_maker.urls')),
    path('log_in/', include('authen.urls')),
    path('register/', include('registration.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('post/<int:post_id>', views.post_page),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
