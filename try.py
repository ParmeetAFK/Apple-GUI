from tkinter import *
from tkinter import filedialog
import os

username = os.getlogin()

# ----------------- FUNCTIONS -------------------------------

def ofile():
	global path
	get_file = filedialog.askopenfilename(initialdir=r"C:\Users\{username}\Documents\Downloads",title="Select",filetypes=(('Images',"*.png"),('Images',"*.jpg"),('Images',"*.jpeg"),("All Files","")))
	path = str(get_file)
	return path

def mainapp(path):
	print(path)

# ------------------------------- ROOT INIT ---------------------------
root = Tk()
root.title("Apple Power")
root.config(bg="#f8f8f8")

#--------------------- HEADING BOX ---------------------------

head = Canvas(root, height=50,width=400,bg="#f8f8f8")
head.grid(row=0,column=0,padx=8,pady=8,columnspan=2)


#----------------------- App BOX --------------------------

app = Frame(root, height=200,width=200,bg="#f8f8f8")
app.grid(row=1,column=0,padx=8,pady=8)


#----------------------- Background BOX --------------------------

back = Canvas(root, height=200,width=200,bg="#f8f8f8",relief='ridge',bd=0, highlightthickness=0)
back.grid(row=1,column=1,padx=8,pady=8)

#----------------------- HEADING Cotent --------------------
#----------------------- LOGO -------------------------
app_logo = PhotoImage(file=r"C:\Users\Parme\Desktop\Apple_8_Bit.png").zoom(3,3)
head.create_image(15,3, anchor=NW, image=app_logo)

#-----------------------  NAME OF APP -------------------------

Label(head, text="APPLE DOCTOR",
			fg='#000',
			bg="#f8f8f8",
			font=('Fugaz One',20)).grid(row=0,column=1,padx=100,pady=8)

#------------------------ APPlication Content ---------------------------------
#----------------------- Image Open Label & Button ----------------------------

Button(app,
      text="Please Select a File",
      bg='#f8f8f8',
      fg='#000',
      font=('Arial Bold',10),
      relief='ridge',
      bd=5,
      command=ofile #ofile is Function declared in FUNCTION SECTION
      ).grid(row=0,
      		 column=0,
      		 padx=8,
      		 pady=8)

Label(app,
	  text="Is Your Apple Healthy ?",
      bg='#f8f8f8',
      fg='#000',
      font=('Arial Bold',10),
      ).grid(row=1,
      		 column=0,
      		 padx=8,
      		 pady=8)

Button(app,
      text="Lets Check",
      bg='#f8f8f8',
      fg='#000',
      font=('Arial Bold',10),
      relief='ridge',
      bd=5,
      command=lambda: mainapp(path) #mainapp is Function which will call your ML program
      ).grid(row=2,
      		 column=0,
      		 padx=8,
      		 pady=8)

#----------------------- BACKGROUND IMAGE --------------------

bg_img = PhotoImage(file=r"C:\Users\Parme\Desktop\fiber-apple.png")
back.create_image(1,3, anchor=NW, image=bg_img)

root.mainloop()