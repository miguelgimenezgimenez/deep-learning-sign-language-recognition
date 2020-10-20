
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('data/asl_alphabet_test/A_test.jpg',0)
print(img)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# while True:

#   cv2.imshow('Video', img)

#   if (cv2.waitKey(1) & 0xFF == ord("q")) or (cv2.waitKey(1) == 27):
#         break

ret,thresh1 = cv2.threshold(img,60,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
print(thresh1)
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()