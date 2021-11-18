# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 12:00:44 2020

@author: scott
"""


# import required classes
 
from PIL import Image, ImageDraw, ImageFont, ImageOps
import pandas as pd
import os
import math

cwd = os.getcwd()
imgdir = cwd + '/SlipPhotos'
savedir = cwd + '/Photos TextAdded'
images = os.listdir(imgdir)

 
# create Image object with the input image
#image = Image.open('test.jpg')
 
# initialise the drawing context with
# the image object as background

# import increments
tracker = pd.read_csv(os.getcwd() + '/Tracker.csv')

# create font object with the font file and specify
# desired size 

for i in range(0,len(tracker)):
    
    tag = tracker['Tag'][i]
    price = tracker['Price'][i]
    size = tracker['Fits Sizes'][i]
    sold = tracker['Sold'][i]
    flip = tracker['Flip'][i]
    iphone = tracker['iphone'][i]
    
    
    font = ImageFont.truetype('Roboto-Bold.ttf', size=90)
    font2 = ImageFont.truetype('Roboto-Bold.ttf', size=130)
    x = 100
    y1 = 100
    y2 = 200
    y3 = 300
    y4 = 500
        
    image = Image.open(imgdir + '/' + tag + '.jpg')
    draw = ImageDraw.Draw(image)
    
    # flip if orientation in photo is incorrect
    if not pd.isnull(flip):
        image = ImageOps.exif_transpose(image)
        draw = ImageDraw.Draw(image)
        
    (x, y) = (x, y1)
    name = tag
    color = 'rgb(255, 255, 255)' # white color
    draw.text((x, y), name, fill=color, font=font)
    
    (x, y) = (x, y2)
    name = '$'+str(price)
    color = 'rgb(255, 255, 255)' # white color
    draw.text((x, y), str(name), fill=color, font=font)
    
    if not pd.isnull(size):
        (x, y) = (x, y3)
        name = size
        color = 'rgb(255, 255, 255)' # white color
        draw.text((x, y), name, fill=color, font=font)
    
    if not pd.isnull(sold):
        (x, y) = (x, y4)
        name = 'SOLD'
        color = 'rgb(255, 0, 0)' # white color
        draw.text((x, y), name, fill=color, font=font2)
    
    
    # save the edited image
    image.save(savedir + '/' + tag + '.jpg')