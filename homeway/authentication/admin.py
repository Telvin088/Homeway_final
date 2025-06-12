from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class CustomUserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'phone', 'is_admin', 'is_staff')
    search_fields = ('username', 'email')
    readonly_fields = ('id',)

    fieldsets = (
        (None, {'fields': ('username', 'email', 'phone', 'password')}),
        ('Permissions', {'fields': ('is_admin', 'is_staff', 'is_superuser')}),
        ('Profile', {'fields': ('profile_image',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'phone', 'password1', 'password2'),
        }),
    )

    ordering = ('username',)

admin.site.register(CustomUser, CustomUserAdmin)
