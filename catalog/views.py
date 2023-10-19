from django.shortcuts import render


def start_homepage(request):
    return render(request, 'catalog/homepage.html')


def start_contacts(request):
    return render(request, 'catalog/contacts.html')