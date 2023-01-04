from django.shortcuts import render, redirect
from . models import Post
from . forms import MakePost
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


def index(request):
    post=Post.objects.all()
    return render(request,'index.html',{'post':post})
def post(request,id):
    post=Post.objects.get(id=id)
    return render(request, 'post.html',{'post':post})
@login_required
def create(request):
    form = MakePost()
    if request.method == 'POST':
        form=MakePost(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'create.html',{'form':form})
@login_required
def edit(request, id):
    post=Post.objects.get(id=id)
    form=MakePost(instance=post)
    if request.method == 'POST':
        form = MakePost(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'edit.html',{'form':form})
@login_required
def delete(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('index')
    return render(request, 'edit.html')
def about(request):
    post=Post.objects.all()
    return render(request,'about.html',{'post':post})
def contact(request):
    post=Post.objects.all()
    return render(request,'contact.html',{'post':post})
def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request,'signup.html',{'form':form})