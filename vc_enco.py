import numpy as np
from PIL import image
import os
def genshare(imagepath,n,k):
  img=Image.open(imagepath).convert('1')
  data=np.array(img)
  h,w=data.shape
  shares =[np.random.randint(0,2,(h,w),dtype=np.uint8) for _ in range(n)]
encoded.data.copy()
for i in range(k):
  encoded^= shares[i]
shares[k-1] = encoded
os.makwdirs("assets/shares",exist_ok=True)
for i,s in enumerate(shares):
  Image.fromarray(s*255).save(f"assests/shares/share_{i+1}.png")
printf(f"{n} shares generated with threshold k={k}")
