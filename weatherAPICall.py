import requests

# this is the API key that I use to access the weather API  -  https://openweathermap.org/
API_KEY = "1ba06f056aec6fbe252352ae07e9e7f4"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather" # we send the rquest to this site

which_city = input("Enter the name of the city you want to check the weather for?")  
request_send = f"{BASE_URL}?appid={API_KEY}&q={which_city}"
response_data =  requests.get(request_send)

if response_data.status_code == 200:
    data = response_data.json() # this is the response i get from the weather site in the form of a json object
    name = data['name'] # in order to get specific information we access it through the data json object nad in the brackets we say the name of the variable we want
    temperature = round(data["main"]["temp"] -273.15,2)# we get the temperature in that city, we substract 273.15 to make it in celcius
    description = data['weather'][0]["description"]
    print("The name of the city is " + name)
    print("The temperature there right now is {}".format(float(temperature)) + " celsius")
    print("The current weather state is " + description)
else:
    print ("An error occured")