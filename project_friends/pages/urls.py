from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('feeds', views.feeds, name='feeds'),
    path('like_post', views.like_post, name='like_post')
]
