from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Label
from kivy.properties import StringProperty

NAMES = ["Craig", "Hannah", "Kyle", "Nicholas", "Trent", "Adam", "Jaiden", "Trevor", "Shane"]


class NameLooper(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = NAMES

    def build(self):
        self.title = "Name Looper"
        self.root = Builder.load_file("name_looper.kv")
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.display_field.add_widget(temp_label)


    def clear_names(self):
        self.root.ids.display_field.clear_widgets()

NameLooper().run()
