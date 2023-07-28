from gui.window import Window
from kivy.app import App


class Calculator(App):

    def build(self):
        return Window()


if __name__ == '__main__':
    calculator = Calculator()
    calculator.run()
