# app1/views.py
from django.shortcuts import render

def Home(request):
    return render(request, 'index.html')

def About(request):
    return render(request, 'About.html') # Or 'app1/About.html' if namespaced

def Contact(request):
    return render(request, 'Contact.html')