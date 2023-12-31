from django.contrib import admin
from .models import GitHubSource, FileUploadSource, UploadedStringFile
from .forms import GitHubSourceAdminForm, FileUploadSourceAdminForm

class GitHubSourceInline(admin.TabularInline):
    model = GitHubSource
    form = GitHubSourceAdminForm
    extra = 1  # Number of extra forms to display
    readonly_fields = ('source_id',)

class FileUploadSourceInline(admin.TabularInline):
    model = FileUploadSource
    form = FileUploadSourceAdminForm
    extra = 0
    readonly_fields = ('source_id',)

# class UploadedFileInline(admin.TabularInline):
#     model = UploadedStringFile
#     extra = 1  # Number of empty forms to display
