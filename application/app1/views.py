from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request, 'Frontend/index.html')

def About(request):
    return render(request, 'Frontend/about.html')

def Contact(request):
    return render(request, 'Frontend/contact.html')
