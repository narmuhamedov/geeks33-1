from django.shortcuts import render
from django.http import HttpResponse
from . import models

def postListView(request):
    post_value = models.Post.objects.all()
    return render(request, 'post/post.html', {'post_key': post_value})

# def postListView(request):
#     post_value = models.Post.objects.all()
#     html_file_name = 'post/post.html'
#     context = {
#         'post_key': post_value,
#     }
#     return render(request, html_file_name, context)







def helloView(request):
    return HttpResponse("<h1>Привет это мой первый проект на DJANGO-TEMPLATE</h1>")
