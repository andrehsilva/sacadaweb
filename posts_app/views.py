from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.core.paginator import Paginator
from django.shortcuts import render
from posts_app.models import Post, Category
from django.urls import reverse_lazy
from django.db.models import Q


class ListPosts(ListView):
    template_name = 'post-list.html'
    model = Post
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search_query', '')

        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) |
                Q(content__icontains=search_query) |
                Q(author__username__icontains=search_query)
            )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['search_query'] = self.request.GET.get('search_query', '')
        context['posts_latest'] = Post.objects.order_by('-created')[:5]
        return context



class PostDetailView(DetailView):
    model = Post
    template_name = 'post-detail.html'
    context_object_name = 'post'