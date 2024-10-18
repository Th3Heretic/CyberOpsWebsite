from django.shortcuts import render


def home(request):
    return render(request, 'Landing.html')  # Renders the Landing.html template
