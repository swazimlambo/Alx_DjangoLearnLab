from django.contrib import admin
from .models import Book, CustomUser

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_filter = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')

class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    fieldsets = ('email', 'profile_photo', 'date_of_birth')

admin.site.register(Book, BookAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
