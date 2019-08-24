from nasa import apod
from tkinter import Tk, Label, Button
from tkinter.font import Font
import urllib.request
import os
from PIL import ImageTk, Image


def nasaCall():
    # Getting Picture of the day
    os.environ["NASA_API_KEY"] = "VqgrgkFLddU85K1dz9iCCxqyuNdgRarFgTHgjslH"
    image = apod.apod('2019-08-23')
    payload = image.url
    # Download the image using the URL in payload
    urllib.request.urlretrieve(payload, "ApodNasa.jpg")


# Create the main UI
class homeDisplay:
    def __init__(self, master):
        self.master = master
        master.resizable(True, True)
        master.geometry("610x500")
        master.config(background='white')
        master.label = Label(text="Welcome to the window of the Cosmos", width=15, foreground="green", background="white")
        myFont = Font(family="Trebuchet MS", size=15)
        master.label.config(font=myFont)
        master.label.pack(anchor='n')
        im = Image.open("C:/Users/Jachimike Onuoha/Pictures/thunder.jpg")
        logo = ImageTk.PhotoImage(im)
        master.label2 = Label(master, image=logo, background='black')
        master.label2.pack(anchor='center')
        nasaCall()


win = Tk()
win.title("SkySight")
display = homeDisplay(win)
win.mainloop()
