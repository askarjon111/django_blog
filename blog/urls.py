from django.urls import path

from blog.views import PostListView, home_view


urlpatterns = [
    path('', home_view, name='home'),
    path('posts/', PostListView.as_view(), name='posts'),
]

