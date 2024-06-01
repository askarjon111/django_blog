from django.shortcuts import render

from blog.models import Post


def home_view(request):
    latest_posts = Post.objects.all().order_by('-id')[:6]
    context = {'latest_posts': latest_posts}
    return render(request, 'index.html', context)
