from .mixins import AdminMenuMixin, PermissionRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from backend.models import LargeFileUpload
from chunked_upload.views import ChunkedUploadView, ChunkedUploadCompleteView
from django.conf import settings
import os
import datetime
from django.http import JsonResponse, HttpResponseBadRequest
import re
from django.core.files.uploadedfile import SimpleUploadedFile


class LargeFileUploadView(PermissionRequiredMixin, LoginRequiredMixin, TemplateView, AdminMenuMixin):
    template_name = "backend/large-file-upload/large-file-upload.html"
    permission_required = 'backend.view_largefileupload'


class MyChunkedUploadView(PermissionRequiredMixin, LoginRequiredMixin, ChunkedUploadView):
    model = LargeFileUpload
    field_name = 'large_file'

    def post(self, request, *args, **kwargs):
        # Create a SimpleUploadedFile instance from the received binary data
        file_data = request.body
        content_range = request.META.get('HTTP_CONTENT_RANGE')
        filename = request.META.get('HTTP_CONTENT_DISPOSITION')
        content_type = request.META.get('HTTP_CONTENT_TYPE')

        if content_range and filename and content_type:
            start, end, size = map(int, re.findall(r'\d+', content_range))
            filename = re.findall(r'filename="(.+)"', filename)[0]

            uploaded_file = SimpleUploadedFile(filename, file_data, content_type)
            request.FILES[self.field_name] = uploaded_file
        else:
            return JsonResponse({"status": "error", "message": "Invalid request headers"})

        return super().post(request, *args, **kwargs)


class MyChunkedUploadCompleteView(PermissionRequiredMixin, LoginRequiredMixin, ChunkedUploadCompleteView):
    model = LargeFileUpload

    def on_completion(self, uploaded_file, request):
        # Generate a new filename with a timestamp
        old_filename = uploaded_file.name
        filename, ext = os.path.splitext(old_filename)
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
        new_filename = f"{timestamp}{ext}"

        # Save the uploaded file to the specified directory with the new filename
        file_path = os.path.join(settings.FILE_UPLOAD_DIR, new_filename)

        with open(file_path, 'wb') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)

        # Create a new instance of your model and save it
        large_file = LargeFileUpload(
            old_filename=old_filename,
            new_filename=new_filename,
            application_type=uploaded_file.content_type,
        )
        large_file.save()

        print(f"File uploaded: {uploaded_file.file.name}")

    def get_response_data(self, chunked_upload, request):
        # Customize the response data sent back to the client
        return {"message": "File uploaded successfully"}

    def post(self, request, *args, **kwargs):
        # Add this block to debug the received data in the request object
        print(f"Request.POST: {request.POST}")
        print(f"Request.FILES: {request.FILES}")

        return super().post(request, *args, **kwargs)

