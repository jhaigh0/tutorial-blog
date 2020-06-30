from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from .models import CV_Element, Dated_Entry, Titled_Entry, Text_Entry
from .forms import Dated_Form, Titled_Form, Text_Form

def cv_main(request):
    intro = Text_Entry.objects.filter(type_id__contains='intro').first()
    education = Dated_Entry.objects.filter(type_id__contains='education')
    skills = Titled_Entry.objects.filter(type_id__contains='skill')
    employment = Dated_Entry.objects.filter(type_id__contains='employment')
    interests = Titled_Entry.objects.filter(type_id__contains='interest')
    refferances = Text_Entry.objects.filter(type_id__contains='refferance')
    return render(request, 'cv_main.html', {'intro': intro, 'education': education, 'skills': skills, 'employment': employment, 'interests': interests, 'refferances': refferances})

def new_dated(request):
    if request.method == "POST":
        entry = Dated_Form(request.POST)
        if entry.is_valid():
            entry.save()
            return redirect('cv_main')
    else:
        entry = Dated_Form()
    return render(request, 'entry_edit.html', {'entry': entry})

def new_titled(request):
    if request.method == "POST":
        entry = Titled_Form(request.POST)
        if entry.is_valid():
            entry.save()
            return redirect('cv_main')
    else:
        entry = Titled_Form()
    return render(request, 'entry_edit.html', {'entry': entry})

def new_text(request):
    if request.method == "POST":
        entry = Text_Form(request.POST)
        if entry.is_valid():
            entry.save()
            return redirect('cv_main')
    else:
        entry = Text_Form()
    return render(request, 'entry_edit.html', {'entry': entry})

def edit_dated(request, pk):
    dated = get_object_or_404(Dated_Entry, pk=pk)
    if request.method == "POST":
        entry = Dated_Form(request.POST, instance=dated)
        if entry.is_valid():
            entry.save()
            return redirect('cv_main')
    else:
        entry = Dated_Form(instance=dated)
    return render(request, 'entry_edit.html', {'entry': entry})

def edit_titled(request, pk):
    titled = get_object_or_404(Titled_Entry, pk=pk)
    if request.method == "POST":
        entry = Titled_Form(request.POST, instance=titled)
        if entry.is_valid():
            entry.save()
            return redirect('cv_main')
    else:
        entry = Titled_Form(instance=titled)
    return render(request, 'entry_edit.html', {'entry': entry})

def edit_text(request, pk):
    text = get_object_or_404(Text_Entry, pk=pk)
    if request.method == "POST":
        entry = Text_Form(request.POST, instance=text)
        if entry.is_valid():
            entry.save()
            return redirect('cv_main')
    else:
        entry = Text_Form(instance=text)
    return render(request, 'entry_edit.html', {'entry': entry})
