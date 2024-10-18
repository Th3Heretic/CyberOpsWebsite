from django.shortcuts import render


def home(request):
    return render(request, 'landing.html')  # Renders the landing.html template
