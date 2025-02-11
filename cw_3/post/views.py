from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django import forms
from .models import Thread, Post

class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['title', 'description']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields =['title', 'description', 'author', 'thread']

def home(request):
    return redirect('/threads')

def thread_list(request):
    threads = Thread.objects.all()
    return render(request, 'post/thread_list.html', {'threads': threads})

def thread_detail(request, id):
    thread = get_object_or_404(thread, id=id)
    posts = Post.objects.filter(thread=thread)
    return render(request, 'post/thread_detail.html', {'thread': thread, 'posts': posts})

@csrf_exempt
def create_thread(request):
    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/threads/')
        return JsonResponse({"error": "Invalid request"}, status=400)
    
@csrf_exempt
def delete_thread(request, id):
    thread = get_object_or_404(Thread, id=id)
    thread.delete()
    return redirect('/threads/')

@csrf_exempt
def edit_thread(request, id):
    thread = get_object_or_404(thread, id=id)
    if request.method == 'POST':
        form = ThreadForm(request.POST, instance=thread)
        if form.is_valid():
            form.save()
            return redirect(f'/threads/{id}')
    return render(request, 'post/thread_edit.html', {'thread': thread})

@csrf_exempt
def create_post(request, id):
    thread = get_object_or_404(thread, id=id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit= False)
            post.thread = thread
            post.save()
            return redirect(f'/threads/{id}')
        return JsonResponse({'error': "Invalid request"}, status=400)


@csrf_exempt
def delete_post(reguest, id):
    post = get_object_or_404(Post, id=id)
    thread_id = post.thread.id
    post.delete()
    return redirect(f'/threads/{thread_id}')

