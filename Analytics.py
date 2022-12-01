from tkinter import *
from  functions  import *
import tkinter.font as font
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt
root = Tk()

frm = ttk.Frame(root, padding=20)
frm.grid()
class database_data_extractor:
    def __init__(self):
        database = connect(host="localhost",user="root",passwd="+7hTnU+Ajaly",database="project")
        cursor = database.cursor()
        cursor.execute("select count( month) from number_of_visites group by month")
        data= cursor.fetchall()
        self.required_data = [i[j] for i in data for j in range(len(i))]
        cursor.execute("select distinct month from number_of_visites")
        data= cursor.fetchall()
        self.month_data= [i[j] for i in data for j in range(len(i))]
        database.close()
    
def class_return():
    return database_data_extractor()

t = class_return()
print(t.required_data)
print(t.month_data)
fig = plt.figure(figsize = (10, 5))
plt.bar(t.month_data,t.required_data, color ='blue',width = 0.4)
plt.xlabel("Month")
plt.ylabel("Number Of Visits")
plt.title("Number Of Times Attended")
least_month=min(t.month_data)
max_month=max(t.month_data)
graph_output=plt.show()
graph_output.grid(column=2,row=2)
plt.xticks(np.arange(least_month, max_month+1, 1))
# select count( month) from number_of_visites group by month; important
bg = ImageTk.PhotoImage(file='Assests/water.jpeg')
my_label = Label(frm,image=bg)
my_label.place(x=0,y=0,relheight=1,relwidth=1 ,bordermode=OUTSIDE)

Label(frm, text="Analytics",font=("Helvetica", 24),bg='#d9ecf0',fg="#000000").grid(column=2, row=0,pady=10)
Label(frm, text="Number Of Visits In A Month",font=("Helvetica", 20),bg='#d9ecf0',fg="#000000").grid(column=2, row=1)
Button(frm, text="Quit", command=root.destroy,font=("times new roman",15),bg="#043565",fg='white').grid(column=2, row=10,padx=55)


root.mainloop()