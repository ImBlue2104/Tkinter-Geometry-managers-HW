from tkinter import Tk, Frame, Button

root = Tk()
root.geometry("300x200")

# Create a frame
my_frame = Frame(root, bg="lightblue", width=200, height=100)
my_frame.pack(pady=20)

# Add a button inside the frame
btn = Button(my_frame, text="Click Me")
btn.pack()

root.mainloop()
