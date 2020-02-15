# this is my views.py
from django.shortcuts import render


def home(request):
    import json
    import requests
    api_request = requests.get(
        "http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=90025&distance=5&API_KEY=EF4AC231-32FD-47CE-A346-CCA0F4C18AFB")

    try:
        api = json.loads(api_request.content)

    except Exception as e:
        api = "Error...."

    if api[0]['Category']['Name'] == "Good" :
        category_description = "(0 - 50) Air  quality is considered  satisfactory, and air pollution poses little or " \
                               "no risk"
        category_color = "good"

    elif api[0]['Category']['Name'] == "Moderate":
        category_description = "(0 - 50) Air quality is acceptable; however, for some pollutants there may be a " \
                               "moderate health concern for a very small number of people who are unusually sensitive to air pollution."
        category_color = "moderate"

    elif api[0]['Category']['Name'] == "Unhealthy for sensitive groups":
        category_description = "(0 - 50) Air quality is acceptable; however, for some pollutants there may be a " \
                               "moderate health concern for a very small number of people who are unusually sensitive to air pollution."
        category_color = "usg"

    elif api[0]['Category']['Name'] == "Unhealthy":
        category_description = "(0 - 50) Air quality is acceptable; however, for some pollutants there may be a " \
                               "moderate health concern for a very small number of people who are unusually sensitive to air pollution."
        category_color = "unhealthy"

    elif api[0]['Category']['Name'] == "Very Unhealthy":
        category_description = "(0 - 50) Air quality is acceptable; however, for some pollutants there may be a " \
                               "moderate health concern for a very small number of people who are unusually sensitive to air pollution."
        category_color = "veryunhealthy"

    elif api[0]['Category']['Name'] == "Hazardous":
        category_description = "(0 - 50) Air quality is acceptable; however, for some pollutants there may be a " \
                               "moderate health concern for a very small number of people who are unusually sensitive to air pollution."
        category_color = "hazardous"

    return render(request, 'home.html', {'api': api,
                                         'category_description': category_description,
                                         'category_color':category_color })


def about(request):
    return render(request, "about.html", {})
