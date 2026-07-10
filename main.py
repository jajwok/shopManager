from kivy.app import App
from kivy.uix.label import Label    

class dataEntryForm(GridLayout):
    
    


class MyApp(dataEntryForm):
    def build(self):
        return dataEntryForm()
    
if __name__ == '__main__':
    MyApp().run()