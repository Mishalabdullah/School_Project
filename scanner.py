import cv2
from pyzbar.pyzbar import decode
from mysql.connector import *
import time


def attendence():
	database = connect(host="localhost",user="root",passwd="root",database="project")
	cursor = database.cursor()
	cursor.execute("insert into attendence values(2,0);")
	cursor.execute("select * from attendence ;")
	for i in cursor:
		print(i)


def qrcodescanner():
	breaking = False
	valid_user = ["http://tiny.cc/pgdn"]
	cap = cv2.VideoCapture(0)
	cap.set(3,650)
	cap.set(4,450)
	camera = True
	while camera == True:
		success, frame = cap.read()
		cv2.imshow('Shool Project', frame)
		cv2.waitKey(1)
		for i in decode(frame):
			User_Id=i.data.decode('utf-8')
			print(User_Id)
			if User_Id in valid_user:
				time.sleep(2)
				camera = False
				cv2.destroyAllWindows()
	
