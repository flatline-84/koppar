#!/usr/bin/python3
import kivy
kivy.require('1.11.1')

import platform
import sys

from kivy.app import App
from kivy.config import Config, ConfigParser
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
# from kivy.core.text import FontContextManager as FCM
from kivy.uix.label import Label
from kivy.core.text import LabelBase

# Import the desired screens
from backend.screens.homescreen import HomeScreen
from backend.screens.newsscreen import NewsScreen
from backend.screens.spotifyscreen import SpotifyScreen
from backend.screens.dealsscreen import DealsScreen
from backend.screens.settingsscreen import SettingsScreen

from backend.debug.touchtracer import TouchTracer

# Config.set('graphics', 'resizable', True) 
# Config.set('input', 'hidinput', 'invert_y=1')
# config = ConfigParser()
Config.read('koppar.ini')
# Config.set('input', 'mouse', 'disable_on_activity')
Config.set('input', '%(name)s', 'probesysfs,provider=hidinput,param=invert_y=0')
# Config.set('koppar', 'colour_home', )
Config.write()
# Config.read('koppar.ini')
# Config.write()
# Config.write()
# causing all the freaking issues with the touchscreen
# made a phantom press mirrored exactly across from the mouse input
# no idea why
# [input]
#     mouse = mouse,disable_on_activity

# Register a new font to be used in the application
LabelBase.register(name="MainFont", fn_regular="res/fonts/RobotoCondensed-Regular.ttf")
LabelBase.register(name="BitFont", fn_regular="res/fonts/PressStart2P-Regular.ttf")

# Builder.load_file("components/homescreen.kv")
# Builder.load_file("components/newsscreen.kv")
# Builder.load_file("components/spotifyscreen.kv")
# Builder.load_file("components/dealsscreen.kv")
# Builder.load_file("components/navbar.kv")

class MyScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super(MyScreenManager, self).__init__(**kwargs)
        Window.size = (800, 480)
        Window.bind(on_motion=self.on_motion)
        # Clock.schedule_once(self.screen_switch_home, 2)

    def on_motion(self, window, pos, eh):
        return

    # def screen_switch_home(self, dt):
    #     self.current = '_home_screen_'
    #     Clock.schedule_once(self.screen_switch_news, 2)

    # def screen_switch_news(self, dt):
    #     self.current = '_news_screen_'
    #     self.ids.home_screen.ids.home_screen_label.text = "Hi I'm The fifth screen spooky!"
    #     Clock.schedule_once(self.screen_switch_spotify, 2)

    # def screen_switch_spotify(self, dt):
    #     self.current = '_spotify_screen_'
    #     Clock.schedule_once(self.screen_switch_deals, 2)

    # def screen_switch_deals(self, dt):
    #     self.current = '_deals_screen_'
    #     Clock.schedule_once(self.screen_switch_home, 2)

class MainApp(App):
    kv_directory = 'ui'
    def build(self):
        return MyScreenManager()

class DebugTracer(App):
    def build(self):
        return TouchTracer()

if __name__ == "__main__":
    if not platform.system() == 'Windows':
        Window.fullscreen = True
    # DebugTracer().run()
    # print(kivy.input.MotionEventFactory.list())
    MainApp().run()