from django.urls import path
from . import views

# routes
urlpatterns = [
    path('', views.index, name='index'),
    path('myPosts/', views.myPosts, name='myPosts'),
]
