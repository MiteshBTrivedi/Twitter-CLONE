from operator import is_
from urllib import request
from django.shortcuts import render
from django.http import  HttpResponseRedirect
from .models import Post
from .forms import Postform

# Create your views here.
# def index(request):
#     if request.method == 'POST':
#         form = Postform(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/')
#         else:
#             return HttpResponseRedirect(form.errors.as_json( ))        
#     posts = Post.objects.all()[:20]
#     return render (request,'posts.html', {'cars':posts})
                     

def index1(request):
    if request.method == 'POST':
        form = Postform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.errors.as_json())
    posts = Post.objects.all()[:20]
    return render(request, 'posts.html', {'posts':posts})

def delete(request, post_id):
    newpost = Post.objects.get(id = post_id)
    newpost.delete()
    return HttpResponseRedirect('/')

def edit(request,post_id):
    posts = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = Postform(request.POST, request.FILES, instance=posts)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect("not valid")
    
    return render(request, 'edit.html', {'post':posts})
def like(request, post_id):
    # Find Post
    post = Post.objects.get(id=post_id)
    newlikecount = post.like_count+1
    post.like_count = int(newlikecount)
    post.save()
    return HttpResponseRedirect('/')
