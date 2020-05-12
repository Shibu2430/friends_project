from django.urls import path

from . import views

urlpatterns = [
    path('addpost', views.addpost, name='addpost'), 
]