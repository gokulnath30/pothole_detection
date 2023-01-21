from PIL import Image
import numpy as np

img_array = np.load('C:/projects/smartathon/val/outdoor/scene_00023/scan_00198/00023_00198_outdoor_000_020_depth.npy')
# im = Image.fromarray(img_array)
# # this might fail if `img_array` contains a data type that is not supported by PIL,
# # in which case you could try casting it to a different dtype e.g.:
# # im = Image.fromarray(img_array.astype(np.uint8))

# im.show()

from matplotlib import pyplot as plt
cmap = plt.cm.jet
cmap.set_bad(color="black")
plt.imshow(img_array, cmap =cmap )
plt.show()
