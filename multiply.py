import sublime_plugin


class MultiplyInput(sublime_plugin.TextInputHandler):
    def __init__(self, view):
        self.view = view

    def placeholder(self):
        return "1.0"

    def initial_text(self):
        return "1.0"

    def validate(self, text):
        try:
            _ = float(text)
            return True
        except ValueError:
            return False


class MultiplyNumbers(sublime_plugin.TextCommand):
    def run(self, edit, multiply_input):
        self.multiply_and_replace_numbers(edit, multiply_input)

    def input(self, args):
        return MultiplyInput(self.view)

    def format_number(self, number):
        formatted = f"{number:.2f}"

        if formatted[-1] == "0":
            formatted = f"{number:.1f}"

        if formatted[-1] == "0":
            formatted = str(int(number))

        return formatted

    def multiply_and_replace_numbers(self, edit, value):
        value = float(value)
        region = self.view.sel()[0]
        text = self.view.substr(region)

        numbers = [float(n) * value for n in text.split(",")]

        new_text = ",".join(self.format_number(n) for n in numbers)
        self.view.replace(edit, region, new_text)
