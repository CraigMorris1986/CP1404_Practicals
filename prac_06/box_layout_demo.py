from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        # print("Welcome.")
        self.root.ids.output_label.text = "Welcome " + self.root.ids.input_name.text

    def clear_text_field(self):
        self.root.ids.input_name.text = ""


class GreeterProgram(App):
    def build(self):
        Window.size = (400, 200)
        self.title = "Greeter Program"
        self.root = Builder.load_file('greeter_program.kv')
        return self.root

    def clear_text(self):
        self.root.ids.text_field.text = ""

    def handle_greet(self):
        self.root.ids.output_label.text = "Greetings " + self.root.ids.text_field.text

# BoxLayoutDemo().run()
GreeterProgram().run()