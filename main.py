from kivy.app import App
from kivy.uix.label import Label  
from kivy.uix.widget import Widget 
from kivy.core.window import Window
import sqlite3

Window.size = (400, 500)
# class dataEntryForm(GridLayout):
#   pass  

# database connection
with sqlite3.connect('shop.db') as connection:
    # Create a cursor object
    cursor = connection.cursor()

# Close the database connection
connection.close()

class DataEntry(Widget):
    def get_widget_values(self):
        # Get the values from the widgets
        item = self.ids.item_input.text
        gender = self.ids.gender_input.text
        age = self.ids.age_input.text
        quantity = self.ids.quantity_input.text
        payment_method = self.ids.payment_method_input.text
        notes = self.ids.notes_input.text
        
        print(f"Item: {item}")
        print(f"Gender: {gender}")
        print(f"Age: {age}")
        print(f"Quantity: {quantity}")
        print(f"Payment Method: {payment_method}")
        print(f"Notes: {notes}")

    def calculate_amount(self, *args):
        unit_price = 15
        quantity_text = self.ids.quantity_input.text
    
        try:
            # Safely convert to integer and multiply
            quantity = int(quantity_text)
            total_amount = quantity * unit_price
            self.ids.amount_label.text = f"{total_amount}"
        
        except ValueError:
            # Handles empty text input or edge cases when input is cleared
            self.ids.amount_label.text = "0"

        
        

class RecordsScreen(Widget):
    pass

class MyApp(App):
    #app title
    title = 'Shop Manager'
    def build(self):
        return DataEntry()
    
if __name__ == '__main__':
    MyApp().run()