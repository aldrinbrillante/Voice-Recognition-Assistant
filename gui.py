import tkinter

from tkinter import *

from PIL import ImageTk,Image

app=Tk()
app.title("Friday")

#set width and height

screen = Canvas(app,width=926,height=720)


image=ImageTk.PhotoImage(Image.open("friday.png"))

screen.create_image(0,0,anchor=NW,image=image)
screen.pack()
app.mainloop()