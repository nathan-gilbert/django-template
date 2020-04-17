from django.db import models


class Quotes(models.Model):
    id = models.IntegerField
    text = models.TextField
    author = models.TextField
