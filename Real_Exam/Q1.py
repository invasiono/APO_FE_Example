"""Q1 - Message Form

Students: complete this file directly. Do not create another Python file.
"""

from tkinter import *
from tkinter import messagebox

# =================CODE HERE=========================
def send_message():
    info1 = text_name.get()
    info2 = text_message.get("1.0", "end-1c")
    
    if info1 and info2 != "":
        msg = messagebox.askyesno("Confirm submission", f"Send message to {info1}?")
        if msg == True:
            messagebox.showinfo("Submitted", f"Your message has been sent to {info1}")
    else:
        messagebox.showwarning("Missing Information", "Please enter name of the message recipient and message.")    
        
def clear_form():
    msg = messagebox.askyesno("Clear form", "Do you want to clear all input?")
    if msg == True:
        text_name.delete(0, "end")
        text_message.delete("1.0", "end-1c")

def show_about():
    msg = messagebox.showinfo("About","Message Form\nAPO201C")

root = Tk()
root.title("Message Form")
root.geometry("500x300")

label1 = Label(root, text="Send to:").grid(row=0, column=0)
label2 = Label(root, text="Message:").grid(row=1, column=0)

text_name = Entry(root, width=25)
text_name.grid(row=0, column=1, sticky="w", padx=20, pady=10)

text_message = Text(root, width=25, height=5)
text_message.grid(row=1, column=1, padx=20)

button1 = Button(root, text="Send", command=send_message, width=10)
button1.grid(row=2, column=0, pady=10)

button2 = Button(root, text="Clear", command=clear_form)
button2.grid(row=2, column=1)

button3 = Button(root, text="About", command=show_about)
button3.grid(row=2, column=2)

# Use the following widget names when you create the two Text widgets:
#   text_name     - one-line Text widget for the message recipient, width = 25
#   text_message  - Text widget for the message body, height = 5 and width = 25
#


# ===================================================


root.mainloop()
