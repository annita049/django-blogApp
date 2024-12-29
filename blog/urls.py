from django.urls import path
from . import views

urlpatterns = [
    path('', views.All_Blogs, name='all_blogs'),
    path('create/', views.Create_Blog, name='Create_Blog'),
    path('<int:blog_id>/edit/', views.Edit_Blog, name='edit_blog'),
    path('<int:blog_id>/delete/', views.Delete_Blog, name='delete_blog'),
    path('<int:blog_id>/detail/', views.blog_detail, name='blog_detail'),
    path('register/', views.Register, name='register'),
]