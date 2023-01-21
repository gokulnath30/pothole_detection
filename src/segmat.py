from ultralytics import YOLO
import cv2,os
import numpy as np


model = YOLO("seg.pt")  # load a custom model
# path = 'dataset/combain/balaji/'
# for img in os.listdir(path):
path = 'dataset/combain/balaji/s2bfb78e2a.png'
image = cv2.imread(path)
# results = model(path)  # predict on an image
results = model.predict(source=image, save=True,)
# pts = results[0].masks.segments
pts = results[0].boxes.xyxy
pts = pts.tolist()
print(pts)
# print(polygons.points)
# print(polygons.segmentation)
# h,w,_=image.shape
# for xx in ploy:
#     for yy in xx:
#         print(yy[0],yy[1])

# image = cv2.polylines(image, [pts],True, (255, 0, 0), 2)

# print(,'--------------------------------')

# 1080 1920
for x in pts:
    x1,y1,x2,y2 = int(x[0]), int(x[1]), int(x[2]),int(x[3])

    
    width = x2 - x1
    height = y2 - y1
    cx ,cy= int((x1 + x2) / 2),int((y1 + y2) / 2)
    
    ratio_px_nn = 150/50
    w_cm = round(width/ratio_px_nn,2)
    h_cm = round(height/ratio_px_nn,2)

    

    cv2.putText(image,'Width '+str(w_cm)+' Cm',(x1,y1 - 10),cv2.FONT_HERSHEY_COMPLEX,1,(25,15,220),2)
    cv2.putText(image,'height '+str(h_cm)+' Cm',(x2,y2 - 10),cv2.FONT_HERSHEY_COMPLEX,1,(25,15,220),2)
    cv2.rectangle(image, (x1,y1), (x2,y2), (255,0,0), 2)

    cv2.circle(image,(cx, cy),3,(0,0,255), thickness=2)



cv2.imwrite('pts.png',image)
    
