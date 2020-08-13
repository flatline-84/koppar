import os
from kivy.clock import Clock
from kivy.uix.screenmanager import Screen

class SettingsScreen(Screen):

    def restart(self, instance):
        os.system("sudo reboot")
    def shutdown(self, instance):
        os.system("sudo halt -p")
    
    def update(self, instance):
        # print(self.ids.keys())
        self.ids.output_window.text = "Updating..."
        os.system("git pull")
        self.ids.output_window.text += "\nPulled latest release..."
        self.ids.output_window.text += "\nRestarting in 3..."
        Clock.schedule_once(self.restartLightDM, 3)

    def restartLightDM(self):
        os.system("sudo pkill lightdm")
        