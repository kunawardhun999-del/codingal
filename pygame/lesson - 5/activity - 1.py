import tkinter as tk
root = tk.Tk()
root.title("main")
root.geometry("400x300")

def topwin():
    top = tk.Toplevel(root)
    top.title("top level")
    top.geometry("100x100")
    L2 = tk.Label(top, text="This is a top level window")
    L2.pack()

L1 = tk.Label(root, text="This is the main window")
L1.pack()

btn = tk.Button(root, text="Click here to open another window", command=topwin)
btn.pack()

root.mainloop()