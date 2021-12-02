"""Greetings class generating greet string from input

Returns:
    string: greet string
"""

class Greeting:

    def __init__(self, name):
        self.name = name

    def greet(self):
        return "Python hails {}.".format(self.name)

