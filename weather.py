def weather(city):
    # WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
    WEATHER_API_KEY = "bb41e4817b91ff70028671598e6c4714"
    # speak("Enter the name of the city : ")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}"
    results = requests.request(method="POST", url=url)
    jsondata = results.json()
    weather_description = jsondata["weather"][0]["description"]
    temp = round(float(jsondata["main"]["temp"]) - 273, ndigits=2)
    temp_min = round(float(jsondata["main"]["temp_min"]) - 273, ndigits=2)
    temp_max = round(float(jsondata["main"]["temp_max"]) - 273, ndigits=2)
    pressure = jsondata["main"]["pressure"]
    humidity = jsondata["main"]["humidity"]
    wind_speed = jsondata["wind"]["speed"]
    cprint(f"Weather in {city} is {weather_description}", "blue")
    speak(f"{weather_description}")
    time.sleep(0.6)
    cprint("DialoGPT : Do you want to hear more about the weather?(Type 'y' or 'n')", "cyan")
    speak("Do you want to hear more about the weather?(Type 'y' or 'n')")
    ans = input(">>")
    if ans == "y":
        weather_data = f"""
        temperature {temp}  degree celsius
        maximum temperature {temp_max}  degree celsius      
        minimum temperature {temp_min}  degree celsius
        Pressure {pressure}    millibars
        Humidity {humidity}
        wind speed {wind_speed}  knots
        """
        cprint(f"{weather_data}", "blue")
        speak(weather_data)
    else:
        return