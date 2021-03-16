import numpy as np
import cv2
from image import *


def img_read(path):
    """
    Read the image with given `path` to a RGBImage instance.
    """
    mat = cv2.imread(path).transpose(2, 0, 1).tolist()
    mat.reverse()  # convert BGR (cv2 default behavior) to RGB
    return RGBImage(mat)


def img_save(path, image: GreyImage):
    """
    Save a RGBImage instance (`image`) as a image file with given `path`.
    """
    rgb_image = image.to_rgb()
    mat = np.stack(list(reversed(rgb_image.get_pixels()))).transpose(1, 2, 0)
    cv2.imwrite(path, mat)

image = img_read("img/dsc20.png")
greyed = ImageProcessing.grayscale(image)
img_save('img/output/dsc20_greyed.png', greyed)
encoded = ImageProcessing.arnold_encode(greyed, shuffle_times=5)
img_save('img/output/dsc20_encoded.png', encoded)

xored = ImageProcessing.xor_key(encoded, key=50)
img_save('img/output/dsc20_xored.png', encoded)

unxored = ImageProcessing.xor_key(xored, key=50)
img_save('img/output/dsc20_unxored.png', encoded)

decoded = ImageProcessing.arnold_decode(unxored, shuffle_times=5)
img_save('img/output/dsc20_decoded.png', decoded)

