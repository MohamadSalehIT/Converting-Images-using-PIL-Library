#!/usr/bin/env python3
import os

from PIL import Image
#this is the directory containing the images
inputFolder  = 'images/'
#this is the directory where the formatted images will be placed
outputFolder = 'newImages'
#NOTE : Both directories are in the same path

for image in os.listdir(inputFolder):
  if image != ".DS_Store":
        im = Image.open(os.path.join(inputFolder, image))
      #Re-rotating the image to the right place
        im = im.rotate(-90)
      #Resizing the image from 192x192 to 128x128
        im = im.resize((128,128))
        im = im.convert("RGB")
      #Converting the images to the JPEG format and placing them in the new directory
        im.save(os.path.join(outputFolder, image+".jpeg"))
