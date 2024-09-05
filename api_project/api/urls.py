from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList

router = DefaultRouter()
router.register(r'book', BookList)

urlpatterns = [
    path('api/', include(router.urls)),
]