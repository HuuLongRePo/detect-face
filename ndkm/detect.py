from tkinter import *
from PIL import Image,ImageTk
import subprocess
from pathlib import Path

parent = Tk()

def get_project_root() -> Path:
    return Path(__file__).parent.parent
  
parent.geometry("400x400")
pathroot = str(get_project_root())
# Add image file
bg = Image.open(pathroot+"/ndkm/bg-image.jpg")
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
          width = 15, text = "New User", fg = "green",command=lambda:subprocess.Popen(args=['python3', r''+pathroot+'/ndkm/getdataSQL.py']))
newbutton.pack(side = TOP)

trainbutton = Button(frame1,height = 3, 
          width = 15, text = "Training Data", fg = "blue",command=lambda:subprocess.Popen(args=['python3', r''+pathroot+'/ndkm/TrainData.py']))
trainbutton.pack(side = TOP)

detectbutton = Button(frame1,height = 3, 
          width = 15, text = "Detect Face", fg = "green", command=lambda:subprocess.Popen(args=['python3', r''+pathroot+'/ndkm/RecongintionData.py']))
detectbutton.pack(side = TOP)

checkbutton = Button(frame1,height = 3, 
          width = 15, text = "Check Camera", fg = "black",command=lambda:subprocess.Popen(args=['python3', r''+pathroot+'/ndkm/getDataWC.py']))
checkbutton.pack(side = TOP)
parent.mainloop()