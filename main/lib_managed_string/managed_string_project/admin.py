from django.contrib import admin
from .models import ManagedStringProject, FileUploadSource
from .forms import ProjectAdminForm, FileUploadSourceAdminForm
from .admin_inlines import GitHubSourceInline, FileUploadSourceInline


@admin.register(ManagedStringProject)
class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm
    list_display = ('project_id', 'name', 'project_type', 'created')
    list_filter = ('project_type',)
    readonly_fields = ('project_id', 'source_content_type', 'source_object_id')
    # readonly_fields = ('project_id', )
    inlines = [GitHubSourceInline, FileUploadSourceInline]
    change_form_template = 'admin/managed_string_project/managed_string_project/change_form.html'

    class Media:
        js = ('js/admin/project_admin.js',)
        

# @admin.register(FileUploadSource)
# class FileUploadSourceAdmin(admin.ModelAdmin):
#     readonly_fields = ('project_id',)

@admin.register(FileUploadSource)       
class FileUploadSourceAdmin(admin.ModelAdmin):
    form = FileUploadSourceAdminForm
    # inlines = [UploadedFileInline]

# admin.site.register(FileUploadSourceAdmin,)