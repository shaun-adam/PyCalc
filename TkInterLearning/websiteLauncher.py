import tkinter as tk
import webbrowser

def reddit(event):
    webbrowser.open_new_tab('http://reddit.com')

def google(event):
    webbrowser.open_new_tab('http://google.ca')

window = tk.Tk()
window.geometry("400x100")
window.title("Test opening tabs")

label1 = tk.Label(text="Here are some buttons to open websites.",font=("Times",14))
label1.grid(column=0,row=0)

button1=tk.Button(window,text="Reddit",bg="orange")
button1.grid(column=0,row=2)
button2=tk.Button(window,text="Google", bg="green")
button2.grid(column=0,row=3)

button1.bind("<Button-1>",reddit)
button2.bind("<Button-1>",google)

window.mainloop()

"""
def doorbell(event):
    print("button was pressed")

window = tk.Tk()
window.title("Test Window")
window.geometry("400x500")
lab = tk.Label(text = "test label here")
lab.grid(column=0,row=0)
mybutton = tk.Button(window, text="test button")
mybutton.grid(column=0,row=1)
mybutton.bind("<Button-1>",doorbell)
window.mainloop()
"""
