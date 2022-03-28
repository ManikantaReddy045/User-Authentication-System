from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class UserAdminConfig(UserAdmin):
    search_fields = ('email',)
    ordering = ('id',)
    list_filter = ('is_active','is_staff',)
    filter_horizontal = ()
    list_display = ('id', 'firstname', 'lastname', 'email', 'dob', 'Age', 'is_active', 'is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        ('Personal info', {'fields': ('firstname', 'lastname', 'dob','phone_numbers')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','email', 'password1', 'password2',)}),
            ('Personal info', {'fields': ('firstname', 'lastname', 'dob','phone_numbers')}),
            ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
    )

admin.site.register(CustomUser, UserAdminConfig)