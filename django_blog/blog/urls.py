from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .import views

urlpatterns = [
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('/posts/', views.PostListView.as_view(), name='post_list'),
    path('/posts/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/comments/new/', views.CommentCreateView.as_view(), name='create_comment'),
    path('comment/<int:pk>/update/',views.CommentUpdateView.as_view(), name='update_comment' ),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='delete_comment' ),
    path('tags/<slug:tag_slug>/', views.PostByTagListView.as_view())
    
] 
