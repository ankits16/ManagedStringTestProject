from django.contrib import admin
from .models import ManagedStringProject, FileUploadSource, GitHubSource
from .forms import ProjectAdminForm
from .admin_inlines import GitHubSourceInline, FileUploadSourceInline, StringSourceFileInline
import nested_admin
from django.core.exceptions import ValidationError

@admin.register(ManagedStringProject)
class ProjectAdmin(nested_admin.NestedModelAdmin):
    form = ProjectAdminForm
    list_display = ('project_id', 'name', 'project_type', 'created')
    list_filter = ('project_type',)
    readonly_fields = ('project_id', 'source_content_type', 'source_object_id')
    # readonly_fields = ('project_id', )
    inlines = [GitHubSourceInline, FileUploadSourceInline]
    change_form_template = 'admin/managed_string_project/managed_string_project/change_form.html'

    class Media:
        js = ('js/admin/project_admin.js',)


@admin.register(FileUploadSource)
class FileUploadSourceAdmin(admin.ModelAdmin):
    inlines = [StringSourceFileInline]
    def get_readonly_fields(self, request, obj=None):
        return ['source_id', 'source_type']

@admin.register(GitHubSource)
class GitHubSourceAdmin(admin.ModelAdmin):
    
    def get_readonly_fields(self, request, obj=None):
        return ['source_id', 'source_type']