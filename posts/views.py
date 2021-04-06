from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import PostModel
from django.shortcuts import render
from .forms import PostCreateForm,PostUpdateForm

# Create your views here.
class PostList(ListView):
    template_name = 'post/post_list.html'
    model = PostModel


class PostCreate(CreateView):
    template_name = 'post/post_create.html'
    model = PostModel
    success_url = reverse_lazy('posts:_post')
    form_class = PostCreateForm
    context_object_name = 'post_create'



class PostUpdateView(UpdateView):
    model=PostModel
    template_name = 'post/post_update.html'
    form_class =PostUpdateForm
    success_url = reverse_lazy('posts:_post')



class PostDeleteView(DeleteView):
    model=PostModel
    template_name = 'post/post_delete.html'
    success_url = reverse_lazy('posts:_post')

