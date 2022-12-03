# Light-weight Python-based No-Library API
This is a "API" that I adopted into after 4 iterations. It is meant as a suggestion and starting point for a possible discussion.

## General
### Advantages
- extraction does not require custom libraries
- can be used in command-lines and dynamically imported into python (see below for code)
- validators are easy: diff file head and tail and test if given example is extracted
- (additional ...)

### Disadvantages
- has some python baggage around it, compared to straight conversion
- uses an unconventional approach
- Other languages (R, etc.) required either translation or a wrapper. I have written a CWL wrapper.
- (additional ...)


## Implementation
### Extractor arguments
- file path (could be file object to allow for data stream)
- recipe (allows to customize extraction)
- save fig (allows to save a "thumbnail" to file)
- additional keywords

### Extractor returns a dictionary of
- image: a meaningfull thumbnail: base64-encoded or svg
- metaVendor: metadata directly copied from vendor file
- metaUser: metadata the scientist creates in the extractor
- recipe (as output)
- [optionally] links to other datasets: not included in the examples

## Caveat
My python code uses 2-space indentation and rather long lines since I really hate scrolling. I am open to scroll-focused codes if the majority prefers.


## Usage
### How to use it as command-line
``` bash
./extractor_png.py example.png
```
Image is not outputted since it can be outputted via arguments. Only one argument is used in current version, but this can be extended.

### How to use in python code
``` python
import base64
from io import BytesIO
from PIL import Image
from extractor_tif import use

content = use('example.tif')   #plain open
content = use('example.tif',saveFileName='myName.jpg')  #save to a file for verification
content = use('example.tif','crop',saveFileName='myName.jpg') #crop stupid bar at bottom and save to file for ...

#Look at stuff
print(content['metaUser'])
print(content['metaVendor'])
print(content['recipe'])

#Look at image
extension = content['image'][11:14]
i = base64.b64decode(content['image'][22:])
i = BytesIO(i)
i = Image.open(i)
i.show()
```

In my code, I link dynamically. If I get a file with a certain extension, then I look if I have a suitable extractor based on the extension and run through those extractors. If the returned value is an empty dict, I go to the next extractor.
