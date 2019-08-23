from nasa import apod
import os

# Getting Picture of the day
os.environ["NASA_API_KEY"] = "YOUR NASA KEY"
image = apod.apod('2019-08-23')
print(image.url)
