from kivy.uix.actionbar import Label
#imports for Ui(Kivy)
from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen ,ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from pathlib import Path



#imports for functionality(backend.py)
from backend import *



#Screens
class ListScreen(Screen):
    pass

class PlayGroundScreen(Screen):
    pass

class BlankScreen(Screen):
    pass

class MenuScreen(Screen):
    pass

#screen manager


class OGScreen(ScreenManager):
    pass
    
# Custom Widget Defination
class Cbtn(Button):
    pass
class Dbtn(Button):
    pass

#Actual widget on screen
class CircleBtns(FloatLayout):
    pass
class ArrowBtns(FloatLayout):
    pass

#main screen
class mainScreen(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.OGScreen_ = OGScreen()
        CircleBtns_ = CircleBtns()
        ArrowBtns_ = ArrowBtns()
        
        self.OGScreen_.size_hint=(0.6,None)
        self.OGScreen_.height=self.OGScreen_.width*16/9
        
        self.add_widget(self.OGScreen_)
        self.add_widget(CircleBtns_)
        self.add_widget(ArrowBtns_)
        
        
        
    def navmenu(self,arg):
        if arg == 'c':
            self.OGScreen_.current ="list"
    
    def navlist(self,arg):
        pass
        
    def abtnAction(self,m):
        print(m)
        if m =='left':
            self.OGScreen_.next()
    
    
    def cbtnAction(self,m):
        if self.OGScreen_.current == 'menu':
            self.navmenu(m)
        if self.OGScreen_.current == 'list':
                    self.navlist(m)

        


class octabBit(App):
    
    def build(self):
        return mainScreen()

#Afunction to load kv ui from kv files
def loadAsserts():
    AssertList = [
        "cButton.kv",
        "dButton.kv",
        "BlankScreen.kv",
        "MenuScreen.kv",
        "ListScreen.kv",
        "PGScreen.kv",
        "ScreenManager.kv",
    ]
    for file in AssertList:
        Builder.load_file(str(Path(__file__).parent / "GUI_element" / file))

loadAsserts()

#Main entry point to the GUI
if __name__ == "__main__":
    ANTENA = CATPoffline()
    
    
    
    
    octabBit().run()