# models.py
from django.db import models

class Webhook(models.Model):
    url = models.URLField()

    def __str__(self):
        return f"Webhook {self.id}"
