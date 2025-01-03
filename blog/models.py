from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=240, default="")
    content = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='photos/',
        blank=True,
        null=True,
        default='photos/pexels-no_photo.jpg'
    )
    read_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} - {self.content[:30]} - {self.user.username}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    photo = models.ImageField(
        upload_to='photos/',
        default='photos/no-profile-photo.png',
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{self.user.username} Profile'

