from django.urls import path
from . import views
from .views import ListPosts, PostDetailView, CreatePostView, ListPostsBack, PostUpdateView, PostDeleteView


urlpatterns = [
    path('', ListPosts.as_view(), name='home'),
    path('post/<uuid:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', CreatePostView.as_view(), name='post-create'),
    path('posts/', ListPostsBack.as_view(), name='post-list'),
    path('post/edit/<uuid:pk>/', PostUpdateView.as_view(), name='post-edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
