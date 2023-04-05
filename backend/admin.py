from django.contrib import admin

# Register your models here.
from .models import AdminMenuMaster
from .models import MyForm

# admin.site.register(AdminMenuMaster)


@admin.register(AdminMenuMaster)
class AdminMenuMasterAdmin(admin.ModelAdmin):
    list_display = ('menu_name', 'menu_order', 'menu_icon', 'menu_route', 'status', 'deleted', 'created_at',
                    'updated_at')


@admin.register(MyForm)
class MyFormAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'email', 'dob', 'status', 'deleted', 'created_at',
                    'updated_at')
