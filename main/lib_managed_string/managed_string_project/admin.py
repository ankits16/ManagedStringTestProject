from django.contrib import admin
from .models import ManagedStringProject
from .forms import ProjectAdminForm

@admin.register(ManagedStringProject)
class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm
    list_display = ('project_id', 'name', 'project_type', 'created')
    list_filter = ('project_type',)
    readonly_fields = ('project_id',)
    # readonly_fields = ('project_id', )
    # inlines = [GitHubSourceInline, FileUploadSourceInline]
    change_form_template = 'admin/managed_string_project/managed_string_project/change_form.html'

    class Media:
        js = ('js/admin/project_admin.js',)