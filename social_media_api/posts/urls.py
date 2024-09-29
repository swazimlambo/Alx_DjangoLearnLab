from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'comment', views.CommentViewSet)
router.register(r'posts', views.PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', views.PostFeedView.as_view({'get': 'list'}), name='feed'),
    path('posts/<int:pk>/like/', views.LikePostView.as_view(), name='like'),
    path('posts/<int:pk>/unlike/', views.UnlikePostView.as_view(), name='unlike')
]