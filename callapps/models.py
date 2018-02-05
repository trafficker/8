from django.db import models

# Create your models here.
from django.db import models

class Question(models.Model):
    context = models.CharField(max_length=200)