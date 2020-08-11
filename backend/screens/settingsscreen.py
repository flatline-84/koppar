import os
from kivy.uix.screenmanager import Screen

class SettingsScreen(Screen):
    def restart(self, instance):
        os.system("sudo reboot")
    def shutdown(self, instance):
        os.system("sudo halt -p")
    def update(self, instance):
        os.system("git pull")
        os.system("sudo pkill lightdm")
