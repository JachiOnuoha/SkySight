from nasa import apod
from tkinter import *
from tkinter.font import Font
import urllib.request
import os
from PIL import ImageTk, Image


# Nasa API Call to download image and get title
def getApod():
    # Getting Picture of the day
    os.environ["NASA_API_KEY"] = "VqgrgkFLddU85K1dz9iCCxqyuNdgRarFgTHgjslH"
    image = apod.apod('2019-07-21')
    payload = image.url
    # Download the image using the URL in payload
    urllib.request.urlretrieve(payload, "ApodNasa.jpg")
    data = "{}*{}".format(image.title, image.explanation)
    # print(data)
    return data


response = getApod()
imgInfo = response.split('*', 2)
# print(imgInfo)
# Create the main UI
win = Tk()
win.title("SkySight")
win.resizable(False, False)
win.geometry("800x600")
win.config(background='black')


# Title Label
win.label = Label(text=imgInfo[0], width=35, height=1, foreground="white", background="black")
myFont = Font(family="Trebuchet MS", size=15)
win.label.config(font=myFont)
win.label.pack(anchor='center')
# Image Frame
picFrame = Frame(win)
picFrame.pack(anchor='center')
bottomframe = Frame(win)
bottomframe.pack(anchor='center')

# Nasa Image display
im = Image.open("C:/Users/Jachimike Onuoha/Desktop/my_Work/NASA/main/ApodNasa.jpg")
logo = ImageTk.PhotoImage(im)
win.label = Label(picFrame, image=logo, background='black', width=400, height=350)
win.label.pack()

win.label = Label(bottomframe, text=imgInfo[1], width=600, height=9, wraplength="800", justify=LEFT, foreground="white", background="black")
myFont = Font(family="Trebuchet MS", size=10)
win.label.config(font=myFont)
win.label.pack(anchor='center')

win.button = Button(text="Another Image", background='gray', foreground='white')
win.button.config(font=myFont)
win.button.pack(anchor='center')
win.mainloop()
