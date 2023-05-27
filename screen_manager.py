from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.factory import Factory
from kivymd.app import MDApp
Builder.load_file('screen_manager.kv')
class MainWindow(Screen):
    pass


class SecondWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class MyMainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = 'Box Layout Test'
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Cyan'
        self.theme_cls.accent_palette = 'Lime'

    def build(self):
        self.root = Factory.WindowManager()


if __name__ == '__main__':
    MyMainApp().run()