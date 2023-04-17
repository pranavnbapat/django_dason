from django.urls import path, include
from .views import (
    FormView,
    ProfileView,
    DashboardView,
    AllUsersView,
    KOView,
    PDF2TextView,
    PDF2TextCreateAPIView,
    PaginationView,
    PaginationAPI,
    LargeFileUploadView,
    MyChunkedUploadView,
    MyChunkedUploadCompleteView
)

app_name = "backend"

urlpatterns = [
    path("my-form/", view=FormView.as_view(), name="my-form"),

    path("user/profile/", view=ProfileView.as_view(), name="user.profile"),

    # Dashboard
    path('dashboard/', view=DashboardView.as_view(), name="dashboard"),

    # Users
    path("users/", view=AllUsersView.as_view(), name="users"),
    path("users-grid/", view=AllUsersView.as_view(), name="users-grid"),

    # Knowledge Objects
    path("knowledge-objects/", view=KOView.as_view(), name="knowledge-objects"),

    # FastAPI View
    path("fastapi-view/", view=KOView.as_view(), name="fastapi-view"),

    # PDF2Text
    path("pdf2text/", view=PDF2TextView.as_view(), name="pdf2text"),
    path('api/pdf2text/', view=PDF2TextCreateAPIView.as_view(), name='pdf2text-api'),

    # Pagination
    path("pagination/", view=PaginationView.as_view(), name='pagination'),
    path("pagination-api/", view=PaginationAPI.as_view(), name='pagination-api'),

    # Large File Upload
    path("large-file-upload/", LargeFileUploadView.as_view(), name='large-file-upload'),
    path('api/chunked_upload/', MyChunkedUploadView.as_view(), name='api_chunked_upload'),
    path('api/chunked_upload_complete/', MyChunkedUploadCompleteView.as_view(), name='api_chunked_upload_complete'),
]
