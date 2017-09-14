from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Label
from kivy.properties import StringProperty

NAMES = ["Craig", "Hannah", "Kyle", "Nicholas", "Trent", "Adam", "Jaiden", "Trevor", "Shane"]


class NameLooper(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.labels = []
        self.names = NAMES
        self.label_index = 0

    def build(self):
        self.title = "Name Looper"
        self.root = Builder.load_file("name_looper.kv")
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.names:
            temp_label = Label(text=name)
            self.labels.append(temp_label)

    def display_widget(self):
        try:
            self.root.ids.display_field.add_widget(self.labels[self.label_index])
            self.label_index += 1
        except IndexError:
            NameLooper.clear_names(self)

    def clear_names(self):
        self.label_index = 0
        self.root.ids.display_field.clear_widgets()


NameLooper().run()
