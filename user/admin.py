from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import CustomUser

admin.site.site_title = "Ecommerce Admin"
admin.site.site_header = "Ecommerce"
admin.site.index_title = "Ecommerce Admin"
admin.site.site_brand = "Ecommerce"
admin.site.welcome_sign = "Ecommerce"
admin.site.copyright = "Ecommerce"

admin.site.unregister(Group)


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    ordering = ['full_name']
    list_display = ['phone', 'full_name', 'role', 'balance']
    list_filter = ['role',]
    fieldsets = (
        (None, {'fields': ('phone',)}),
        ('Personal info', {'fields': ('full_name', 'role', 'balance')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'full_name', 'role', 'balance', 'password1', 'password2'),
        }),
    )


admin.site.register(CustomUser, CustomUserAdmin)
