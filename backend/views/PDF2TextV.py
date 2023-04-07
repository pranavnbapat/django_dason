from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import AdminMenuMixin, PermissionRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin
from .data_processing import file_async_upload
from django.conf import settings
from ..models import PDF2Text
from django.http import JsonResponse
import PyPDF2


class PDF2TextView(PermissionRequiredMixin, UserPassesTestMixin, TemplateView, LoginRequiredMixin, AdminMenuMixin):
    template_name = "backend/pdf2text/pdf2text.html"
    permission_required = 'backend.view_pdf2text'

    def post(self, request):
        result = file_async_upload(request, settings.PDF2TEXT_PATH, "application/pdf")

        if result["status"] == "success":
            pdf_reader = PyPDF2.PdfFileReader(request.FILES['file'])
            extracted_text = ""
            for page_number in range(pdf_reader.numPages):
                page = pdf_reader.getPage(page_number)
                extracted_text += page.extractText()

            file_entry = PDF2Text(
                old_filename=result["old_filename"],
                new_filename=result["new_filename"],
                application_type="application/pdf",
                file_text=extracted_text
            )

            file_entry.save()

            return JsonResponse({"status": "success", "message": "File uploaded successfully"})

        return JsonResponse(result)
