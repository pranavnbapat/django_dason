from django.contrib.auth import get_user_model
from django.views.generic import TemplateView


# Create your views here.
# class AppsView(LoginRequiredMixin, TemplateView):
class AppsView(TemplateView):
    pass


class ChatViewGetUsers(TemplateView):
    template_name = "apps/apps-chat.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user_id = self.request.user.id
        # users =
        users = get_user_model().objects.exclude(id=current_user_id)
        context["users"] = users
        return context


# chat
apps_chat_chat_view = ChatViewGetUsers.as_view()

# Contacts
apps_contacts_usergrid_view = AppsView.as_view(
    template_name="apps/contacts/apps-contacts-grid.html"
)
apps_contacts_userlist_view = AppsView.as_view(
    template_name="apps/contacts/apps-contacts-list.html"
)
