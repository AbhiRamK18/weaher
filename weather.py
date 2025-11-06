import requests

api_key="41c66ddd9c5ec0f3edb3ba19ce1d985f" #default apikey from "https://openweathermap.org" after singin
user_input=input("Enter a city : ")
weather_data=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

#print(weather_data.json()) 
if weather_data.json()['cod'] == '505':  #505 is not an imaginary cod value (for case=not found cod)
    print("city not found")
else:
   weather =weather_data.json()['weather'][0]['main']
   temp=round(weather_data.json()['main']['temp'])
   print(f"The weather in {user_input} is: {weather}")
   print(f"The temperature in {user_input} is: {temp}°F") #to get degree symbol use"Alt+0176"
