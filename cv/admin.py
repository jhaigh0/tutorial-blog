from __future__ import unicode_literals
from django.contrib import admin
from .models import CV_Element, Dated_Entry, Titled_Entry, Text_Entry

admin.site.register(CV_Element)
admin.site.register(Dated_Entry)
admin.site.register(Titled_Entry)
admin.site.register(Text_Entry)
