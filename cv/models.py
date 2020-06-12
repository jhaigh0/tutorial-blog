from __future__ import unicode_literals
from django.db import models

class CV_Element(models.Model):
    title = models.CharField(max_length=2000)
    start_date = models.DateField()
    end_date = models.DateField()
    text = models.TextField()

    def save(delf):
        self.save()

    def __str__(self):
        return self.title
