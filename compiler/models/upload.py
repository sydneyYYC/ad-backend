from django.db import models
from django.db.models import Index, QuerySet


class UploadFile(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        indexes = [
            Index(fields=['name'])
        ]

def init(*args, **kwargs):
    my_file: QuerySet = UploadFile.objects.filter(name='my file')
    if my_file.exists():
        print('found my upload file')
    else:
        print('CANNOT find upload')
        # created: UploadFile = UploadFile.objects.create(name='my file')