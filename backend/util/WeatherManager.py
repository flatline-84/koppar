import config

class Weather():

    def __init__(self):
        if (config.key_openweather == None):
            print("No open weather key!")
            return
        if (config.city == None):
            print("No city defined!")
            return
        self.ep_current_forecast = "api.openweathermap.org/data/2.5/weather?id={0}&appid={1}&units=metric"
    
        print(self.ep_current_forecast.format(config.city, config.key_openweather))
        print(config.key_openweather)
