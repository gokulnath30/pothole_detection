import cv2,os,time
import xml.etree.ElementTree as ET
from shapely.geometry import Polygon,Point,box

def intersect(box1, box2):
    x1, y1, x2, y2 = box1
    a1, b1, a2, b2 = box2
    p1 = Polygon([(x1, y1), (x2, y1), (x2, y2), (x1, y2)])
    p2 = Polygon([(a1, b1), (a2, b1), (a2, b2), (a1, b2)])
    flag_1 = p1.intersects(p2)
    ox, oy = (a1 + a2) // 2, (b1 + b2) // 2
    obj_centroid = Point(ox, oy)
    area_coords = box(x1, y1, x2, y2)
    flag_2 = obj_centroid.within(area_coords)

    if flag_1 and flag_2:
        return True
    return False



imgpath = 'annotation/image/'
xmlpath = 'annotation/xml/'
sarea = [0,620,1920,1080]

# for xml in os.listdir(xmlpath):
# parse an xml file by name
tree = ET.parse('annotation/xml/0250.xml')
root = tree.getroot()
# print(root.find('filename').text,'===')
image = cv2.imread('annotation/image/'+root.find('filename').text)
imgCopy = image.copy()
cv2.rectangle(image,(sarea[0],sarea[1]),(sarea[2],sarea[3]), (0, 255, 0), 2)
for child in root.findall('object'):
    points = []
    classes = str(child.find('name').text)
    for val in child.find('bndbox').iter():
        if str(val.tag) != 'bndbox':
            points.append(int(val.text))
            # str(val.tag), str(val.text)
          
    if intersect(sarea, points):  
        x1,x2,y1,y2 = points

        crop_img = imgCopy[x2:y2,x1:y1]
        # cv2.imshow("crop_img",crop_img)
        # cv2.waitKey(0)

        # cv2.imwrite('pothols/'+str(time.time())+'.png',crop_img)
        cv2.rectangle(image,(x1,x2),(y1,y2), (0, 0, 255), 2)

cv2.imshow("image",cv2.resize(image, (0,0), fx=0.50, fy=0.50))
cv2.waitKey(0)


