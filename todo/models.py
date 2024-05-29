from django.db import models

class Todo(models.Model):
    task = models.TextField()
    description = models.TextField()
    date = models.DateField()

class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=100)