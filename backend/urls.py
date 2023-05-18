from django.urls import path
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
    RecordClickView,
    ShowPaginationContactView,
    # ElasticSearchView,
    # ElasticSearchResultsView,
    ElasticSearchSingleView,
    ElasticSearchSingleResultsView,
    AutocompleteBasicView,
    MoreLikeThisView,
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
    path('pagination/record-click/<str:contact_no>', view=ShowPaginationContactView.as_view(), name='record-click'),
    path('pagination/record-click-api/', view=RecordClickView.as_view(), name='record-click-api'),


    # Large File Upload
    path("large-file-upload/", LargeFileUploadView.as_view(), name='large-file-upload'),

    # ElasticSearch
    # path("elastic-search/", view=ElasticSearchView.as_view(), name='elastic-search'),
    # path("elastic-search/search", view=ElasticSearchResultsView.as_view(), name='elastic-search-search'),

    # ElasticSearch Single Table
    path("elastic-search-single/", view=ElasticSearchSingleView.as_view(), name='elastic-search-single'),
    path("elastic-search-single/search", view=ElasticSearchSingleResultsView.as_view(),
         name='elastic-search-single-search'),

    path("autocomplete-basic/", view=AutocompleteBasicView.as_view(), name="autocomplete-basic"),

    path("morelikethis/", view=MoreLikeThisView.as_view(), name="morelikethis"),

]

handler404 = 'backend.views.handler404'
