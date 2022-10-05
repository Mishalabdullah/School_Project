from mysql.connector import *
try:
    database = connect(host="localhost",user="root",passwd="root",database="projet")
    cursor = database.cursor()
except:
    database_user = input("Enter Your Username For The Database:")
    database_passwd=input("Enter Your Passphrase For The Database:")
    database = connect(host="localhost",user=database_user,passwd=database_passwd)
    cursor = database.cursor()
    cursor.execute("create database project")
    cursor.execute("use project")
    cursor.execute("create table attendence (day int(31) primary key, attendence int(1) ")
    for i in range (1,19):
        cursor.execute("inset into attendence vales("+ i +",0)")
