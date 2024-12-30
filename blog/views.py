from django.shortcuts import render
from .models import Blog
from .forms import BlogForm, UserRegistrationForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
# Create your views here.

def index(request):
    return render(request, 'index.html')

def All_Blogs(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'all_blogs.html', {'blogs': blogs})

@login_required
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

@login_required
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

@login_required
def Delete_Blog(request, blog_id):
    blog = get_object_or_404(Blog, pk= blog_id, user=request.user)
    if request.method == 'POST':
        blog.delete()
        return redirect('all_blogs')
    return render(request, 'delete_blog.html', {'blog': blog})


def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog_detail.html', {'blog': blog})


def Register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('all_blogs')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


def my_blogs(request):
    if request.user.is_authenticated:
        blogs = Blog.objects.filter(user=request.user)
        return render(request, 'my_blogs.html', {'blogs': blogs})
    else:
        return redirect('login')


    