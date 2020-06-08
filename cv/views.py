from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect

def cv_main(request):
    return render(request, 'cv_main.html')
