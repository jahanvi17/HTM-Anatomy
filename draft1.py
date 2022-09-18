
import tkinter
from tkinter import *
from functools import partial


def Login(email,password):
    global a
    global b
    a=email.get()
    b=password.get()
    print("Email / Username: ",a)
    print("Password: ",b)
    def Information():
        win1.destroy()
        win3=Tk()
        win3.geometry('400x150')  
        win3.title('Hack The Mountain - Information')
        def dictionary():
            info=StringVar()
            infoEntry=Entry(win3, textvariable=info).grid(row=0, column=1)
            import wikipedia
            text=print(wikipedia.summary(info.get()))
            print("Output: \n"+text)
        def hologram():
            print("Hologram")
        def profile():
            print("Profile")
            #submit= Button(win3, text="Find", command=Wiki).grid(row=2, column=0)
        def videos():
            print("Videos")
        submit1 = Button(win3,text="Dictionary",command=dictionary).grid(row=1,column=0)
        submit2 = Button(win3,text="Hologram",command=hologram).grid(row=1,column=1)
        submit3 = Button(win3,text="Profile",command=profile).grid(row=1,column=2)
        submit4 = Button(win3,text="Self Paced Videos", command=videos).grid(row=1,column=3)
        #submit5 = Button(win3, text="Submit", command=Dictionary.Wiki).grid(row=1, column=2)
        win3.mainloop()
    Information()
        


def Register():
    global win2
    win1.destroy()
    win2=Tk()
    win2.geometry('400x150')  
    win2.title('Hack The Mountain - Login/Register')
    emailLabel2 = Label(win2, text="Email").grid(row=0, column=0)
    email2 = StringVar()
    emailEntry2 = Entry(win2, textvariable=email2).grid(row=0, column=1)  
    passwordLabel2 = Label(win2,text="Password").grid(row=1, column=0)  
    password2 = StringVar()
    passwordEntry2 = Entry(win2, textvariable=password2, show='*').grid(row=1, column=1)
    nameLabel = Label(win2,text="Name").grid(row=2, column=0)
    name=StringVar()
    nameEntry = Entry(win2, textvariable=name).grid(row=2, column=1)
    roll_noLabel = Label(win2,text="Roll Number").grid(row=3, column=0)
    roll_no=StringVar()
    roll_noEntry = Entry(win2, textvariable=roll_no).grid(row=3, column=1)
    def RegisterSuccess():
        tkinter.messagebox.showinfo("Registeration Successful","Status: Registeration Successful \n *PLease Login To Conitnue*")
    submit= Button(win2, text="Submit", command=RegisterSuccess).grid(row=4, column=0)
    win2.mainloop()

win1=Tk()
win1.geometry('400x150')  
win1.title('Hack The Mountain - Login/Register')
emailLabel = Label(win1, text="Email").grid(row=0, column=0)
email = StringVar()
emailEntry = Entry(win1, textvariable=email).grid(row=0, column=1)  
passwordLabel = Label(win1,text="Password").grid(row=1, column=0)  
password = StringVar()
passwordEntry = Entry(win1, textvariable=password, show='*').grid(row=1, column=1)
Login = partial(Login,email, password)
loginButton = Button(win1, text="Login", command=Login).grid(row=4, column=0)
registerButton = Button(win1,text="Register",command=Register).grid(row=5,column=0)
win1.mainloop()