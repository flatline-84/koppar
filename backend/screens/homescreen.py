from kivy.uix.screenmanager import Screen
from kivy.clock import Clock

from datetime import datetime
from ..util.WeatherManager import Weather

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)

        # self.update_freq()
        # self.update_slow()
        self.weather = Weather()
        # Run the update function before the next frame
        Clock.schedule_interval(self.update_freq, 0.1)
        # updates every hour
        Clock.schedule_once(self.update_slow)
        Clock.schedule_interval(self.update_slow, 3600)


    
    # Data that needs to be updated frequently
    # like clock time
    def update_freq(self, dt):
        # print(dt)
        now = datetime.now()
        dt_string = now.strftime("%H:%M:%S")
        self.ids.home_screen_label_time.text = dt_string
    
    # Data that needs to be updated slowly
    # like the date and weather
    def update_slow(self, dt):
        now = datetime.now()
        dt_string = now.strftime("%A, %d %b %Y")
        self.ids.home_screen_label_date.text = dt_string