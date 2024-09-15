from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, UpdateView, DeleteView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import SignUpForm
from .models import Post
from django.forms import BaseModelForm
from django.http import HttpResponse

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
    pass

class CommentUpdateView(UpdateView):
    pass

class CommentDeleteView(DeleteView):
    pass