from django.contrib.auth import get_user_model
from django.views.generic import TemplateView
from django.db import connections


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


class UsersView(TemplateView):
    template_name = "apps/apps-users.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user_id = self.request.user.id
        all_users = get_user_model().objects.exclude(id=current_user_id).exclude(is_superuser=True)

        with connections['default'].cursor() as cursor:
            cursor.execute('SELECT au.first_name, au.last_name, au.username, au.email, au.last_login, au.is_staff, '
                           'ag.name as group_name, au.is_active, au.date_joined, au.id '
                           'FROM auth_user au '
                           'INNER JOIN auth_user_groups aug ON au.id = aug.user_id '
                           'INNER JOIN auth_group ag ON ag.id = aug.group_id '
                           'WHERE au.is_superuser != 1 AND au.id != ' + str(current_user_id))
            all_users = cursor.fetchall()
        context['all_users'] = all_users

        return context


# chat
apps_chat_chat_view = ChatViewGetUsers.as_view()
# users
apps_users_view = UsersView.as_view()


# Contacts
apps_contacts_usergrid_view = AppsView.as_view(
    template_name="apps/contacts/apps-contacts-grid.html"
)
apps_contacts_userlist_view = AppsView.as_view(
    template_name="apps/contacts/apps-contacts-list.html"
)
