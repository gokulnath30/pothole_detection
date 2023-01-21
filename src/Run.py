import os,cv2 
import numpy as np


negative = 'dataset/Scene 1/'
for image in os.listdir(negative):

    img = cv2.imread(negative+image,0)
    kernel = np.ones((5,5),np.float32)/25  
    blur = cv2.bilateralFilter(img,9,75,75)  

    edge = cv2.Canny(image, 150, 200)
    # out = cv2.hconcat([image, edge]) 

    # # Apply kernel for embossing
    # emboss_kernel = np.array([[-1, 0, 0],
    #                 [0, 0, 0],
    #                 [0, 0, 1]])

    # emboss_img = cv2.filter2D(src=image, ddepth=-5, kernel=emboss_kernel)

    cv2.imshow("img",cv2.resize(edge,(1080,600)))
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break
