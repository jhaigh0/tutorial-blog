from __future__ import unicode_literals
from django.db import models

class CV_Element(models.Model):
    title = models.CharField(max_length=2000)
    start_date = models.DateField()
    end_date = models.DateField()
    text = models.TextField()
    type_id = models.CharField(max_length=200, default='place_holder')
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.title
