from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserProfile(admin.ModelAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'is_staff')


admin.site.register(CustomUser, CustomUserProfile)