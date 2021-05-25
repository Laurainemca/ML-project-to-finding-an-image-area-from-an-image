import cv2
import numpy as np
main_img=cv2.imread('fruit.PNG',cv2.IMREAD_UNCHANGED)
img=cv2.imread('new.PNG',cv2.IMREAD_UNCHANGED)
result=cv2.matchTemplate(main_img,img,cv2.TM_CCOEFF_NORMED)

min_val,max_val,min_loc,max_loc=cv2.minMaxLoc(result)
threshold =0.8
if max_val>=threshold:
    print("found")
    img_w=img.shape[1]
    img_h=img.shape[0]
    
    top_left=max_loc
    bottom_right=(top_left[0]+img_w,top_left[1]+img_h)
    cv2.rectangle(main_img,top_left,bottom_right,color=(0,255,0),thickness=2,lineType=cv2.LINE_4)
    cv2.imshow('result',main_img)
    cv2.waitKey()
else:
    print("not found")

