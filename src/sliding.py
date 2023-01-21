import numpy as np
import cv2,os,time



def Sliding(imgpath):
      image=cv2.imread(imgpath)
      slid_h,slid_w = 650,350
      im_y,im_x,_ = image.shape
      im_y,im_x = int(np.ceil(im_y/slid_h)),int(np.ceil(im_x/slid_w))
      for y in range(0,im_y):
            if y >= slid_h:
                  y = slid_h
            for x in range(0,im_x):
                  if x >= slid_w:
                        x = slid_w
                  tx1,ty1,tx2,ty2 = x*slid_w,  y*slid_h,  slid_w*(x+1),  slid_h*(y+1)
                  # print(tx1,ty1,tx2,ty2)
                  # cv2.rectangle(image,(tx1,ty1),(tx2,ty2), (255, 0, 0), 5)
                  # cv2.imshow("tmp",cv2.resize(image,(800,400)))
                  # cv2.waitKey(0)
                  # time.sleep(0.5)

                  crop_img = image[ty1:ty2, tx1:tx2]
                  # cv2.imshow("cropped", crop_img)
                  # cv2.waitKey(0)

                  cv2.imwrite('classifications/negative/'+str(time.time())+'.png',crop_img)   
                   

negative = 'dataset/negative/'
for img in os.listdir(negative):
      if img.split('.')[1] == 'jpg':
            Sliding(negative+img)
            print('classifications/negative/'+str(time.time())+'.png')
             
      

