from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet
from rest_framework.authtoken import views

router = DefaultRouter()
#router.register(r'book', BookList)
router.register(r'book', BookViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token)
]
