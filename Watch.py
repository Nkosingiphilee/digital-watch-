from datetime import datetime
from tkinter import *
#intialize window 
win = Tk()
win.title("Digital clock")
win.resizable(height=False,width=False)


def current_time():
    dt = datetime.now()
    time_label['text'] = dt.strftime('%I:%M:%S %p')
    time_label.after(1000, current_time)


def current_date():
    dt = datetime.now()
    return dt.strftime("%d/%b/%Y")

day=current_date()

time_label = Label(text='',font=('times', 50, 'bold'), bg='green',fg='white')
time_label.pack()
date_label = Label(text=day,font=('times', 20, 'bold'), bg='green') 
date_label.pack()

#call function to update clock label
current_time()

win.mainloop()