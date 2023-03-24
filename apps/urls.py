from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from apps.routing import websocket_urlpatterns

from .views import (
    apps_chat_chat_view,
    apps_users_view,
    apps_email_inbox_view,
    apps_email_read_view,
    apps_contacts_usergrid_view,
    apps_contacts_userlist_view,
)

app_name = "apps"
urlpatterns = [
    # chat
    path("chat", view=apps_chat_chat_view, name="chat"),
    path("users", view=apps_users_view, name="users"),

    # Email
    path("email/inbox", view=apps_email_inbox_view, name="email.inbox"),
    path("emial/read_email", view=apps_email_read_view, name="email.read"),

    # Contacts
    path(
        "contacts/user_grid", view=apps_contacts_usergrid_view, name="contacts.usergrid"
    ),
    path(
        "contacts/user_list", view=apps_contacts_userlist_view, name="contacts.userlist"
    )
]

application = ProtocolTypeRouter({
    "websocket": URLRouter(websocket_urlpatterns),
})
