from django.db import models

class LabTheme(models.Model):
    name = models.CharField(unique=True, max_length=256)