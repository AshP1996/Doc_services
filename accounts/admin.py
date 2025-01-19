from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['id', 'username', 'email', 'user_type', 'is_active', 'is_staff']  # Display 'id' in list view
    list_filter = ['is_active', 'is_staff', 'user_type']  # Optionally add user_type to filters
    search_fields = ['id', 'email', 'username']  # Allow searching by 'id', 'email', 'username'
    ordering = ['id']  # Order by 'id' for clarity

    # Include 'id' in the fieldsets to make it visible in the form
    fieldsets = (
        (None, {'fields': ('id', 'username', 'email', 'password')}),  # 'id' displayed in fieldsets
        ('Personal info', {'fields': ('first_name', 'last_name', 'user_type')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'user_type', 'is_active', 'is_staff')
        }),
    )

    # Ensure 'id' is read-only in the form since it's auto-generated
    readonly_fields = ['id']

# Register the custom admin interface
admin.site.register(CustomUser, CustomUserAdmin)
