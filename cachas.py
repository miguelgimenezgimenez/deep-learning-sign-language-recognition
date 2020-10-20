import cv2
# from imageai import Detection
modelpath = "models/yolo.h5"
# yolo = Detection.ObjectDetection()
# yolo.setModelTypeAsYOLOv3()
# yolo.setModelPath(modelpath)
# yolo.loadModel()

cam = cv2.VideoCapture(0)  # 0=front-cam, 1=back-cam
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1300)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1500)

font = cv2.FONT_HERSHEY_SIMPLEX 
org = (150, 90) 
fontScale = 1
thickness = 2
color = (255, 0, 0) 
while True:
    im = cv2.imread("data/asl_alphabet_test/A_test.jpg")
    cv2.imshow("image",im)

    # ret, frame = cam.read()
    # def ROI():
     

      
#     # Line thickness of 2 px 
#     grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     cv2.putText(frame, 'El cachas', org, font,  
#                    fontScale, (0, 255, 0), thickness , cv2.LINE_AA) 
#     cv2.putText(frame, 'PELIGRO: te da por culo cuando te agachas', (0, 540) , font,  
#                    fontScale, (0, 0, 255), thickness , cv2.LINE_AA) 
   
#     # (thresh, blackAndWhiteFrame) = cv2.threshold(grayFrame, 127, 255, cv2.THRESH_BINARY)



#     roi = grayFrame[100:500, 100:500]

#     cv2.rectangle(frame, (100, 100), (500, 500), (0, 255, 0), 2)
#     cv2.imshow("ROI",roi)
#     cv2.imshow('Video', frame)
    # cv2.waitKey(0)

    if (cv2.waitKey(1) & 0xFF == ord("q")) or (cv2.waitKey(1) == 27):
        break
# # close camera
# cam.release()
# cv2.destroyAllWindows()
