import tkinter as tk
import messagebox
import image
from tkinter.tix import IMAGE

root = tk.Tk()
root.title("Denomination Counter")
root.configure(bg="lightblue")
root.geometry("650x400")

# load and display the image
upload = image.open('money.jpg')
upload = upload.resize((300, 300), image.ANTIALIAS)
image = tk.PhotoImage(upload)

Label = tk.Label(root, image=image, bg="lightblue")
Label.place(x=100, y=20)

