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

label1 = tk.Label(root, text="Hey User! Welcome to Denomination Counter Application", bg="lightblue")
label1.place(relx=0.5, y=340, anchor=tk.CENTER)

def msg():
    MsgBox = messagebox.showinfo("Alert",
      "Do you want to calculaate the denomination counter of your money?")
    if MsgBox == "ok":
        topwin()
 button1 = tk.Button(root, text="Let's get started!", command=msg, bg="brown", fg="white")

button1.place(x=260, y=360)

def topwin():
    top = tk.Toplevel(root)
    top.title("Denomination Counter")
    top.configure(bg="light grey")
    top.geometry("600x350+50+50")

    label = tk.Label(top, text="Enter total amount", bg="light grey")
    entry = tk.Entry(top)

lbl = tk.Label(
    top,
    text="Here are the number of notes for each denomination",
    bg="light grey"
)
l1 = tk.Label(top, text="2000", bg="light grey")
l2 = tk.Label(top, text="500", bg="light grey")
l3 = tk.Label(top, text="100", bg="light grey")

t1 = entry(top)
t2 = entry(top)
t3 = entry(top)

def calcualator():
    try:
        amount = int(entry.get())

        notes_2000 = amount // 2000
        amount %= 2000

        amount = amount // 500
        amount %= 500

        amount = amount // 100
        amount %= 100

        t1.delete(0, tk.END)
        t2.delete(0, tk.END)
        t3.delete(0, tk.END)

        t1.insert(0, str(notes_2000))
        t2.insert(0, str(amount_500))
        t3.insert(0, str(amount_100))

    except ValueError:
        messagebox.showerror("Error!", "Please enter a valid number.")

btn = tk.Button(top, text="Calculate", command=calcualator, bg="brown", fg="white")

label.place(x=230, y=50)
entry.place(x=200, y=80)
btn.place(x=240, y=120)

lbl.place(x=140, y=170)

l1.place(x=180, y=200)
l2.place(x=180, y=230)
l3.place(x=180, y=260)

top.mainloop()

root.mainloop()