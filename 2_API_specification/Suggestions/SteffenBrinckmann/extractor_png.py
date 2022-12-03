#!/usr/bin/python3
"""extract data from a .png file
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
  metaVendor = image.info
  imgArr = np.array(image)
  if len(imgArr.shape)==3:
    imgArr = imgArr[:,:,0]
  if recipe.endswith('crop'):                   #: Crop 3/4 of the image
    newHeight = int(imgArr.shape[0]/2)
    newWidth  = int(imgArr.shape[1]/2)
    imgArr = imgArr[:newHeight, :newWidth]
    recipe = 'image/png/crop'
  else:                                         #: Default | uncropped
    recipe = 'image/png'
  maskBlackPixel = imgArr<128
  metaUser   = {'number black pixel': len(maskBlackPixel[maskBlackPixel]),
                'number all pixel': int(np.prod(image.size)) }

  #save to file
  imageData = Image.fromarray(imgArr).convert('P')
  if saveFileName is not None:
    imageData.save(saveFileName)

  # convert PIL image to base64
  figfile = BytesIO()
  imageData.save(figfile, format="PNG")
  imageData = base64.b64encode(figfile.getvalue()).decode()
  imageData = "data:image/png;base64," + imageData

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
