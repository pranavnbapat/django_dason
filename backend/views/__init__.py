from .DashboardV import DashboardView
from .FormV import FormView
from .ProfileV import ProfileView
from .AllUsersV import AllUsersView
from .KnowledgeObjectsV import KOView
from .PDF2TextV import PDF2TextView
from .PDF2TextV import PDF2TextCreateAPIView
from .PaginationV import PaginationView, PaginationAPI, RecordClickView, ShowPaginationContactView
from .LargeFileUploadV import LargeFileUploadView
from .ElasticSearchV import ElasticSearchSingleView, ElasticSearchSingleResultsView
from .AutocompleteBasicV import AutocompleteBasicView
from .MoreLikeThisV import MoreLikeThisView

# ElasticSearchView, ElasticSearchResultsView,


from django.shortcuts import render
from django.template import RequestContext

def handler404(request, exception, template_name="backend/errors/404.html"):
    response = render(request, template_name)
    response.status_code = 404
    return response
