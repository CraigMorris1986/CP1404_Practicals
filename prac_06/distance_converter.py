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
        miles = convert_to_integer(miles)
        kilometers = int(miles) * 1.6
        self.root.ids.KM.text = "{:.2f} KM".format(kilometers)

    def handle_increment(self, miles, increment):
        miles = convert_to_integer(miles)
        # miles = int(miles) + 1
        miles += increment
        self.root.ids.miles.text = str(miles)


def convert_to_integer(number):
    try:
        # int(number)
        return int(number)
    except ValueError:
        return 0


MilesToKmApp().run()
