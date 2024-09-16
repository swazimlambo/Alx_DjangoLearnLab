from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, UpdateView, DeleteView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import SignUpForm
from .models import Post, Comment
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.db.models import Q
from django.urls import reverse_lazy


# Create your views here.

def register (request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog/login/')
    else:
        form = SignUpForm()

    return render(request, 'blog/register.html', {'form':form})

@login_required        
def profile(request):
    if request.method == 'POST':
        user = request.user
        user.email = request.POST['email']
        user.save()
    return render(request, 'blog/profile.html')    

class PostListView(ListView):
    model = Post 
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post 
    template_name = 'blog/post_detail.html'

class PostCreateView(CreateView, LoginRequiredMixin):
    model = Post
    template_name = 'blog/post_create.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'blog/post_update.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostDeleteView(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('post_list')


class CommentCreateView(CreateView):
    model = Comment
    template_name = 'blog/create_comment.html'
    fields = '__all__'


class CommentUpdateView(UpdateView):
    model = Comment
    template_name = 'blog/update_comment.html'


class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'blog/delete_comment.html'

def search_post(request):
    query = request.GET.get('q')
    posts = Post.objects.filter(
        Q(title__icontains=query) /
        Q(content__icontains=query) / 
        Q(tags__name__icontains=query)
    ).distinct()
    return render(request, 'search_results.html')

class PostByTagListView(ListView):
    model = Post 
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'