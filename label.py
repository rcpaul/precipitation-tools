#!/usr/bin/python3

from datetime import datetime, timedelta
import os.path
from PIL import Image, ImageDraw, ImageFont
import time

start = datetime.fromisoformat("2020-08-01")
end = datetime.fromisoformat("2020-09-01")

current = start
while current < end:
	stamp = current.strftime("%Y%m%d%H%M")
	fileIn = "downloads/" + stamp + '.png'
	fileOut = "labelled/" + stamp + '.png'
	if os.path.isfile(fileIn) and not os.path.isfile(fileOut):
		print("Labelling " + fileIn)
		image = Image.open(fileIn)
		draw = ImageDraw.Draw(image)
		font = ImageFont.truetype("FreeSansBold.ttf", 16)
		draw.text((20, 4), current.strftime("%Y-%m-%d"), font=font, fill=(0, 0, 0))
		draw.text((19, 3), current.strftime("%Y-%m-%d"), font=font)
		image.save(fileOut)
	
	current = current + timedelta(seconds=300)
