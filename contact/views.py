from django.shortcuts import render
from .models import Contact, Category

def index(request):
    contacts = Contact.objects.all()
    return render(request, "contact/index.html", {"contacts":contacts})
