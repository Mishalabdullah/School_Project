import cv2
from pyzbar.pyzbar import decode
from mysql.connector import *
import time

global valid_user
valid_user = "http://tiny.cc/pgdn"
  
def attendence():
	database = connect(host="localhost",user="root",passwd="root",database="school")
	cursor = database.cursor() 
	'''cursor.execute("update attendence set Attendence=1")
	cursor.execute("select * from attendence")
	for i in cursor:
		print(i)
		# changing the code from here not resemble my own local database'''
				

def payed_fees():
	database = connect(host="localhost",user="root",passwd="root",database="EXAM")
	cursor = database.cursor()	
	cursor.execute("update attendence set Attendence=0 where Day=0;")
	
		

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
attendence()
