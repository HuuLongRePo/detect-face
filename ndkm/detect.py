from tkinter import *
from PIL import Image,ImageTk
parent = Tk()

  
parent.geometry("400x400")
  
# Add image file
# bg = PhotoImage(file = "D:\\ndkm\\pyauto\\ndkm\\bg-image.jpg")


bg = Image.open("D:\\ndkm\\pyauto\\ndkm\\bg-image.jpg")
bg = bg.resize((400, 400))
bg = ImageTk.PhotoImage(bg)

label1 = Label( parent, image = bg)
label1.place(x = 0, y = 0)  

# Create Canvas
# canvas1 = Canvas( parent, width = 400, height = 400)
# canvas1.pack(fill = "both", expand = True)
  
# Display image
# canvas1.create_image( 0, 0, image = bg, anchor = "nw")

# Create Frame
frame1 = Frame(parent)
frame1.pack(pady = 80 )
# parent.wm_attributes("-transparentcolor", 'grey')

newbutton = Button(frame1,height = 3, 
          width = 15, text = "New User", fg = "green")
newbutton.pack(side = TOP)

trainbutton = Button(frame1,height = 3, 
          width = 15, text = "Training Data", fg = "blue")
trainbutton.pack(side = TOP)

detectbutton = Button(frame1,height = 3, 
          width = 15, text = "Detect Face", fg = "green")
detectbutton.pack(side = TOP)

checkbutton = Button(frame1,height = 3, 
          width = 15, text = "Check Camera", fg = "black")
checkbutton.pack(side = TOP)
parent.mainloop()