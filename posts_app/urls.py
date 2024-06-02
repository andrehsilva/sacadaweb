from django.urls import path
from . import views
from .views import ListPosts, PostDetailView


urlpatterns = [
    path('', ListPosts.as_view(), name='post-list'),
    path('post/<uuid:pk>/', PostDetailView.as_view(), name='post-detail'),
]