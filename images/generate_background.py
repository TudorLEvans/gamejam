import numpy as np
import matplotlib.pyplot as plt
from PIL import Image as im

height = 10000
img = np.zeros([height,600,3])
array = 255*np.arange(height)/height

for i in range(600):
    img[:,i,2] = array

img = np.uint8(img)

data = im.fromarray(img)
data.save('background.png') 