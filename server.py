from flask import Flask,render_template,jsonify,request
from fileinput import filename
import time
from ultralytics import YOLO
import cv2,os,shutil
import numpy as np

app = Flask(__name__)

model = YOLO("weights/v2.pt")
ratio_px_nn = 123/50


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload",methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':  
        f = request.files['files']
        fname = str(time.time())+'.png'
        fpath = 'static/uploads/'+fname
        f.save(fpath)  
        image = cv2.imread(fpath)
        shutil.rmtree('runs/segment')

        results = model.predict(source=image, save=True) 
        # pts = results[0].masks.segments
        pts = results[0].boxes.xyxy
        pts = pts.tolist()
        cfg = results[0].boxes.conf
        cfg = cfg.tolist()
        res = []
        outimg = ''
        tempImg = cv2.imread('runs/segment/predict/'+os.listdir('runs/segment/predict/')[0])
       
        for i,x in enumerate(pts):
            x1,y1,x2,y2 = int(x[0]), int(x[1]), int(x[2]),int(x[3])
            
            width = x2 - x1
            height = y2 - y1
            cx ,cy= int((x1 + x2) / 2),int((y1 + y2) / 2)
            
            depth = cx - x1
            
            w_cm = round(width/ratio_px_nn,2)
            h_cm = round(height/ratio_px_nn,2)
            depth_cm = round(depth/ratio_px_nn,2)
           
            cv2.putText(tempImg,str(w_cm)+' Cm_W',(x1,y1 - 30),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
            cv2.putText(tempImg,str(h_cm)+' Cm_H',(x2,y2 - 30),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
            cv2.putText(tempImg,str(depth_cm)+' Cm_D',(cx,cy - 5),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
            # cv2.rectangle(tempImg, (x1,y1), (x2,y2), (255,0,0), 2)

            cv2.circle(tempImg,(cx, cy),3,(0,255,0), thickness=2)

            res.append({'name':'Pothole '+str(i+1),'width':w_cm,'height':h_cm,'depth':depth_cm,'confidence':round(cfg[i],2)})

        opath = 'static/output/'+fname
        cv2.imwrite(opath,tempImg)
        outimg = opath

        
    return jsonify(res = res,output=outimg)



if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True, host='0.0.0.0')