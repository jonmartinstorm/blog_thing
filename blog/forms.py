from django import forms

from .models import BlogPost

class BlogPostForm(forms.Form):
    title = forms.CharField()
    #slug = forms.SlugField()
    content = forms.CharField(widget=forms.Textarea)

class BlogPostModelForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ['title', 'content']


# class ContactForm(forms.Form):
#     full_name = forms.CharField()
#     email = forms.EmailField()
#     content = forms.CharField(widget=forms.Textarea)
