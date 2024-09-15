from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, UpdateView, DeleteView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import SignUpForm
from .models import Post

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
    context_object_name = 'object'

class PostDetailView(DetailView):
    model = Post 

class PostCreateView(CreateView, LoginRequiredMixin):
    pass

class PostUpdateView(UpdateView):
    pass

class PostDeleteView(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    pass
