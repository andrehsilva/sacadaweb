from django.urls import path
from . import views
from .views import ListPosts, PostDetailView, CreatePostView, ListPostsBack


urlpatterns = [
    path('', ListPosts.as_view(), name='post-list'),
    path('list/', ListPostsBack.as_view(), name='post-list-back'),
    path('post/<uuid:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', CreatePostView.as_view(), name='post-create'),
]