"""A programming language class."""


class ProgrammingLanguage:
    """Class structure for different programming languages."""

    def __init__(self, name, typing, reflection, year):
        self.name = name.title()
        self.typing = typing.title()
        self.reflection = bool(reflection)
        self.year = year

    def __str__(self):
        string_format = "{}, {} Typing, Reflection = {}, First appeared in {}".format(self.name, self.typing,
                                                                                      self.reflection, self.year)
        return string_format

    def is_dynamic(self):
        return self.typing == "Dynamic"
