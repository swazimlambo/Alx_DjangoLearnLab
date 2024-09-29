from django.urls import path
from rest_framework.authtoken import views
from .views import ProfileView, RegistrationView, LoginView, TokenRetrieveView, FollowUserView, UnfollowUserView

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='registration'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_vie(), name='profile'),
    path('token/', TokenRetrieveView.as_view(), name='token'),
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow'),
]