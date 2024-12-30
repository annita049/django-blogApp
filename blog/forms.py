from django import forms
from .models import Blog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'photo']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your content here'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        
    def clean_photo(self):
    # If no photo is uploaded -> we return default image of no photo
        photo = self.cleaned_data.get('photo')
        if not photo:
            return None  # empty photo field
        return photo

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email',
        })
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password',
        })
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm your password',
        })
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your username',
            }),
        }