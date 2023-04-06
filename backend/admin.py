from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import AdminMenuMaster, MyForm, KnowledgeObjects, DefaultAuthUserExtend

# Unregister the old User model from the admin site
# admin.site.unregister(User)

# Register the new DefaultAuthUserExtend model with the admin site
admin.site.register(DefaultAuthUserExtend, UserAdmin)


@admin.register(AdminMenuMaster)
class AdminMenuMasterAdmin(admin.ModelAdmin):
    list_display = ('menu_name', 'menu_order', 'menu_icon', 'menu_route', 'status', 'deleted', 'created_at',
                    'updated_at')


@admin.register(MyForm)
class MyFormAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'email', 'dob', 'status', 'deleted', 'created_at', 'updated_at')


@admin.register(KnowledgeObjects)
class KnowledgeObjectsAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'deleted', 'created_at', 'updated_at')

