import cv2,threading,time
import numpy as np
import cv2,time
import matplotlib.pyplot as plt



# class SlidingWindow(object):
#       def __init__(self,):
#             self.image=cv2.imread('frams/1672013113.7502463.png')
#             self.slid_h,self.slid_w = 100,100
#             self.im_y,self.im_x,_ = self.image.shape
#             self.im_y,self.im_x = int(np.ceil(self.im_y/self.slid_h)),int(np.ceil(self.im_x/self.slid_w))

#       def Sliding(self,frame):
#             for y in range(0,self.im_y):
#                 if y >= self.slid_h:
#                     y = self.slid_h
#                 for x in range(0,self.im_x):
#                     if x >= self.slid_w:
#                             x = self.slid_w
#                     tx1,ty1,tx2,ty2 = x*self.slid_w,  y*self.slid_h,  self.slid_w*(x+1),  self.slid_h*(y+1)
#                     # print(tx1,ty1,tx2,ty2)
#                     cv2.rectangle(frame,(tx1,ty1),(tx2,ty2), (255, 0, 0), 5)
#                     # cv2.imshow("tmp",cv2.resize(frame,(800,400)))
#                     # if cv2.waitKey(1) & 0xFF == ord('q'):
#                     #     break
#                     # time.sleep(0.5)

#                     # crop_img = self.image[ty1:ty2, tx1:tx2]
#                     # cv2.imshow("cropped", crop_img)
#                     # cv2.waitKey(0)

#             return frame




class videoStream(object):
    def __init__(self,cam_list):
        self.cam_list = cam_list
        self.caps = []
        self.thread = []
        self.font = cv2.FONT_HERSHEY_COMPLEX
        self.detector = {}
                
        # self.slider = SlidingWindow()
        
        for cam in self.cam_list:
            cap = cv2.VideoCapture(cam['path'])
            self.caps.append(cap)
            t1 = threading.Thread(target = self.stream, args =(cap,cam['camId'],))
            t1.start()
            self.thread.append(t1)
        
        for tt in self.thread:
            tt.join()

    def __del__(self):
        for cap in self.caps:
            cap.release()
    
    def drawDetections(self,frame, result):
        for cls, objs in result.items():
            for x1, y1, x2, y2 in objs:
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255))
                cv2.putText(frame, cls, (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), thickness=2)
        return frame

    def stream(self,cap,camName):
        while(cap.isOpened()):
            start_time = time.time()
            ret, frame = cap.read()
            if ret == True:
                cv2.resize(frame,None, fx=0.4, fy=0.4)
                # frame = self.slider.Sliding(frame)
                # frame = self.drawDetections(frame, self.detector[camName].detect(frame, conf=0.1))
                try: 
                    fps = int(1.0 / (time.time() - start_time))
                except:
                    fps = 0
                frame = cv2.putText(frame,'FPS : {} '.format(fps),(50,150),self.font,2,(50,255,100),3)            
                cv2.imshow(camName,cv2.resize(frame,None, fx=0.4, fy=0.4))
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                print('{} Video end'.format(camName))
                break
            
stream = videoStream([{'camId':'Webcam','path':"C:/Users/gokul/Downloads/www.1TamilMV.men - Pattathu Arasan (2022) Tamil HQ HDRip - 1080p - x264 - AAC - 2.5GB - HC-ESub.mkv"}])
