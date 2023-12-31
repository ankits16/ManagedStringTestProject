import uuid
from django import forms
from django.contrib.contenttypes.models import ContentType
from .models import ManagedStringProject, ProjectStringSource, GitHubSource, FileUploadSource

class ProjectAdminForm(forms.ModelForm):
    SOURCE_TYPE_CHOICES = (
        ('', '---------'),
        ('github', 'GitHub'),
        ('file_upload', 'File Upload'),
    )
    source_type = forms.ChoiceField(choices=SOURCE_TYPE_CHOICES, required=False)


    class Meta:
        model = ManagedStringProject
        fields = '__all__'
        readonly_fields = ('source_content_type', 'source_object_id',)
        # exclude = ('source_content_type', 'source_object_id') 

    def clean(self):
        cleaned_data = super().clean()
        project_type = cleaned_data.get('project_type')
        custom_project_type = cleaned_data.get('custom_project_type')

        if project_type == 'Others' and not custom_project_type:
            self.add_error('custom_project_type', 'This field is required when project type is "Others".')

        return cleaned_data
    
    # def save(self, commit=True):
    #     instance = super().save(commit=False)

    #     source_type = self.cleaned_data.get('source_type')

    #     # Logic to handle the source type
    #     if source_type == 'github':
    #         # Adjust this logic as needed
    #         github_source, created = GitHubSource.objects.get_or_create(
    #             project=instance,
    #             defaults={'repository_url': 'Default URL'}
    #         )
    #         instance.source_content_type = ContentType.objects.get_for_model(GitHubSource)
    #         instance.source_object_id = github_source.pk

    #     elif source_type == 'file_upload':
    #         # Adjust this logic as needed
    #         file_upload_source, created = FileUploadSource.objects.get_or_create(
    #             project=instance,
    #             defaults={'file': None}
    #         )
    #         instance.source_content_type = ContentType.objects.get_for_model(FileUploadSource)
    #         instance.source_object_id = file_upload_source.pk

    #     if commit:
    #         instance.save()
    #     return instance

class ProjectStringSourceAdminForm(forms.ModelForm):
    # source_id = forms.CharField(disabled=True, required=False)
    class Meta:
        model = ProjectStringSource
        fields = '__all__'
        # abstract = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.instance.pk:
            self.instance.source_id = uuid.uuid4()

class GitHubSourceAdminForm(ProjectStringSourceAdminForm):
    class Meta(ProjectStringSourceAdminForm.Meta):
        model = GitHubSource

class FileUploadSourceAdminForm(ProjectStringSourceAdminForm):
    class Meta(ProjectStringSourceAdminForm.Meta):
        model = FileUploadSource