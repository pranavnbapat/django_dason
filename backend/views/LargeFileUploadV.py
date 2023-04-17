from .mixins import AdminMenuMixin, PermissionRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class LargeFileUploadView(PermissionRequiredMixin, LoginRequiredMixin, TemplateView, AdminMenuMixin):
    template_name = "backend/large-file-upload/large-file-upload.html"
    permission_required = 'backend.view_largefileupload'
