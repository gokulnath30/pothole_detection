import torch,os,cv2

# model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # or yolov5m, yolov5l, yolov5x, etc.
model = torch.hub.load('ultralytics/yolov5', 'custom', 'best.pt')  # custom trained model


negative = 'dataset/Scene 1/'
for image in os.listdir(negative):
    img = negative+image
    # imgs = cv2.imread(img)
    results = model(img)
    print(results[0])
    # for pts in  results.xyxy[0].tolist():
    #     x1,y1,x2,y2,cfg,clss = pts
    #     # print(x1,x2,y1,y2,cfg,clss)
    #     if cfg > 0.6:
    #         # cv2.rectangle(imgs, (int(x1), int(y1)), (int(x2), int(y2)), (255,0,0), 2)

    #         crop_img = imgs[int(y1):int(y2), int(x1):int(x2)]
    #         # edge = cv2.Canny(crop_img, 50,150)
    #         cv2.imshow("img",cv2.resize(crop_img,(600,500)))
    #         if cv2.waitKey(0) & 0xFF == ord('q'):
    #             break