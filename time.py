# Import required libraries
from tkinter import *
from time import strftime
import datetime as dt
from PIL import ImageTk, Image

# Create an instance of tkinter window
win = Tk()

# Define the geometry of the window
win.geometry("700x500")

frame = Frame(win, width=600, height=400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("01.jpg"))

# Create a Label Widget to display the text or Image
label = Label(frame, image = img)
label.pack()

  
win.title("Display Current Date")
win.iconbitmap("clock.ico")
win.geometry("700x350")
import datetime
def greeting():
    currentTime = datetime.datetime.now()
    currentTime.hour

    if currentTime.hour < 12:
        label = Label(win, text="Good Morning",font= ('calibri', 40, 'bold'))
        label.pack(pady=20)
    elif 12 <= currentTime.hour < 18:
        label = Label(win, text="Good Afternoon",font= ('calibri', 40, 'bold'))
        label.pack(pady=20)
    else:
        label = Label(win, text="Good Evening",font= ('calibri', 40, 'bold'))
        label.pack(pady=20)


greeting()


date = dt.datetime.now()
# Create Label to display the Date
label1 = Label(win, text=f"{date:%A}", font="Calibri, 20")
label1.pack(pady=20)
label = Label(win, text=f"{date: %B %d, %Y}", font="Calibri, 20")
label.pack(pady=20)

# importing strftime function to
# retrieve system's time
from time import strftime
  
win.title('Clock')
  
# This function is used to 
# display time on the label
def time():
    string = strftime('%H:%M %p ')
    lbl.config(text = string)
    lbl.after(1000, time)
   



# Styling the label widget so that clock
# will look more attractive
lbl = Label(win, font = ('calibri', 40, 'bold'),
            background = 'purple',
            foreground = 'white')
  





# Placing clock at the centre
# of the tkinter window
lbl.pack(anchor = 'center')
time()

  

win.mainloop()