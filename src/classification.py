import numpy as np
import tensorflow as tf
import cv2,os
from pathlib import Path



class Classification(object):
        def __init__(self):
            self.cls = ['Good','Potholes']            
            self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
            self.model_path = 'models/pothole/keras_model.h5'
            self.model = tf.keras.models.load_model(self.model_path)

        def findId(self,img):
            image = cv2.resize(img,(224,224))
            image_array = np.asarray(image)
            normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
            self.data[0] = normalized_image_array
            prediction = self.model.predict(self.data)
            return self.cls[np.argmax(prediction[0], 0)],max(prediction[0])


np.set_printoptions(suppress=True) 
predict = Classification()

path = 'C:/projects/smartathon/polutions/Dataset/pothole/potholes/'
for file in os.listdir(path):
    if Path(file).suffix == '.jpg' or Path(file).suffix == '.png':
        print('Image path : ',path+file)
        img = cv2.imread(path+file)

        pridict_val = predict.findId(img)
        print("{} predicted and accuracy is {} : ".format(pridict_val[0],pridict_val[1]))
        cv2.imshow('img',img)
        cv2.waitKey(0)


