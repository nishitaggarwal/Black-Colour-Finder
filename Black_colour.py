#%%

import cv2
# import time
import numpy as np

# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# output_file = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

cap = cv2.VideoCapture(0)
image = cv2.imread("nishit.jpg")
bg = 0
# for i in range(60):
#     ret,bg = cap.read()
 
# bg = np.flip(bg,axis = 1)

while (cap.isOpened()):
    ret,img = cap.read()
    # if not ret:
    #     break
    # img = np.flip(img,axis = 1)
    frame = cv2.resize(img,(640,480))
    image = cv2.resize(image,(640,480))


    # hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    l_black = np.array([30,30,0])
    u_black = np.array([104,153,70])
    
    mask_1 = cv2.inRange(frame,l_black,u_black)

    res = cv2.bitwise_and(frame, frame, mask = mask_1)
    
    fe = frame - res
    f = np.where(fe == 0, image, fe)
    cv2.imshow("video",frame)
    cv2.imshow("mask", f)

    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()

# %%
