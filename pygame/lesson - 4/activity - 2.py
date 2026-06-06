from tkinter import*
window=Tk()
window.title()
window.geometry('500x500')
def display():
  print(login)
f1= Frame(master=window, height=200, width=360, bg='white')
f1.pack()

lbl1=Label(f1, text='Name', height=2, width=12, bg='black', fg='white')
lbl1.place(x=20, y=10)

lbl2=Label(f1, text='Email', height=2, width=12, bg='black', fg='white')
lbl2.place(x=20, y=60)

lbl3=Label(f1, text='Password', height=2, width=12, bg='black', fg='white')
lbl3.place(x=20, y=110)

name_entry=Entry(f1)
name_entry.place(x=120,y=10)

Email_entry=Entry(f1)
Email_entry.place(x=120, y=60)

Pswd_entry=Entry(f1)
Pswd_entry.place(x=120, y=110)

btn = Button(text='Create Account', command=display, bg='red')
btn.place(x=130, y=210)

textbox= Text(bg='black', fg="white")
textbox.place(y=250)

window.mainloop()