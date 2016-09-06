from PIL import Image
from importlib import reload
import DM3lib as dm3
reload(dm3)
dm3f = dm3.DM3('images/single.dm3')
print(dm3f.info)
#print(dm3f.imagedata)
print(dm3f.pxsize)
