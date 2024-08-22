from .views import list_books, LibraryDetailView
from . import views


#views.register 
#LogoutView.as_view(template_name= logout)
#LoginView.as_view(template_name= login)#

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

urlpatterns = [
    path('login/', LoginView.as_view(template_name='relationship_app//login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/', views.edit_book, name='edit_book'),
    path('delete_book', views.delete_book, name='delete_book')
]
