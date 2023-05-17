from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import AdminMenuMaster, MyForm, KnowledgeObjects, DefaultAuthUserExtend, PDF2Text, FakerModel, \
    CustomPermissions, GroupCustomPermissions, PermissionMaster

# Unregister the old User model from the admin site
# admin.site.unregister(User)

# Register the new DefaultAuthUserExtend model with the admin site
admin.site.register(DefaultAuthUserExtend, UserAdmin)


@admin.register(AdminMenuMaster)
class AdminMenuMasterAdmin(admin.ModelAdmin):
    list_display = ('menu_name', 'menu_order', 'menu_icon', 'menu_route', 'menu_access', 'status', 'deleted',
                    'created_at', 'updated_at')


@admin.register(MyForm)
class MyFormAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'email', 'dob', 'status', 'deleted', 'created_at', 'updated_at')


@admin.register(KnowledgeObjects)
class KnowledgeObjectsAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'deleted', 'created_at', 'updated_at')


@admin.register(PDF2Text)
class PDF2TextAdmin(admin.ModelAdmin):
    list_display = ('old_filename', 'new_filename', 'status', 'created_at', 'updated_at')


@admin.register(FakerModel)
class FakerModelAdmin(admin.ModelAdmin):
    list_display = ('keywords', 'description', 'status', 'created_at', 'updated_at')


@admin.register(CustomPermissions)
class CustomPermissionsAdmin(admin.ModelAdmin):
    list_display = ('user', 'permission_name', 'status', 'created_at', 'updated_at')


@admin.register(GroupCustomPermissions)
class GroupCustomPermissionsAdmin(admin.ModelAdmin):
    list_display = ('group', 'get_permission_names', 'status', 'created_at', 'updated_at')
    filter_horizontal = ('permission_names',)

    def get_permission_names(self, obj):
        return ", ".join([p.__str__() for p in obj.permission_names.all()])
    get_permission_names.short_description = 'Permission Names'


@admin.register(PermissionMaster)
class PermissionMasterAdmin(admin.ModelAdmin):
    list_display = ('menu', 'action', 'status', 'created_at', 'updated_at')
