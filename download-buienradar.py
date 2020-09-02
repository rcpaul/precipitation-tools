#!/usr/bin/python3

from datetime import datetime, timedelta
import os.path
import urllib.request
import time

start = datetime.fromisoformat("2020-08-01")
end = datetime.fromisoformat("2020-09-01")

current = start
while current < end:
	stamp = current.strftime("%Y%m%d%H%M")
	url = "https://image.buienradar.nl/2.0/archive/image/radarmaprainnl/" + stamp
	filename = "downloads/" + stamp + '.png'
	if not os.path.isfile(filename):
		print("Downloading " + url)
		try:
			urllib.request.urlretrieve(url, filename)
		except:
			print("Got error downloading")

		time.sleep(1)
	
	current = current + timedelta(seconds=300)
