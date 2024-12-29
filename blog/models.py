from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=240, default="Blog Post")
    content = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True, default='photos/pexels-no_photo.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.title} - {self.content[:30]}'
