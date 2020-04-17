from django.db import models


class Quotes(models.Model):
    text = models.TextField(default="")
    author = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
