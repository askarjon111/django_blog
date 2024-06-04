from django_filters import FilterSet

from blog.models import Post


class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {'title': ['contains'], 'tag': ['exact'], 'category': ['exact']}
