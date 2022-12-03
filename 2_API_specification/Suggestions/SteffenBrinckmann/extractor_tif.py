#!/usr/bin/python3
"""extract data from a .tif file
"""
import base64, sys
from io import BytesIO
import numpy as np
from PIL import Image

def use(filePath, recipe='', saveFileName=None, **kwargs):
  """
  Args:
    filePath (string): full path file name
    recipe (string): supplied to guide recipes
                     recipe is / separated hierarchical elements parent->child
    saveFileName (string): if given, save the image to this file-name

  Returns:
    dict: containing image, metaVendor, metaUser, recipe
  """
  # Extractor
  image = Image.open(filePath)
  with open(filePath,'rb') as fIn:
    metadata = fIn.read()
    found = int(metadata.hex().find('5B557365725D'.lower())/2) #/2 since two letters=1byte
    metadata = bytearray(source=metadata[found:]).decode('utf-8', errors='replace').split('\n')
    metaVendor = {i.split('=')[0]:i.split('=')[1].strip() for i in metadata if '=' in i }
  imgArr = np.array(image)
  if len(imgArr.shape)==3:
    imgArr = imgArr[:,:,0]
  if recipe.endswith('crop'):                   #: Crop white bar from bottom
    imgArr = imgArr[:883, :]
    recipe = 'image/tif/crop'
  else:                                         #: Default | uncropped
    recipe = 'image/tif'
  maskBlackPixel = imgArr<10
  metaUser   = {'number black pixel': len(maskBlackPixel[maskBlackPixel]),
                'number all pixel': int(np.prod(image.size)) }

  #save to file
  imageData = Image.fromarray(imgArr)
  if saveFileName is not None:
    imageData.save(saveFileName)

  # convert PIL image to base64
  figfile = BytesIO()
  imageData.save(figfile, format="JPEG")
  imageData = base64.b64encode(figfile.getvalue()).decode()
  imageData = "data:image/jpg;base64," + imageData

  # return everything
  return {'image':imageData, 'recipe':recipe, 'metaVendor':metaVendor, 'metaUser':metaUser}

  #other datatypes could follow here if statements are used
  #...
  #final return if nothing successful
  #return {}


# main function for command-line execution
if __name__ == "__main__":
  if len(sys.argv)>1:
    res = use(sys.argv[1])
    del res['image']
    print(res)
