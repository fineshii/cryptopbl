import numpy as np
from PIL import image
import os
def genshare(imagepath,n,k):
  img=Image.open(imagepath).convert('1')
  data=np.array(img)
  h,w=data.shape
  shares =[np.random.randint(0,2,(h,w),dtype=np.uint8) for _ in range(n)]
