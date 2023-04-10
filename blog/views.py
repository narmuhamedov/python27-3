from django.http import HttpResponse
from django.shortcuts import render
from . import models

def helloview(request):
    return HttpResponse('Hello World')


def blogview(request):
    post = models.Post.objects.all()
    context = {
        'post_object': post
    }
    return render(request, 'post.html', context)