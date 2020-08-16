# -*- coding: utf-8 -*-
"""
Created on Fri May 14 22:22:14 2020

@email_id : shubham.more26@gmail.com
@author: SHUBHAM MORE
"""

import csv
from tkinter import *
from tkinter import messagebox
import datetime
import tkinter as tk
from googletrans import Translator
import googletrans
from PIL import Image, ImageTk

translator = Translator()

languages_lis =dict (googletrans.LANGUAGES)

# fetching current date
date = str(datetime.datetime.now().date())

# creating root object
root = Tk()
root.title(" Google Dictionary ".title())
root.geometry("650x550+350+200")
root.resizable(FALSE, FALSE)
root.iconphoto(FALSE, tk.PhotoImage(file='gtl.png'))
# top frame
top = Frame(root, height=150, bg='#F0F0F0')
top.pack(fill=X)

# bottom
bottom = Frame(root, height=500, bg='#34baeb')
bottom.pack(fill=X)

# title Segoe Print
heading = Label(top, text="dictionary in pyhton".title(), font=('Edwardian Script ITC', 40, 'bold'), fg='black')
heading.place(x=90, y=35)

#-------------------------BODY-------------------------------------------------------------------


def search():
    try:
        if variable.get() == 'Select':
            result.insert(END, "")
            key = data.get("1.0", "end-1c")
            results = translator.translate(key, dest='mr')
            result.delete("1.0", END)
            result.insert(END, results.text)
        else:
            result.insert(END, "")
            key = data.get("1.0", "end-1c")
            results = translator.translate(key, dest=variable.get())
            result.delete("1.0", END)
            result.insert(END, results.text)
    except EXCEPTION as msg:
        messagebox.ERROR(msg)





search = Button(bottom,padx=40, compound=LEFT, text="Translate ", font='arial 15  ',
                        command=search)
search.place(x=235, y=100)

data = Text(bottom,font= 20, height=21, width=23)
data.place(x= 10, y=10)

imgimage = Image.open("gtl.png")

photo = ImageTk.PhotoImage(imgimage)

label = Label(bottom, image=photo)
label.image = photo # keep a reference!
label.place(x=250, y=150)




# listbox
variable = tk.StringVar(bottom)
variable.set("Select")
opt = OptionMenu(bottom, variable, *languages_lis.values())
opt.config(width=10,padx=25, pady=5, font=('Helvetica', 12))
opt.place(x=240, y=10)

result = Text(bottom,font= 20, height=21, width=23)
result.place(x= 435, y=10)






root.mainloop()
