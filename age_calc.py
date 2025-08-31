from tkinter import Tk, Entry, Text, Label, Text, Button
from datetime import date

#Sets Window
root = Tk()
root.title("Age Calculator App")
root.geometry("400x400")

#Screen Title
Label(root, text="Welcome to the Age Calculator App", fg = 'white', bg='black').pack()

#Getting DOB Year
Label(root, text="Enter Birth Year:", fg='black', bg='#d0efff').pack()
Year= Entry(root, fg="black", bg='grey', width=50)
Year.pack()


#Getting Name
Label(root, text="Enter Birth Month:", fg='black', bg='#d0efff').pack()
Month= Entry(root, fg="black", bg='grey', width=50)
Month.pack()


#Getting Name
Label(root, text="Enter Birth Date:", fg='black', bg='#d0efff').pack()
Date= Entry(root, fg="black", bg='grey', width=50)
Date.pack()


#Getting Name
Label(root, text="Enter Name:", fg='black', bg='#d0efff').pack()
Name= Entry(root, fg="black", bg='grey', width=50)
Name.pack()


#Func to calc age
def calculate_age(dob):
    today = date.today()
    age = today.year - dob.year

    # If birthday hasn’t happened yet this year, subtract 1
    if (today.month, today.day) < (dob.month, dob.day):
        age -= 1
    return age

#Displays age

def display():
        # Get values from entries *when button is clicked*
    y = int(Year.get())
    m = int(Month.get())
    d = int(Date.get())
    n = Name.get()

    dob = date(y, m, d)  # YYYY, MM, DD
    Message = Label(root, text = f"Hi {n}!!!\n You are {calculate_age(dob)} years old!", fg = 'white', bg = 'black')
    Message.place(x = 130, y = 250)
Button(root, text = "Submit", fg = 'white', bg='black', relief='sunken', command = display).pack()

root.mainloop()

