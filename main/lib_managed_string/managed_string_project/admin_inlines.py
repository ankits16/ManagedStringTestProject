from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from .models import GitHubSource, FileUploadSource, StringSourceFile
from django.contrib.contenttypes.models import ContentType
from django.forms.models import BaseInlineFormSet
from .forms import FileUploadSourceForm
import nested_admin

class SourceInlineFormset(BaseInlineFormSet):
    def save_new(self, form, commit=True):
        instance = super().save_new(form, commit=False)
        # Set the content type and object id for the source
        content_type = ContentType.objects.get_for_model(instance)
        self.instance.source_content_type = content_type
        if commit:
            instance.save()
            self.instance.source_object_id = instance.id
            self.instance.save()
        return instance
    

class StringSourceFileInline(nested_admin.NestedTabularInline):
    model = StringSourceFile
    extra = 1  # Number of extra forms to display
   

class GitHubSourceInline(nested_admin.NestedStackedInline):
    model = GitHubSource
    extra = 1
    max_num = 1
    # fk_name = 'source repository'
    def get_readonly_fields(self, request, obj=None):
        return ['source_id', 'source_type']

class FileUploadSourceInline(nested_admin.NestedStackedInline):
    model = FileUploadSource
    # form = FileUploadSourceForm
    inlines = [StringSourceFileInline]
    extra = 1
    max_num = 1
    # fk_name = 'source files'
    def get_readonly_fields(self, request, obj=None):
        return ['source_id', 'source_type']

    # def get_formset(self, request, obj=None, **kwargs):
    #     formset = super().get_formset(request, obj, **kwargs)
    #     print(f'<<<<<< get_formset called {formset}')
    #     # formset.form = FileUploadSourceForm
    #     return formset

