from django.views.generic.base import ContextMixin
from .context_processors import get_admin_menu


class AdminMenuMixin(ContextMixin):
    def get_admin_menu(self):
        context = get_admin_menu()
        return context

    def get_context_data(self, **kwargs):
        if hasattr(super(), 'get_context_data'):
            context = super().get_context_data(**kwargs)
        else:
            context = kwargs
        context.update(self.get_admin_menu())
        return context