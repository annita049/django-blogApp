from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['text', 'photo']
    def clean_photo(self):
    # If no photo is uploaded -> we return default image of no photo
        photo = self.cleaned_data.get('photo')
        if not photo:
            return None  # empty photo field
        return photo
