from django import forms
from django.contrib.contenttypes.models import ContentType
from .models import ManagedStringProject

class ProjectAdminForm(forms.ModelForm):
    
    class Meta:
        model = ManagedStringProject
        fields = '__all__'
        readonly_fields = ('project_id')
        # exclude = ('source_content_type', 'source_object_id') 

    def clean(self):
        cleaned_data = super().clean()
        project_type = cleaned_data.get('project_type')
        custom_project_type = cleaned_data.get('custom_project_type')

        if project_type == 'Others' and not custom_project_type:
            self.add_error('custom_project_type', 'This field is required when project type is "Others".')

        return cleaned_data
    
   