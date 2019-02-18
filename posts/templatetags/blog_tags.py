from django import template
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown

register = template.Library()

from ..models import Post
from comments.models import Comment
@register.simple_tag
def total_posts():
    return Post.objects.count()


# @register.inclusion_tag('/post_order/latest_post.html')
@register.simple_tag
def show_latest_posts(count=5):
    latest_posts = Post.objects.order_by('-timestamp')[:count]
    # return {'latest_posts': latest_posts}
    return latest_posts


@register.simple_tag
def get_most_commented_posts(count=6):

    return Post.objects.annotate(total_comments=Count('comment')).order_by('-total_comments')[:count]



@register.simple_tag
def get_tag_posts(count=10):

    return Post.objects.annotate(total_comments=Count('comment')).order_by('-total_comments')



@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))