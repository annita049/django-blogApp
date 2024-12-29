from django.shortcuts import render
from .models import Blog
from .forms import BlogForm
from django.shortcuts import get_object_or_404, redirect
# Create your views here.

def index(request):
    return render(request, 'index.html')

def All_Blogs(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'all_blogs.html', {'blogs': blogs})

def Create_Blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = request.user
            blog.save()
            return redirect('all_blogs')
        else:
            print("Form errors:", form.errors) 
            print("Form data:", form.cleaned_data)
    else:
        form = BlogForm()
    return render(request, 'blog_form.html', {'form': form})

def Edit_Blog(request, blog_id):
    blog = get_object_or_404(Blog, pk= blog_id, user = request.user)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = request.user
            blog.save()
            return redirect('all_blogs')
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blog_form.html', {'form': form})

def Delete_Blog(request, blog_id):
    blog = get_object_or_404(Blog, pk= blog_id, user=request.user)
    if request.method == 'POST':
        blog.delete()
        return redirect('all_blogs')
    return render(request, 'blog_delete', {'blog': blog})

    