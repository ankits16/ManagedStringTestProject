from django.contrib.contenttypes.admin import GenericTabularInline
from .models import GitHubSource, FileUploadSource

class GitHubSourceInline(GenericTabularInline):
    model = GitHubSource
    extra = 1  # Number of extra forms to display

class FileUploadSourceInline(GenericTabularInline):
    model = FileUploadSource
    extra = 1
