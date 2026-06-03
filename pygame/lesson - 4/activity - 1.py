# "C:\Users\ASUS Zenbook\AppData\Local\Python\pythoncore-3.14-64\python.exe" "c:/Users/ASUS Zenbook/OneDrive/Documents/codingal/pygame/lesson - 4/activity - 1.py"

from tkinter import *
from datetime import date
# Create the main window
window = Tk()

# Set the title and size of the window

window.title("Welcome app")
window.geometry("400x400")
def display():
  print('Welcome')
lbl = Label(text='Welcome App', fg='white', bg='black', 
height=2, width=200)
lbl.pack()

name_lbl = Label(text="Full Name", bg='black', fg='white',
height=2, width=200)
name_lbl.pack()
name_entry= Entry()
name_entry.pack()

btn = Button(text="Begin", command=display
, bg='black', fg='white', height=2
, width=200)
btn.pack()

text_box = Text(height=3)
text_box.pack()

# start the gui event loop
window.mainloop()
