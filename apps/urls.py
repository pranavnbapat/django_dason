from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from apps.routing import websocket_urlpatterns

from .views import (
    apps_chat_chat_view,
    apps_users_view,
    apps_contacts_usergrid_view,
    apps_contacts_userlist_view,
)

app_name = "apps"
urlpatterns = [
    # chat
    path("chat", view=apps_chat_chat_view, name="chat"),
    path("users", view=apps_users_view, name="users"),

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
