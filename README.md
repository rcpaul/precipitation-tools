# precipitation-tools

## Contents

This small repository contains some tools that aid in making movies of series of images. It is created to create a movie from buienradar.nl archive images but it can be repurposed for other image sets.

`download-buienradar.py` downloads precipitiation radar archive images that it didn't already download. The second of sleep in between each request is there so it won't overload the website.

`label.py` looks alike but adds date stamps to images. These scripts could be merged.

## Making a movie

My favorite tool for creating a movie from a serie of images is `ffmpeg`.

## Future ideas

* Calculate cumulative radar images somehow. We can 
interpret colors and add up estimated precipitation quantities but maybe we're better of starting with something closer to the source [1]

[1] https://dataplatform.knmi.nl/catalog/index.html