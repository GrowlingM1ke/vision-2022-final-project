import config
from imutils import paths
import cv2
import numpy as np
from pathlib import Path

'''
inputs = sorted(list(paths.list_images(config.IMAGE_DATASET_PATH)))
masks = sorted(list(paths.list_images(config.MASK_DATASET_PATH)))

indices = []
for i in range(len(masks)):
    m = cv2.imread(masks[i], 0)
    if np.any(m):
        indices.append(i)

inputs = np.array(inputs)[indices]
masks = np.array(masks)[indices]


import shutil
for input in inputs:
    shutil.copy(input, config.IMAGE_HAEM_DATASET_PATH)

for mask in masks:
    shutil.copy(mask, config.MASK_HAEM_DATASET_PATH)

'''

inputs = sorted(list(paths.list_images(config.IMAGE_HAEM_DATASET_PATH)))
masks = sorted(list(paths.list_images(config.MASK_HAEM_DATASET_PATH)))

for i in range(len(inputs)):
    name = Path(inputs[i]).stem
    img_input = cv2.imread(inputs[i], 0)
    img_mask = cv2.imread(masks[i], 0)

    height, width = img_input.shape


    div = 4
    length = int(512 / div)
    for x in range(0,div):
        for y in range(0,div):
            new_quadrant = img_mask[x*length:(x+1)*length, y*length:(y+1)*length]
            if np.any(new_quadrant):
                cv2.imwrite("%s\\%s_%i_%i.png" % (config.MASK_HAEM_4_DATASET_PATH, name, x, y), new_quadrant)
                cv2.imwrite("%s\\%s_%i_%i.png" % (config.IMAGE_HAEM_4_DATASET_PATH, name, x, y), img_input[x*length:(x+1)*length, y*length:(y+1)*length])