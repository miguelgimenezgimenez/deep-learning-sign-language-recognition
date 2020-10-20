import cv2

import time
from tensorflow import keras

import numpy as np
from imageProcessing import resizeImg, generateMask

cam = cv2.VideoCapture(0)  
from PIL import Image


while True:
    

    ret, frame = cam.read()
    im = Image.fromarray(frame)

    resized_image = resizeImg(im, dimension=(256,384))
    mask = generateMask(resized_image)

    foreground_mask = np.any(mask != [0, 0, 0], axis=-1)
    imgarray = np.array(resized_image.convert("RGB"))
    foreground_mask_reshaped =np.repeat(foreground_mask[:, :, np.newaxis], 3, axis=2)

    foreground_mask_image = foreground_mask_reshaped*imgarray

    cv2.imshow('Video', foreground_mask_image)
 
    
    if (cv2.waitKey(1) & 0xFF == ord("q")) or (cv2.waitKey(1) == 27):
        break
# close camera
cam.release()
cv2.destroyAllWindows()
