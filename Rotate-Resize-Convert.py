#!/usr/bin/env python3
import os
from PIL import Image

inputFolder  = 'images/'
outputFolder = '/opt/icons'

for image in os.listdir(inputFolder):
  if image != ".DS_Store":
        im = Image.open(os.path.join(inputFolder, image))
        im = im.rotate(-90)
        im = im.resize((128,128))
        im = im.convert("RGB")
        im.save(os.path.join(outputFolder, image+".jpeg"))
