from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from Blog.models import Post
# Create your views here.

def post_chosen(request, pk):
    context = {'pk': pk}
    return render(request, 'index.html', {"title": pk, "posts_menu": Post.objects.all(),
                                          "posts": Post.objects.filter(id=pk)})

def index(request):
    return render(request, 'index.html', {"title": "title2", "posts_menu": Post.objects.all(),
                                          "posts": Post.objects.all()})

