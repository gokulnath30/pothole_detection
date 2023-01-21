


f = open("annotation/train/labels/s24efb5c04_png.rf.56e7a618fdc28c010771c5c5a1d70975.txt", "r")
pts = f.read()
pts = pts.split(' ')[1:-1]
for i in pts:
    print(float(i)*100)