from kivy.uix.boxlayout import BoxLayout
from gui.screen import Screen
from gui.keyboard import KeyBoard


class Window(BoxLayout):

    def __init__(self, **kwargs):
        super(Window, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.__screen = Screen()
        self.__keyboard = KeyBoard()
        self.add_widget(self.__screen)
        self.add_widget(self.__keyboard)
        self.__bindEventsOnButtons()

    @property
    def screen(self):
        return self.__screen

    @property
    def keyboard(self):
        return self.__keyboard

    def writeOnScreen(self, instance):
        screenText = self.__screen.text
        screenText += instance.text
        self.__screen.text = screenText

    def __bindEventsOnButtons(self):
        number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
        for btn in self.keyboard.buttons:
            if btn in number:
                self.keyboard.buttons[btn].bind(on_press=self.writeOnScreen)
