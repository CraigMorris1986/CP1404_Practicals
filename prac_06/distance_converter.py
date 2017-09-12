"""
Converts miles to kilometers with a Kivy GUI.
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class MilesToKmApp(App):
    """A Kivy app to convert imperial miles to metric kilometers."""

    def build(self):
        Window.size = (480, 480)
        self.title = "Miles to KM"
        self.root = Builder.load_file("distance_converter.kv")
        return self.root

    def handle_conversion(self, miles):
        miles = check_if_valid_number(miles)
        kilometers = int(miles) * 1.6
        self.root.ids.KM.text = "{:.2f} KM".format(kilometers)

    def handle_increment_up(self, miles):
        miles = check_if_valid_number(miles)
        miles = int(miles) + 1
        self.root.ids.miles.text = str(miles)

    def handle_increment_down(self, miles):
        miles = check_if_valid_number(miles)
        miles = int(miles) - 1
        self.root.ids.miles.text = str(miles)


def check_if_valid_number(number):
    try:
        int(number)
        return number
    except ValueError:
        return int(0)


MilesToKmApp().run()
