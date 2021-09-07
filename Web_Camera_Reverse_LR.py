import cv2
 
cam = cv2.VideoCapture(0)
cam.set(3,3840) #CV_CAP_PROP_FRAME_WIDTH
cam.set(4,2400) #CV_CAP_PROP_FRAME_HEIGHT
cam.set(cv2.CAP_PROP_AUTOFOCUS, 0)
 
while True:
    ret_val, img = cam.read() # 캠 이미지 불러오기
 
    cv2.imshow("Cam Viewer",img) # 불러온 이미지 출력하기
    if cv2.waitKey(1) == 27:
        break
