from django.shortcuts import render
import requests


# Weather API to fetch the data for a specific location.
def weather_status(request):

    cityname = request.GET.get('cityname')

    url = "https://weatherapi-com.p.rapidapi.com/current.json"

    querystring = {"q":cityname}

    headers = {
        "X-RapidAPI-Key": "782cf90fc8mshd0cbd9a9e305402p1e4337jsna61f4f7ac8b3",
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    response_data = response.json()

    print(response.text)

    city=response_data['location']['name']
    country=response_data['location']['country']
    temperature=response_data['current']['temp_c']
    text=response_data['current']['condition']['text']
    date=response_data['location']['localtime']
    
    return render(request,'HomePage.html',{'text':text,'city':city,'country':country,'temperature':temperature,'date':date})