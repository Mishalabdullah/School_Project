def testcode():
        if i[0] == 1:
            if i [1] == 1:
                canvas = Canvas(frm)
                canvas.create_rectangle(50, 50,10, 10, fill="#f50")
                canvas.grid(column=1,row=2)
            else:
                canvas = Canvas(frm)
                canvas.create_rectangle(50, 50,10, 10, fill="#fb0")
                canvas.grid(column=1,row=2)
def colour_box_changer(i):
    canvas = Canvas(frm)
    canvas.create_rectangle(50, 50,10, 10, fill="#f50")
    canvas.grid(column=1,row=2)

# Create two varaibles inside the function one for canvas,row and coloumn
# implement the variables with format()