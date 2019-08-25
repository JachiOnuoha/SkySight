# SkySight
# Lightning Code
# Created by Jachimike Onuoha
# Copyright © 2019 Jachimike Onuoha. All rights reserved.

from nasa import apod
from tkinter import *
from tkinter.font import Font
import urllib.request
import os
from PIL import ImageTk, Image
from random import randrange
from datetime import *
import time


# Nasa API Call to download image and get title
def getApod(date):
    # Getting Picture of the day
    os.environ["NASA_API_KEY"] = "NASA_API_KEY"
    image = apod.apod(date)
    payload = image.url
    # Download the image using the URL in payload
    urllib.request.urlretrieve(payload, "ApodNasa.jpg")
    data = "{}*{}*{}".format(image.title, image.explanation, date)
    # print(data)
    return data

# Generate a random date for the Picture of the Day
def random_date():
    start = datetime.strptime('12/31/1995 1:30 PM', '%m/%d/%Y %I:%M %p')
    end = datetime.strptime('8/24/2019 4:50 AM', '%m/%d/%Y %I:%M %p')
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

# Download and load next APOD image and facts
def next():
    # Console Output
    print("Fetching NASA data...")
    
    # Get date
    date = random_date()
    current = str(date.date())
    print(current)
    
    # Recall API
    value = getApod(current)
    imgInfo = value.split('*', 2)
    
    # Update Title
    Label_one.config(text=imgInfo[0]+' ('+imgInfo[2]+')')
    
    # Update Description
    Label_three.config(text=imgInfo[1])
    
    # Update Image
    im2 = Image.open("IMAGE_FILE_PATH")
    logo2 = ImageTk.PhotoImage(im2)
    Label_two.config(image=logo2)
    Label_two.image = logo2


# Initial Call
response = getApod('2019-08-24')
imgInfo = response.split('*', 3)

# Create the main UI
win = Tk()
win.title("SkySight")
win.resizable(False, False)
win.geometry("900x640")
win.config(background='black')


# Title Label
Label_one = Label(text=imgInfo[0]+' ('+imgInfo[2]+')', height=1, foreground="white", background="black")
myFont = Font(family="Trebuchet MS", size=15)
Label_one.config(font=myFont)
Label_one.pack(anchor='center', fill='x')

# Image and Description Frames
picFrame = Frame(win)
picFrame.pack(anchor='center', fill='x')
bottomframe = Frame(win)
bottomframe.pack(anchor='center')

# Nasa Image display
im = Image.open("IMAGE_FILE_PATH")
logo = ImageTk.PhotoImage(im)
Label_two = Label(picFrame, image=logo, background='black', width=700, height=360)
Label_two.pack(fill='x')

# Image Description display
Label_three = Label(bottomframe, text=imgInfo[1], width=700, height=10, wraplength="800", justify=LEFT, foreground="white", background="black")
myFont = Font(family="Trebuchet MS", size=10)
Label_three.config(font=myFont)
Label_three.pack(anchor='center')

# Next button
win.button = Button(text="Another Image", background='gray', foreground='white', command=next)
win.button.config(font=myFont)
win.button.pack(anchor='center')


win.mainloop()
