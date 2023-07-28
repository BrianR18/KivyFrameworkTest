from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class KeyBoard(GridLayout):

    def __init__(self, **kwargs):
        super(KeyBoard, self).__init__(**kwargs)
        self.cols = 4
        self.rows = 4
        self.__buttons = {}
        self.__buttons['1'] = Button(text='1', font_size=14)
        self.__buttons['2'] = Button(text='2', font_size=14)
        self.__buttons['3'] = Button(text='3', font_size=14)
        self.__buttons['del'] = Button(text='Del', font_size=14)
        self.__buttons['4'] = Button(text='4', font_size=14)
        self.__buttons['5'] = Button(text='5', font_size=14)
        self.__buttons['6'] = Button(text='6', font_size=14)
        self.__buttons['+'] = Button(text='+', font_size=14)
        self.__buttons['7'] = Button(text='7', font_size=14)
        self.__buttons['8'] = Button(text='8', font_size=14)
        self.__buttons['9'] = Button(text='9', font_size=14)
        self.__buttons['-'] = Button(text='-', font_size=14)
        self.__buttons['='] = Button(text='=', font_size=14)
        self.__buttons['0'] = Button(text='0', font_size=14)
        self.__buttons['*'] = Button(text='*', font_size=14)
        self.__buttons['/'] = Button(text='/', font_size=14)
        for btn in self.__buttons:
            self.add_widget(self.__buttons[btn])

    @property
    def buttons(self):
        return self.__buttons
