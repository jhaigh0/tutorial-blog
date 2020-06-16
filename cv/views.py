from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from .models import CV_Element

def cv_main(request):
    intro = CV_Element.objects.filter(title__contains='intro').first()
    education = CV_Element.objects.filter(title__contains='education')
    skills = CV_Element.objects.filter(title__contains='skill')
    interests = CV_Element.objects.filter(title__contains='interest')
    refferances = CV_Element.objects.filter(title__contains='refferance')
    return render(request, 'cv_main.html', {'intro': intro, 'education': education, 'skills': skills, 'interests': interests, 'refferances': refferances})
