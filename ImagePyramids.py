%matplotlib inline
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import skimage
from skimage import data
from skimage import io
from skimage.transform import pyramid_gaussian

image=skimage.data.imread('girlsface_pyramid.jpg') 
rows, cols, dim = image.shape
pyramid = tuple(pyramid_gaussian(image, downscale=2))
composite_image = np.zeros((rows, cols + cols / 2, 3), dtype=np.double)
composite_image[:rows, :cols, :] = pyramid[0]
i_row = 0
for p in pyramid[1:]:
    n_rows, n_cols = p.shape[:2]
    composite_image[i_row:i_row + n_rows, cols:cols + n_cols] = p
    i_row += n_rows        
fig, ax = plt.subplots()
ax.imshow(composite_image)
plt.savefig('composite_image.jpg')
plt.show()    
