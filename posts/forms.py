from django import forms

from pagedown.widgets import PagedownWidget
from taggit.models import Tag
from .models import Post


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=PagedownWidget(show_preview=False))
    image = forms.ImageField(required=False)
    content_image = forms.ImageField(required=False)
    video = forms.URLField(required=False)
    tags = forms.ModelChoiceField(widget=forms.Select,queryset=Tag.objects.all(),required=True)
    # publish = forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model = Post
        fields = [
            "title",
            "content",
            "image",
            "content_image",
            "video",
            "tags",
            # "draft",
            # "publish",
        ]


