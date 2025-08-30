from django.db import models
import uuid

# Create your models here.
class Folder(models.Model):
    uid = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)

class Files(models.Model):
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    
    