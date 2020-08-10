#!/usr/bin/python3
import kivy
kivy.require('1.11.1')

import platform

from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.boxlayout import BoxLayout

Builder.load_file("components/homescreen.kv")
Builder.load_file("components/newsscreen.kv")
Builder.load_file("components/spotifyscreen.kv")
Builder.load_file("components/dealsscreen.kv")
# Builder.load_file("components/navbar.kv")

class HomeScreen(Screen):
    # def build(self):
        # return Builder.load_file("homescreen.kv")
    pass

class NewsScreen(Screen):
    pass

class SpotifyScreen(Screen):
    pass

class DealsScreen(Screen):
    pass

class MyScreenManager(ScreenManager):

    def __init__(self, **kwargs):
        super(MyScreenManager, self).__init__(**kwargs)
        self.transition = FadeTransition()
    #     Clock.schedule_once(self.screen_switch_home, 2)

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
    kv_directory = 'components'

    def build(self):
        return MyScreenManager()

if __name__ == "__main__":
    if not platform.system() == 'Windows':
        Window.fullscreen = True
    MainApp().run()