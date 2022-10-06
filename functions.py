import cv2
from pyzbar.pyzbar import decode
from mysql.connector import *
import time

global valid_user
valid_user = "http://de.qrwp.org/QR-Code"#http://tiny.cc/pgdn"

m =[]

def attendence():
	l = []
	database = connect(host="localhost",user="root",passwd="root",database="project")
	cursor = database.cursor() 
	cursor.execute("select * from attendence")
	for i in cursor:
		l.append(i)
	return l 
	database.close()

	
def payed_fees():
	qrcodescanner()
	database = connect(host="localhost",user="root",passwd="root",database="project")
	cursor = database.cursor()	
	cursor.execute("update attendence set attendence=0")
	database.commit()
	database.close()


def qrcodescanner():
	breaking = False
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

def attender():
	qrcodescanner()
	database = connect(host="localhost",user="root",passwd="root",database="project")
	cursor = database.cursor() 
	cursor.execute("select * from attendence")
	for i in cursor:
		if i[1] == 0:
			#database = connect(host="localhost",user="root",passwd="root",database="project")
			#cursor = database.cursor()
			cursor.execute("update attendence set Attendence=1 where Day =" + str(i[0]))
			database.commit()
			database.close()
			print(attendence())

