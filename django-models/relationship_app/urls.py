from .views import list_books, LibraryDetailView

views.register 
LogoutView.as_view(template_name= logout)
LoginView.as_view(template_name= login)
