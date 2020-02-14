#this is my views.py
from django.shortcuts import render


def home(request):
    import json
    import requests
    api_request=requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=90025&distance=5&API_KEY=EF4AC231-32FD-47CE-A346-CCA0F4C18AFB")

    try:
        api=json.loads(api_request.content)

    except Exception as e :
        api="Error...."

    return render(request, 'home.html', {'api':api})

def about(request):
    return render(request, "about.html", {})
