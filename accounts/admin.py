from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Дополнительная информация', {
            'fields': ('middle_name', 'photo')
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets

    list_display = (
        'username',
        'last_name',
        'first_name',
        'middle_name',
        'is_staff',
    )

    search_fields = (
        'username',
        'last_name',
        'first_name',
        'middle_name',
    )