from django.shortcuts import render
import requests


def home(request):
    response = requests.get(
        "https://www.thecocktaildb.com/api/json/v1/1/random.php").json()
    cocktail = response['drinks'][0]['strDrink']
    return render(request, "home.html", {"cocktail": cocktail})
