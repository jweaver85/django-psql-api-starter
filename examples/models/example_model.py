import uuid as uuid
from django.db import models


class ExampleModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4)
    text = models.TextField(default=None)
    char = models.CharField(default=None, max_length=4096)
    binary = models.BinaryField(default=None)
    boolean = models.BooleanField(default=False)