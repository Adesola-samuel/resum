from django.db import models

class Message(models.Model):
    name=models.CharField(max_length=40)
    email=models.EmailField()
    subject=models.CharField(max_length=40)
    message = models.TextField()