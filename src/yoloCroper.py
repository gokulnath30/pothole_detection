import cv2,os,time
import xml.etree.ElementTree as ET


imgpath = 'dataset/image/'
xmlpath = 'dataset/xml/'

for xml,img in zip(os.listdir(xmlpath),os.listdir(imgpath)):
    # parse an xml file by name
    tree = ET.parse(xmlpath+xml)
    root = tree.getroot()
    image = cv2.imread(imgpath+img)
    for child in root.findall('object'):
        points = []
        classes = str(child.find('name').text)
        if classes == 'person':
            for val in child.find('bndbox').iter():
                if str(val.tag) != 'bndbox':
                    points.append(str(val.text))
                    # str(val.tag), str(val.text)
            x1,x2,y1,y2 = points

            crop_img = image[int(y1):int(y2),int(x1):int(x2)]
            cv2.imshow("crop_img",crop_img)
            cv2.imwrite('classifications/positive/'+str(time.time())+'.png',crop_img)
            cv2.rectangle(image,(int(x1),int(x2)),(int(y1),int(y2)), (255, 0, 0), 5)
            cv2.imshow("image",cv2.resize(image,(800,400)))
            cv2.waitKey(0)


