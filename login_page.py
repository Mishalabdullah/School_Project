from tkinter import *
root = Tk()
root.title('Codemy.com - Set Image as Background')
#root.iconbitmap('Assests/swimming_bg_1.png')
root.geometry("800x500")

# Define image
bg = PhotoImage(file="Assests\bg.png")

# Create a canvas
my_canvas = Canvas(root, width=800, height=500)
my_canvas.pack(fill="both", expand=True)

# Set image in canvas
my_canvas.create_image(0,0, image=bg, anchor="nw")

# Add a label
my_canvas.create_text(400, 250, text="Welcome!", font=("Helvetica", 50), fill="white")
# add some buttons
button1 = Button(root, text="Start")
button2 = Button(root, text="Reset Scores")
button3 = Button(root, text="Exit")

button1_window = my_canvas.create_window(10, 10, anchor="nw", window=button1)
button2_window = my_canvas.create_window(100, 10, anchor="nw", window=button2)
button3_window = my_canvas.create_window(230, 10, anchor="nw", window=button3)


root.mainloop()
