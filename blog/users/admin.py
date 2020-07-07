from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_superuser', 'date_joined']
    list_filter = ['is_superuser']
    search_fields = ['username', 'email']
    fields = ['username', 'email', 'password', 'profile_picture', 'is_staff', 'is_superuser']

admin.site.register(User, UserAdmin)