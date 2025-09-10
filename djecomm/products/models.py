from django.db import models
from utils.models import BaseModel

class Category(models.Model):
    name = models.CharField(max_length=100)
