from django.db import models

class Komplekt(models.Model):
    name = models.CharField(max_length=140, blank=False, default='')
    year = models.CharField(max_length=200, blank=False, default='')
    description = models.TextField(max_length=2000,blank=False, default='')
    published = models.BooleanField(default=False)