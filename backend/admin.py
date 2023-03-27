from django.contrib import admin

# Register your models here.
from .models import AdminMenuMaster

# admin.site.register(AdminMenuMaster)


@admin.register(AdminMenuMaster)
class AdminMenuMasterAdmin(admin.ModelAdmin):
    list_display = ('menu_name', 'menu_order', 'menu_icon', 'menu_route', 'status', 'deleted', 'created_at',
                    'updated_at')
