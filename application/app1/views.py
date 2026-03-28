# app1/views.py
from django.shortcuts import render
from .models import Student

def Home(request):
    students = Student.objects.all()
    return render(request, 'index.html', {'students': students})

def About(request):
    return render(request, 'About.html') # Or 'app1/About.html' if namespaced

def Contact(request):
    return render(request, 'Contact.html')