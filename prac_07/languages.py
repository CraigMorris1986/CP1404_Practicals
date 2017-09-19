from prac_07.programming_language import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(ruby)
    print(ruby.is_dynamic())
    print(python)
    print(python.is_dynamic())
    print(visual_basic)
    print(visual_basic.is_dynamic())
    languages = [ruby, python, visual_basic]
    display_dynamic_languages(languages)


def display_dynamic_languages(programming_languages):
    for language in programming_languages:
        if language.is_dynamic():
            print(language.name)


main()
