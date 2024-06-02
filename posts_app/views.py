from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from django.shortcuts import render
from posts_app.models import Post, Category
from django.urls import reverse_lazy


class ListPosts(ListView):
    template_name = 'post-list.html'
    model = Post
    context_object_name = 'posts'
    paginate_by = 2

    def get_queryset(self):
        # Aqui você pode personalizar sua queryset conforme necessário
        return Post.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        objetos = context['posts']
        paginator = Paginator(objetos, self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        context['categories'] = Category.objects.all()
        return context
