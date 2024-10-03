from kivy.app import App
from kivy.uix.widget import Widget
from kivy.animation import Animation
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

# Set the app size
Window.size = (500, 700)

# Designate our .kv design file
Builder.load_file('whathever.kv')

class MyGridLayout(Widget):
   
    name = ObjectProperty(None)
    pizza = ObjectProperty(None)
    color = ObjectProperty(None)
   
    def press(self, instance):
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text
        
        print(f'Hello {name}, you like {pizza} pizza, and you favorite color is {color}!')
        # self.add_widget(Label(text=f'Hello {name}, you like {pizza} pizza, and you favorite color is {color}!'))

        self.name.text = ""
        self.pizza.text = ""
        self.color.text = ""
        
        
        

class AwesomeApp(App):
    def build(self):
        # return Label(text="Hello World!", font_size=72)
        return MyGridLayout()
     
    
    
if __name__ == '__main__':
    AwesomeApp().run()
