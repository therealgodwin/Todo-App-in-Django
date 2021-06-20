from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Todo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)


class Task(models.Model):
    task = models.CharField(max_length=30)
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE, null=True)
