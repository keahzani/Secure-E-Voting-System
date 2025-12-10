from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Profile

# Inline Profile section attached to User admin
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'
    fields = ['role', 'identification_number']

# Custom User admin
class CustomUserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
    
    # Remove 'email' from list_display and add ID number
    list_display = ('username', 'get_identification_number', 'is_staff', 'is_active')
    list_select_related = ('profile',)

    def get_identification_number(self, instance):
        return instance.profile.identification_number
    get_identification_number.short_description = 'ID Number'

    # Optional: remove email from form
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2')}
        ),
    )

# Unregister and re-register User admin
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

# Optionally register Profile separately
# admin.site.register(Profile)

