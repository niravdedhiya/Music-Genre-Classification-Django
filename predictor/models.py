from django.db import models

# Create your models here.
class Document(models.Model):
    file = models.FileField(upload_to='file/')