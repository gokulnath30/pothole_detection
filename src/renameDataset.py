import cv2,os,time,uuid
import shutil

pth = 'dataset/Scene 1/'
for img in os.listdir(pth):
	if img != 'sections.mov':
		id = str(uuid.uuid4())
		ids = id.split('-')[0]
		print(pth+img,'dataset/combain/s1'+ids+'.png','............')
		shutil.copyfile(pth+img,'dataset/combain/s1'+ids+'.png')
