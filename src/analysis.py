import cv2 

def nothing(x):
	pass

cv2.namedWindow('controls')
cv2.createTrackbar('min_t','controls',0,500,nothing)
cv2.createTrackbar('max_t','controls',0,500,nothing)
image = cv2.imread('pothols/1674008954.6817193.png')

while True:
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    min_thres= int(cv2.getTrackbarPos('min_t','controls'))
    max_thres = int(cv2.getTrackbarPos('max_t','controls'))
    ret, thresh = cv2.threshold(img_gray, min_thres, max_thres, cv2.THRESH_BINARY)
    cv2.imshow('Binary image', thresh)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break


# cv2.imwrite('image_thres1.jpg', thresh)
# detect the contours on the binary image using cv2.CHAIN_APPROX_NONE
# contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
                                      
# # draw contours on the original image
# image_copy = image.copy()
# cv2.drawContours(image=image_copy, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
                
# # see the results
# cv2.imshow('None approximation', image_copy)
# cv2.waitKey(0)
# cv2.imwrite('contours_none_image1.jpg', image_copy)
# cv2.destroyAllWindows()

