# import kivy module  
import kivy  

kivy.require("1.9.1")  

from kivy.app import App
  

from kivy.uix.vkeyboard import VKeyboard
  
# Create the vkeyboard
class Test(VKeyboard):
    player = VKeyboard()
  
# Create the App class
class VkeyboardApp(App):
    def build(self):
        return Test()
  
# run the App
if __name__ == '__main__':
    VkeyboardApp().run()