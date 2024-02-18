#!/usr/bin/python
from PIL import Image
import os, sys

def crop_center(pil_img, crop_width, crop_height):
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))

def resize():
    path = "" #TODO
    dirs = os.listdir( path )
    for item in dirs:
        if os.path.isfile(path+item):
            print(item)
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            # imResize = im.resize((1024,1024))
            imResize = crop_center(im, 1024, 1024)
            imResize.save(f + ' resized.jpg', 'PNG', quality=100)

resize()