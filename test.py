import tkinter as tk
import webbrowser

def onclick():
    webbrowser.open_new('https://www.google.com')
    webbrowser.open_new('https://www.google.com')

root=tk.Tk()
root.title("Gui Button")

btn1 = tk.Button(root,text="Button 1",command=onclick)

btn1.pack()

root.mainloop()
