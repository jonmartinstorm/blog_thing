from django import forms

from .models import BlogPost

# class BlogPostForm(forms.Form):
#     title = forms.CharField()
#     #slug = forms.SlugField()
#     content = forms.CharField(widget=forms.Textarea)

class BlogPostModelForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ['title', 'content']

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        qs = BlogPost.objects.filter(title__iexact=title)
        if self.instance is not None:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("This title exists, use another")
        return title
