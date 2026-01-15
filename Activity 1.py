from tkinter import *

root = Tk()
root.geometry("400x500")
root.title("main")

def topwindow():
    topwindow = Toplevel(root)
    topwindow.geometry("100x180")
    l2 = Label(topwindow, text = "This is a top level widget")
    l2.pack()
    topwindow.mainloop()

l1 = Label(root, text = "This is a root window")
l1.pack()
button = Button(root, text = "Press this button to reveal a topwindow", command = topwindow)
button.pack()

root.mainloop()
    
