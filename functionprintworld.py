import cv2
from pyzbar.pyzbar import decode
import time
def qrcodescanner():
	breaking = False
	valid_user = ["http://tiny.cc/pgdn"]
	cap = cv2.VideoCapture(0)
	cap.set(3,650)
	cap.set(4,450)
	camera = True
	while camera == True:
		success, frame = cap.read()
		for i in decode(frame):
			User_Id=i.data.decode('utf-8')
			print(User_Id)
			if User_Id in valid_user:
				time.sleep(3)
				breaking = True
		if breaking == True:
			break
		cv2.imshow('Shool Project', frame)
		cv2.waitKey(1)
qrcodescanner()