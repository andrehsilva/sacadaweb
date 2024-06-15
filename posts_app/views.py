from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.core.paginator import Paginator
from django.shortcuts import render
from posts_app.models import Post, Category
from posts_app.forms import PostForm
from django.urls import reverse_lazy
from django.db.models import Q



class ListPosts(ListView):
    template_name = 'post-list.html'
    model = Post
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search_query', '')
        category_id = self.request.GET.get('category', '')

        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) |
                Q(description__icontains=search_query)
            )

        if category_id:
            queryset = queryset.filter(categories__id=category_id)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['selected_category'] = self.request.GET.get('category', '')
        context['search_query'] = self.request.GET.get('search_query', '')
        context['posts_latest'] = Post.objects.order_by('-created')[:5]
        context['no_results'] = not context['posts'].exists()
        return context


class ListPostsBack(ListView):
    template_name = 'post-list-back.html'
    model = Post
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post-detail.html'
    context_object_name = 'post'


class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_form.html'
    success_url = reverse_lazy('post-list')