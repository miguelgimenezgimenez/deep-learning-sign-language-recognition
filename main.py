import cv2

import time
from tensorflow import keras
model = keras.models.load_model('models/kerryModelv3')
import numpy as np

letters = [ "E","K", "R","Y","nothing"]

cam = cv2.VideoCapture(0)  

font = cv2.FONT_HERSHEY_SIMPLEX 
org = (180, 40) 
fontScale = 1
thickness = 2
color = (255, 0, 0) 
thresh = 130

frame_rate = 4
prev_time = 0
prev_sign = ["?"]
current_word = ''
img_size = (100,100)

roi_dimension = (10,450)

uniques, ids = np.unique(letters, return_inverse=True)

while True:
    blank_image = 255 * np.ones(shape=[240, 512, 3], dtype=np.uint8)

    ret, frame = cam.read()
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret,binary_image = cv2.threshold(grayFrame,thresh,255,cv2.THRESH_BINARY)

    roi = binary_image[roi_dimension[0]:roi_dimension[1], roi_dimension[0]:roi_dimension[1]]

    cv2.rectangle(frame, (roi_dimension[0], roi_dimension[0]), (roi_dimension[1], roi_dimension[1]), (0, 255, 0), 2)
    cv2.imshow("ROI",roi)
    cv2.imshow('Video', frame)
    time_elapsed = time.time() - prev_time

    cv2.putText(blank_image, f"WAT?", org, font,  
                   fontScale, (0, 255, 0), thickness , cv2.LINE_AA) 

    cv2.putText(blank_image, f"Reconociendo ...", (org[0]-40,org[1]+40), font,  
                   fontScale, (0,0,255), thickness , cv2.LINE_AA) 
    
    if time_elapsed > 1./frame_rate:
        prev_time = time.time()
        im_bw = cv2.resize(roi, img_size, interpolation=cv2.INTER_AREA)
        # ret,binary_image = cv2.threshold(im_bw,thresh,255,cv2.THRESH_BINARY)

        im_bw = im_bw/255
        y_pred = model.predict(im_bw.reshape(1,100,100,1))
        y_pred = uniques[y_pred.argmax(1)]
        print(y_pred)
        print(prev_sign)

        if (y_pred[0] == prev_sign[-1]) and (prev_sign[-1]!='nothing'):
            prev_sign.append(y_pred[0])
        else:
            prev_sign=[y_pred[0]]

        if len(prev_sign) > 3:
            cv2.putText(blank_image, f"{prev_sign[-1]} ?", (org[0],org[1]+80), font,  
                   fontScale, (0,0,255), thickness , cv2.LINE_AA) 
            
        if len(prev_sign) > 10:
            current_word += prev_sign[-1]
            prev_sign = ["nothing"]
    if len(current_word):
        cv2.putText(blank_image, f"Has dicho: {current_word}", (org[0]-80,org[1]+120), font,  
               fontScale, (255,0,0), thickness , cv2.LINE_AA) 
        if (current_word == "KERRY"):
            cv2.putText(blank_image, f"KAVERGA", (org[0]+80,org[1]+150), font,  
               fontScale, (255,0,0), thickness , cv2.LINE_AA) 
        

    cv2.imshow("White Blank", blank_image)    
    if (cv2.waitKey(1) & 0xFF == ord("q")) or (cv2.waitKey(1) == 27):
        break
# close camera
cam.release()
cv2.destroyAllWindows()
