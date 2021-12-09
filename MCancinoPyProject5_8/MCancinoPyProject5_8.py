#Import Tkinter
import tkinter as tk
import tkinter.font as tkFont

#Create the Tkinter object
app = tk.Tk()
#Set the object size to 640 x 480
app.geometry("640x480")

#Create a font style of your own choice and size
fontStyle = tkFont.Font(family="Lucida Grande", size=35)

#Create a label example with the text “The system is idle.”
idelLabel = tk.Label(app, text="The System is Idle.", font=fontStyle)

def Idle():
    #change label text
    idelLabel.config(text = "The System is Idle.")
    app.configure(bg='grey')

#Create a SystemOn method that change the label example text to “System Running.”
def SystemOn():
    #Change background
    app.configure(bg='green')
    #Change label text
    idelLabel.config(text= "The System is On")

#Create a SystemOff method that change the label example text to “System Off.”
def SystemOff():
    #Change background
    app.configure(bg='red')
    #Change label text
    idelLabel.config(text= "The System is Off")
    #Call Idel rest method after 2 seconds
    app.after(2000, Idle)

#Create a virtual image 1 pixel width x 1 pixel height
pixelVirtual = tk.PhotoImage(width=1, height=1);

#Use the pack attribute to add the label example to the application window
idelLabel.pack(side=tk.TOP)

#Create a button with the text “System On” with a height of 100 and a width of 200
#Use the command attribute to bind the system on button to the SystemOn method
onButton = tk.Button(app, text="System On", bg="green", fg="white", image=pixelVirtual, width=200, height=100, compound="c", command = SystemOn)
#Use the place attribute to set this button at an x value of 100 and a y value of 400
onButton.place(x=100,y=400)

#Create a button with the text “System Off” with a height of 100 and a width of 200
#Use the command attribute to bind the system off button to the SystemOff method
offButton = tk.Button(app, text="System Off", bg="red", fg="white", image=pixelVirtual, width=200, height=100, compound="c", command = SystemOff)
#Use the place attribute to set this button at an x value of 340 and a y value of 400
offButton.place(x=340, y=400)

#Create an Exit button
exitButton = tk.Button(app, text="EXIT", command = app.quit)
#Use the pack attribute to add the exit button to the application window
exitButton.pack(side=tk.RIGHT)

app.mainloop()