from django.contrib import admin
from .models import Shelf, ShelfBook
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Extra Info", {"fields": ("date_of_birth", "profile_photo")}),
    )

admin.site.register(Shelf)
admin.site.register(ShelfBook)

# Register your models here.
