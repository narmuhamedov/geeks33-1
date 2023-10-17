from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.helloView),
    path('post/', views.postListView),
]