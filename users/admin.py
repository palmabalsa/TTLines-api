from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from .models import User
# from .forms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.

# class CustomUserAdmin(UserAdmin):
#     model = User
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     search_fields = ('email', 'last_name')
#     list_filter = ('email', 'last_name', 'is_staff', 'is_active')
#     list_display = ('id', 'email', 'first_name', 'last_name', 'is_active', 'is_staff')
    
    # fieldsets: (
    #     *UserAdmin.fieldsets,
    #     (
    #         'User role',
    #         {
    #             'fields':()
    #         }
    #     )
    # )

admin.site.register(User,)
