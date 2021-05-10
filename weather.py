import os
def weatherCheck():
    from dotenv import load_dotenv
    import requests
    import json
    load_dotenv('.env')
    LATITUDE = os.getenv('LATITUDE')
    LONGITUDE = os.getenv('LONGITUDE')
    API_KEY = os.getenv('WEATHER_API_KEY')
    url = "http://api.openweathermap.org/data/2.5/weather?lat="+ LATITUDE + "&lon=" + LONGITUDE + "appid="+ API_KEY 
    reply = requests.get(url)
    x = reply.json()
    # store the value of "main"
    # key in variable y
    y = x["main"]
  
    # store the value corresponding
    # to the "temp" key of y
    current_temperature = y["temp"]
  
    # store the value corresponding
    # to the "pressure" key of y
    current_pressure = y["pressure"]
  
    # store the value corresponding
    # to the "humidity" key of y
    current_humidity = y["humidity"]
  
    # store the value of "weather"
    # key in variable z
    z = x["weather"]
  
    # store the value corresponding 
    # to the "description" key at 
    # the 0th index of z
    weather_description = z[0]["description"]
  
    # print following values
    print(" Temperature (in kelvin unit) = " +
                    str(current_temperature) + 
          "\n atmospheric pressure (in hPa unit) = " +
                    str(current_pressure) +
          "\n humidity (in percentage) = " +
                    str(current_humidity) +
          "\n description = " +
                    str(weather_description))

weatherCheck()
