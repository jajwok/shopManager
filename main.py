from kivy.app import App
from kivy.uix.label import Label    
import sqlite3
from name import name
# class dataEntryForm(GridLayout):
#   pass  

# database connection
with sqlite3.connect('shop.db') as connection:
    # Create a cursor object
    cursor = connection.cursor()

# Close the database connection
connection.close()


class MyApp(App):
    def build(self):
        return Label(text=f"Hello  {name}")
    
if __name__ == '__main__':
    MyApp().run()