from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListPosts.as_view(), name='post-list'),
]