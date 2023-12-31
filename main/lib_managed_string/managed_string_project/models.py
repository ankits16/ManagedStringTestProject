import uuid, os
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django_cryptography.fields import encrypt

class ManagedStringProject(models.Model):
    PROJECT_TYPES = (
        ('iOS', 'iOS'),
        ('Android', 'Android'),
        ('Others', 'Others'),
    )

    project_id = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    project_type = models.CharField(max_length=10, choices=PROJECT_TYPES)
    custom_project_type = models.CharField(max_length=100, blank=True, null=True)

    # Fields for the generic relation
    source_content_type = models.ForeignKey(ContentType, null=True, on_delete=models.CASCADE)
    source_object_id = models.PositiveIntegerField(null=True)
    source = GenericForeignKey('source_content_type', 'source_object_id')


    def __str__(self):
        return self.name
    

class ProjectStringSource(models.Model):
    source_id = models.UUIDField(default=uuid.uuid4, editable=False)
    project = models.ForeignKey(ManagedStringProject, on_delete=models.CASCADE)
    source_type = models.CharField(max_length=50, editable=False)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.project.name} - {self.source_type}"
    
class GitHubSource(ProjectStringSource):
    
    repository_url = models.URLField()
    ssh_key = encrypt(models.TextField(help_text="Enter the SSH key for accessing the repository."))

    def save(self, *args, **kwargs):
        self.source_type = 'GitHub'
        super().save(*args, **kwargs)

# Function to generate the upload path
def project_string_source_upload_path(instance, filename):
    # Generate the path based on project_id
    return os.path.join(
        'project_string_sources',
        str(instance.project.project_id),
        str(instance.source_id),
        filename
    )


class FileUploadSource(ProjectStringSource):
    file = models.FileField(upload_to=project_string_source_upload_path, max_length=200)

    def save(self, *args, **kwargs):
        self.source_type = 'File Upload'
        super().save(*args, **kwargs)

class UploadedStringFile(models.Model):
    # file_upload_source = models.ForeignKey(FileUploadSource, related_name='uploaded_files', on_delete=models.CASCADE)
    file = models.FileField(upload_to=project_string_source_upload_path)

    def __str__(self):
        return f"File for {self.file_upload_source.project.name}"