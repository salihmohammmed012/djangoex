from django import forms
from .models import Post
class UploadResumeForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['name','email','phone_no','resume']