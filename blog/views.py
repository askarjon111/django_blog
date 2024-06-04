from django.shortcuts import render
from django.views.generic import ListView
from django_filters.views import FilterView

from blog.filters import PostFilter
from blog.models import Post


def home_view(request):
    latest_posts = Post.objects.all().order_by('-id')[:6]
    context = {'latest_posts': latest_posts}
    return render(request, 'index.html', context)


class PostListView(FilterView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
    filterset_class = PostFilter
