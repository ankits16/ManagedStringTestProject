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

    STRING_RESOURCE_CHOICES = (
        ('github', 'GitHub'),
        ('file_upload', 'File Upload'),
    )

    project_id = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    project_type = models.CharField(max_length=10, choices=PROJECT_TYPES)
    custom_project_type = models.CharField(max_length=100, blank=True, null=True)

    string_resource = models.CharField(max_length=12, choices=STRING_RESOURCE_CHOICES)

    def __str__(self):
        return self.name
    
  
class GithubStringResource(models.Model):
    # This field creates a unique identifier for each GitHub source
    source_id = models.UUIDField(default=uuid.uuid4, editable=False)

    # Field to store the URL of the GitHub repository
    repo_url = models.URLField(max_length=200)

    # This field establishes a one-to-one relationship with ManagedStringProject
    # Ensure that each GithubStringResource is associated with one and only one ManagedStringProject
    managed_string_project = models.ForeignKey(
        ManagedStringProject,
        on_delete=models.CASCADE,  # This means if the ManagedStringProject is deleted, this resource will also be deleted
    )
# Function to generate the upload path
def project_string_source_upload_path(instance, filename):
    # Generate the path based on project_id
    return os.path.join('project_string_sources', str(instance.project.project_id), filename)


class MultipleFileStringSource(models.Model):
    # This field creates a unique identifier for each source
    source_id = models.UUIDField(default=uuid.uuid4, editable=False)

    # This field establishes a one-to-one relationship with ManagedStringProject
    # Ensure that each MultipleFileStringSource is associated with one and only one ManagedStringProject
    managed_string_project = models.ForeignKey(
        ManagedStringProject,
        on_delete=models.CASCADE,  # This means if the ManagedStringProject is deleted, this source will also be deleted
    )

    # Method to define the upload path of each file
    def file_upload_path(instance, filename):
        # Extracting file extension
        file_extension = filename.split('.')[-1]
        # Formatting the path
        return f'{instance.managed_string_project.project_id}/{instance.source_id}/{filename}.{file_extension}'

    # File field(s)
    # You can use a FileField for each file, or use a related model if you have multiple files.
    file = models.FileField(upload_to=file_upload_path)