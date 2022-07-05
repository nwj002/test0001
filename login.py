from tkinter import*

login_window= Tk()
blank_space = " "
login_window.title("JABS-CALENDER")
login_window.configure(bg='#800000')
login_window.iconbitmap("calender.ico")

theme_font =('Arial',12,)

#FRAME ONE 
window_frame = LabelFrame(login_window,text=24*blank_space+"SIGN IN TO",font=("Helvetica",12,"bold"), padx=25, pady=10, borderwidth=0,bg='#CCCCCC',)
window_frame.pack(padx=60, pady=100,)

heading = Label(window_frame, text="JABS CALENDER",font=("Helvetica",20,"bold"), bg="#CCCCCC", fg="blue", ).grid(row=0, column=0, columnspan=3, ipady=25)

Username = Label(window_frame, text="Username",font=theme_font,bg='#CCCCCC', ).grid(row=1, column=0,columnspan=3)
password = Label(window_frame, text="Password", font=theme_font,bg='#CCCCCC').grid(row=3, column=0,columnspan=3,)


username_entry = Entry(window_frame, relief=FLAT,font=theme_font).grid(row=2, column=0, padx=20,columnspan=3)
password_entry = Entry(window_frame, show="*",relief=FLAT,font=theme_font).grid(row=4, column=0, padx=20 ,columnspan=3) 


login_button = Button(window_frame, text="LOG IN", font=theme_font,relief=FLAT,).grid(row=5, column=0, pady=10,columnspan=3, )


no_account= Label(window_frame, text="Don't have an account?",bg='#CCCCCC',font=theme_font).grid(row=6, column=0, columnspan=3)
newaccount = Button(window_frame, text="CREATE AN NEW ACCOUNT",relief=FLAT, bg="#CCCCCC",font=('Arial',9,'underline', ), fg="dark green").grid(row=7, column=0, columnspan=3,)

print("hello")

window_frame.mainloop()
