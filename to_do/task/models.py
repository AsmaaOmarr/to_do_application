from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=30,validators=[MinLengthValidator(2)])
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
