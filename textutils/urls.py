
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('text1/', views.text1, name='text1'),
    path('link1/', views.link1, name='link1'),
    # path('removepunc', views.removepunc, name='rempun'),
    path('capitalizefirst', views.capfirst, name='capfirst'),
    path('newlineremove', views.newlineremove, name='newlineremove'),
    path('spaceremove', views.spaceremove, name='spaceremove'),
    path('charcount', views.charcount, name='charcount'),
    path('analyze', views.analyze, name='analyze'),
    path('ex1', views.ex1, name='ex1'),
]
