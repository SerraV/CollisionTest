from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.config import Config
from collections import OrderedDict
Config.set('modules', 'inspector', "")

class WordLabel(Scatter):
    my_string = StringProperty('')
    l = ObjectProperty('')

    def on_pos(self, instance, position):
        root = self.parent
        if root is not None:
            if self.collide_widget(root.c):
                print 'is colliding'

    def __init__(self, text, **kw):
        super(WordLabel, self).__init__(**kw)
        self.my_string = text
        self.id = text

class Root(BoxLayout):
    f = ObjectProperty(None)
    c = ObjectProperty(None)

    word_list = ['Result0','Result1','Result2','Result3','Result4','Result5','Result6','Result7']

    def __init__(self, **kw):
        super(Root, self).__init__(**kw)
        for word in self.word_list:
            self.f.add_widget(WordLabel(word))       

class ExpeApp(App):
    def build(self):
        return Root()

if __name__ == '__main__':
    ExpeApp().run()