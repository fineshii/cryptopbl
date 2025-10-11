import numpy as np
from PIL import Image

def reconstruct(shares_paths):
    combined = None
    for path in shares_paths:
        img = Image.open(path).convert('1')
        data = np.array(img) // 255
        if combined is None:
            combined = data
        else:
            combined ^= data  # XOR for reconstruction

    Image.fromarray(combined * 255).show()
