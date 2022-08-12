"""nadeemsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from . import view

# code for vedio 6:
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('' , view.index, name='index'),
#     path('about' , view.about, name='about'),
#
# ]

# code for vedio 7:
# code for pipe in django

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', view.index, name='index'),
#     path('removepunc', view.removepunc, name='rempun'),
#     # path('capitlizefirs t', view.capfirst, name='capfirst'),
#
# ]

# CODE FOR BACKEND
from django.views.static import serve
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view.index, name='index'),
    path('analyze', view.analyze, name='analyze'),
    url(r'^ static/(P<path>.*)$', serve, {'document_root:   setting.MEDIA_ROOT'}),
    url(r'^ static/(P<path>.*)$', serve, {'document_root:   setting.MEDIA_ROOT'}),
]
urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
