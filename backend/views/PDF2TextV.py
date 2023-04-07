from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import AdminMenuMixin, PermissionRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin
from .data_processing import file_async_upload
from django.conf import settings
from backend.models import PDF2Text
from django.http import JsonResponse
from pdf2image import convert_from_path
import pytesseract
import pdfplumber
import os
from rest_framework import generics, permissions
from backend.serializers import PDF2TextSerializer
from rest_framework import status
from rest_framework.response import Response


def process_pdf_file(request):
    result = file_async_upload(request, settings.PDF2TEXT_PATH, "application/pdf")

    if result["status"] == "success":
        try:
            extracted_text = ""
            with pdfplumber.open(request.FILES['file']) as pdf:
                # Check if the first page contains text
                page = pdf.pages[0]
                if not page.extract_text():
                    # If not, use OCR to extract text from the image-based PDF
                    images = convert_from_path(request.FILES['file'].temporary_file_path())
                    for image in images:
                        extracted_text += pytesseract.image_to_string(image)
                else:
                    # Extract text from plain text PDF
                    for page in pdf.pages:
                        extracted_text += page.extract_text()

            file_entry = PDF2Text(
                old_filename=result["old_filename"],
                new_filename=result["new_filename"],
                application_type="application/pdf",
                file_text=extracted_text
            )

            file_entry.save()
            return file_entry, None

        except Exception as e:
            # If there's an error while saving the record to the database, delete the file from the folder
            file_path = os.path.join(settings.PDF2TEXT_PATH, result["new_filename"])
            if os.path.isfile(file_path):
                os.remove(file_path)
            return None, "There's an error in extracting text from the file"

    return None, result["message"]


class PDF2TextView(PermissionRequiredMixin, UserPassesTestMixin, TemplateView, LoginRequiredMixin, AdminMenuMixin):
    template_name = "backend/pdf2text/pdf2text.html"
    permission_required = 'backend.view_pdf2text'

    def post(self, request):
        file_entry, error_message = process_pdf_file(request)

        if file_entry:
            return JsonResponse({"status": "success", "message": "File uploaded successfully"})
        else:
            return JsonResponse({"status": "error", "message": error_message})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pdf_files = PDF2Text.objects.all()
        context['pdf_files'] = pdf_files
        return context


class PDF2TextCreateAPIView(generics.CreateAPIView):
    queryset = PDF2Text.objects.all()
    serializer_class = PDF2TextSerializer
    permission_classes = [permissions.IsAuthenticated]  # Require authentication

    def create(self, request, *args, **kwargs):
        file_entry, error_message = process_pdf_file(request)

        if file_entry:
            serializer = self.get_serializer(file_entry)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "error", "message": error_message}, status=status.HTTP_400_BAD_REQUEST)

