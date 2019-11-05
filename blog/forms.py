from django import forms
from pagedown.widgets import AdminPagedownWidget
from pagedown.widgets import PagedownWidget

from .models import BlogPost

class BlogPostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=AdminPagedownWidget())

    class Meta:
        model = BlogPost
        fields = "__all__"

class BlogPostModelForm(forms.ModelForm):
    publish_date = forms.DateField(widget=forms.SelectDateWidget)
    content = forms.CharField(widget=PagedownWidget())

    class Meta:
        model = BlogPost
        fields = ['title', 'image', 'content', 'publish_date']

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        qs = BlogPost.objects.filter(title__iexact=title)
        if self.instance is not None:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("This title exists, use another")
        return title
