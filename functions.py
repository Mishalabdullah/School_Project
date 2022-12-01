import cv2
from pyzbar.pyzbar import decode
from mysql.connector import *
from datetime import date
from tkinter import *
from tkinter import ttk


global valid_user
valid_user = "persuader storage repressed dawdler unearned eardrum groom polyester savings hazelnut ventricle resume"
repay_user = "poncho paralegal stellar parkway rectify landfall primal drizzle slate timothy circular trident"

m =[]

def login_check():
	l = []
	database = connect(host="localhost",user="root",passwd="+7hTnU+Ajaly",database="project")
	cursor = database.cursor()
	cursor.execute("select * from login")
	for i in cursor:
		l.append(i)
	return l
	database.close()
	

def attendence():
	l = []
	todays_date = date.today()
	month= todays_date.month
	database = connect(host="localhost",user="root",passwd="+7hTnU+Ajaly",database="project")
	cursor = database.cursor() 
	cursor.execute("select * from attendence")
	database.close()
	database = connect(host="localhost",user="root",passwd="+7hTnU+Ajaly",database="project")
	cursor = database.cursor() 
	cursor.execute("insert into number_of_visites values("+str(month)+")")
	database.commit()
	for i in cursor:
		l.append(i)
	return l 


	
def payed_fees():
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
			if User_Id in repay_user:
				time.sleep(2)
				camera = False
				cv2.destroyAllWindows()
	database = connect(host="localhost",user="root",passwd="+7hTnU+Ajaly",database="project")
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
	database = connect(host="localhost",user="root",passwd="+7hTnU+Ajaly",database="project")
	cursor = database.cursor() 
	cursor.execute("select * from attendence")
	for i in cursor:
		if i[1] == 0:
			database = connect(host="localhost",user="root",passwd="+7hTnU+Ajaly",database="project")
			cursor = database.cursor()
			cursor.execute("update attendence set Attendence=1 where Day =" + str(i[0]))
			database.commit()
			database.close()
			print(attendence())
attendence()

