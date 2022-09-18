import tkinter
#import cv2
#import numpy as np
import wikipedia
from tkinter import *
from functools import partial
from PIL import ImageTk, ImageFont, Image
import PIL
import re
from tkinter import messagebox
import os 
from tkinter import *
from tkvideo import tkvideo
import os
        
def Login():
    #Condition For Password andEmail
    if email.get() != "" and password.get() != "" and e.match(email.get())  :
        messagebox.showinfo("Login Success", "Congratulations For Your Successful Login")
    else:
        messagebox.showinfo("Login error", "*Username and password fields can not be empty Or You have entered a invalid email address*")
    
    global a
    global b
    a=email.get()
    b=password.get()
    print("Email: ",a)
    print("Password: ",b)
    def Information():
        win1.destroy()
        win3=Tk()
        win3.geometry('1190x600')  
        win3.title('Hack The Mountain - Login/Register')
        win3.config(background="lavender")
        win3.resizable(False,False)
        imgl=PIL.Image.open(r"/Users/jahanvisachdeva/Downloads/HTM/welcome.jpeg")
        win3.bg=ImageTk.PhotoImage(imgl)
        win3.bg_image=Label(image=win3.bg).place(x=0,y=0,relwidth=1,relheight=1)

        #Small BG
        win3.Frame_login=Frame(background="white")
        win3.Frame_login.place(x=350,y=150,height=340,width=500)
        imgl1=PIL.Image.open(r"/Users/jahanvisachdeva/Downloads/HTM/bg1.jpg")
        win3.Frame_login.img = ImageTk.PhotoImage(imgl1)
        bg_img=Label(win3.Frame_login,image=win3.Frame_login.img,background="white").place(x=5,y=15)
        
        '''def dictionary():
            win4=Tk()
            win4.geometry('400x150')  
            win4.title('Dictionary')
            info=StringVar()
            infoEntry=Entry(win4, textvariable=info).grid(row=1, column=1)
            print("namaste",info)
            def Wiki():
                #import wikipedia
                #wik=info.get()
                #print("hello")
                print(wikipedia.summary(info.get()))
                #resultwik=wikipedia.summary(wik)
                #Tk.messagebox.showinfo(resultwik)
                #messagebox.showinfo("Dictionary Result",resultwik)

            submit= Button(win4, text="Find", command=Wiki).grid(row=1, column=0)
            Wiki()'''
        #import wikipedia
        def dictionary():
            win4=Tk()
            win4.geometry('400x150')  
            win4.title('Dictionary')
            info=StringVar()
            infoEntry=Entry(win4, textvariable=info).grid(row=1, column=1)
                    
            def Wiki():
                #import wikipedia
                #wik=info.get()
                #print(wikipedia.summary(wik))
                #resultwik=wikipedia.summary(wik)
                #Tk.messagebox.showinfo(resultwik)
                #messagebox.showinfo("Dictionary Result",resultwik)
                #info=StringVar()
                #infoEnty=Entry(win4,textvaribale=info).grid(row=1,column=1)
                #result= wikipedia.summary(info, sentences = 2)
                #print(result)
                
                #import wikipedia
                text=print(wikipedia.summary(info.get()))
                print("Output: \n"+text)

            submit= Button(win4, text="Find", command=Wiki).grid(row=1, column=0)
            Wiki()

        def hologram():
            print("Hologram")
            win5=Tk()
            win5.geometry('400x150')
            win5.title("Hologram Videos")
            #info=StringVar()
            #infoEnty=Entry(win5,textvaribale=info).grid(row=1,column=1)
        
            def brain():
                os.chdir('/Users/jahanvisachdeva/Downloads/HTM/')
                root = Tk()
                my_label = Label(root)
                root.title("Brain Example")
                my_label.pack()
                player = tkvideo("screen-20220916-182043.mp4", my_label, loop = 1, size = (1280,720))
                player.play()

                root.loop()

            def frog():
                os.chdir('/Users/jahanvisachdeva/Downloads/HTM/')
                root = Tk()
                root.title("Frog Example")
                my_label = Label(root)
                my_label.pack()
                player = tkvideo("/Users/jahanvisachdeva/Downloads/HTM/Frog Anatomy - Simulation.mp4", my_label, loop = 1000, size = (1280,720))
                player.play()

                root.loop() 

            submit1 = Button(win5,text="Brain (Example)",command=brain).grid(row=1,column=0)
            submit2 = Button(win5,text="Frog (Example)",command=frog).grid(row=1,column=1)

        '''def profile():
            name01 = "Jahanika"
            email01 = "hackathon@gmail.com"
            insti_name01 = "The NorthCap University"
            print("Name: {}\nEmailID: {}\nInstitution Name: {}".format(name01, email01, insti_name01 ))'''

        def profile():
            win6 = Tk()
            win6.geometry('400x150')
            win6.title("Profile Info")
            name01 = "example"
            email01 = "hackathon@gmail.com"
            insti_name01 = "Example"
            
            text=text.insert("Name: {}\nEmailID: {}\nInstitution Name: {}".format(name01, email01, insti_name01))
            #text.pack()

            l = Label(win6.Profile_Info,text = text.pack(),background="black")
            #l.pack()
            Output=Text(win6.Profile_Info, background="black")
            #Display=Button(win6.Profile_Info,text=)
            #email2Label = Label(win2.Frame_login,font=("Inter",10,"bold"), text="Email*",background = "white", foreground = "#3c3953")
            #Display.pack()
            Output.pack()

            win6.mainloop()

        lg12=PIL.Image.open(r"/Users/jahanvisachdeva/Downloads/HTM/Hologram icon updated.png") #icon holograms
        photo=ImageTk.PhotoImage(lg12)
        lg12_label=Label(win3.Frame_login,image=photo,bg="white")
        lg12_label.image=photo
        loginButton = Button(win3.Frame_login,image=photo,text="HOLOGRAMS",borderwidth=0,command=hologram,bg="white",highlightthickness=0,relief=FLAT)
        loginButton.place(x=30,y=50,height=50,width=50)



        lg13=PIL.Image.open(r"/Users/jahanvisachdeva/Downloads/HTM/Dictionary icon updated.png") #icon dictionary
        photo=ImageTk.PhotoImage(lg13)
        lg13_label=Label(win3.Frame_login,image=photo,bg="white")
        lg13_label.image=photo
        loginButton = Button(win3.Frame_login,image=photo,text="DICTIONARY",borderwidth=0,command=dictionary,bg="white",highlightthickness=0,relief=FLAT)
        loginButton.place(x=30,y=125,height=50,width=50)



        lg14=PIL.Image.open(r"/Users/jahanvisachdeva/Downloads/HTM/Profile icon updated.png") #icon profile
        photo=ImageTk.PhotoImage(lg14)
        lg14_label=Label(win3.Frame_login,image=photo,bg="white")
        lg14_label.image=photo
        loginButton = Button(win3.Frame_login,image=photo,text="PROFILE",borderwidth=0,command=profile,bg="white",highlightthickness=0,relief=FLAT)
        loginButton.place(x=30,y=200,height=50,width=50)
            
        #submit1 = Button(win3,text="Dictionary",command=dictionary).grid(row=1,column=0)
        #submit2 = Button(win3,text="Hologram",command=hologram).grid(row=1,column=1)
        #submit3 = Button(win3,text="Profile",command=profile).grid(row=1,column=2)
        win3.mainloop()
    Information()

def Register():
    #1st BG
    global win2
    win1.destroy()
    win2=Tk()
    win2.geometry('1190x600')  
    win2.title('Hack The Mountain - Login/Register')
    win2.config(background="lavender")
    win2.resizable(False,False)
    img=PIL.Image.open(r"/Users/jahanvisachdeva/Downloads/HTM/welcome.jpeg") #register ICON
    win2.bg=ImageTk.PhotoImage(img)
    win2.bg_image=Label(image=win2.bg).place(x=0,y=0,relwidth=1,relheight=1)
    
    
    #2nd BG
    win2.Frame_login=Frame(background="white")
    win2.Frame_login.place(x=220,y=75,height=440,width=700)
    img1=PIL.Image.open(r"/Users/jahanvisachdeva/Downloads/HTM/welcome.jpeg")  #background
    win2.Frame_login.img = ImageTk.PhotoImage(img1)
    bg_img=Label(win2.Frame_login,image=win2.Frame_login.img).place(x=-2,y=-2)
    
    
    #Email
    email2Label = Label(win2.Frame_login,font=("Inter",10,"bold"), text="Email*",background = "white", foreground = "#3c3953")
    email2Label.place(x=375,y=45)
    email2 = StringVar()
    email2Entry = Entry(win2.Frame_login,bg="white",foreground = "black",highlightthickness=0,font=("Inter",12),relief=FLAT, textvariable=email2)
    email2Entry.place(height=30,width=246,x=375,y=63)
    email_line=Canvas(win2.Frame_login,width=250,height=2.0,bg="black",highlightthickness=0)
    email_line.place(x=377,y=90)
    
    
    #Password- Create
    password2Label = Label(win2.Frame_login,font=("Inter",10,"bold"),text="Create Password* ",background = "white", foreground = "#3c3953")
    password2Label.place(x=375,y=109)  
    password2 = StringVar()
    password2Entry = Entry(win2.Frame_login, bg="white",foreground = "black",highlightthickness=0,font=("Inter",14),relief=FLAT,textvariable=password2, show='*')
    password2Entry.place(height=30,width=246,x=375,y=129)
    password_line=Canvas(win2.Frame_login,width=250,height=2.0,bg="black",highlightthickness=0)
    password_line.place(x=377,y=155)
    
    
    #Password- Confirm
    password3Label = Label(win2.Frame_login,font=("Inter",10,"bold"),text="Confirm Password*",background = "white", foreground = "#3c3953")
    password3Label.place(x=375,y=174)  
    password3 = StringVar()
    password3Entry = Entry(win2.Frame_login, bg="white",foreground = "black",highlightthickness=0,font=("Inter",14),relief=FLAT,textvariable=password3, show='*')
    password3Entry.place(height=30,width=246,x=375,y=194)
    password3_line=Canvas(win2.Frame_login,width=250,height=2.0,bg="black",highlightthickness=0)
    password3_line.place(x=377,y=220)
    
    
    #Name
    nameLabel = Label(win2.Frame_login,font=("Inter",10,"bold"),text="Name*",background = "white", foreground = "#3c3953")
    nameLabel.place(x=375,y=239)  
    name = StringVar()
    nameEntry = Entry(win2.Frame_login, bg="white",foreground = "black",highlightthickness=0,font=("Inter",14),relief=FLAT,textvariable=name)
    nameEntry.place(height=30,width=73,x=375,y=259)
    name_line=Canvas(win2.Frame_login,width=75,height=2.0,bg="black",highlightthickness=0)
    name_line.place(x=377,y=285)
    
    
    #Insitution Name
    insti_nameLabel = Label(win2.Frame_login,font=("Inter",10,"bold"),text="Institution Name*",background = "white", foreground = "#3c3953")
    insti_nameLabel.place(x=463,y=239)  
    insti_name = StringVar()
    insti_nameEntry = Entry(win2.Frame_login, bg="white",foreground = "black",highlightthickness=0,font=("Inter",14),relief=FLAT,textvariable=insti_name)
    insti_nameEntry.place(height=30,width=73,x=463,y=259)
    insti_name_line=Canvas(win2.Frame_login,width=175,height=2.0,bg="black",highlightthickness=0)
    insti_name_line.place(x=465,y=285)
    
    
    #Blah
    blahLabel = Label(win2.Frame_login,font=("Inter",10,"bold"),text="Blah*",background = "white", foreground = "#3c3953")
    blahLabel.place(x=375,y=304)
    blah = StringVar()
    blahEntry = Entry(win2.Frame_login, bg="white",foreground = "black",highlightthickness=0,font=("Inter",14),relief=FLAT,textvariable=blah, show='*')
    blahEntry.place(height=30,width=110,x=375,y=324)
    blah_line=Canvas(win2.Frame_login,width=250,height=2.0,bg="black",highlightthickness=0)
    blah_line.place(x=377,y=350)
    
    #Registeration Success Message
    def RegisterSuccess():
        Tk.messagebox.showinfo("Registeration Successful","Status: Registeration Successful \n *PLease Login To Conitnue*")
    
    #Submit
    sb=Image.open(r"C:\Users\ACER\Desktop\Frame4.png") #submit icon
    photo=ImageTk.PhotoImage(sb)
    sb_label=Label(win2.Frame_login,image=photo,bg="white")
    sb_label.image=photo
    submit= Button(win2.Frame_login, image=photo,text="Submit", borderwidth=0,bg="white",highlightthickness=0,relief=FLAT,command=RegisterSuccess).place(x=405,y=369)
    win2.mainloop()
    

#Bg image
win1=Tk()
win1.geometry('1190x600')  
win1.title('Hack The Mountain - Login/Register')
win1.config(background="lavender")
#win1.resizable(false,false)
img=PIL.Image.open(r"/Users/jahanvisachdeva/Downloads/HTM/welback.jpg") #j1 or a1??? 
win1.bg=ImageTk.PhotoImage(img)
win1.bg_image=Label(image=win1.bg).place(x=0,y=0,relwidth=1,relheight=1)


#Small BG
win1.Frame_login=Frame(background="white")
win1.Frame_login.place(x=350,y=150,height=340,width=500)
img1=PIL.Image.open(r"/Users/jahanvisachdeva/Downloads/HTM/bg1.jpg")
win1.Frame_login.img = ImageTk.PhotoImage(img1)
bg_img=Label(win1.Frame_login,image=win1.Frame_login.img,background="white").place(x=5,y=15)


#Text On Image
win1.Frame_login.txt="Hack The Mountain"
heading=Label(win1.Frame_login,text=win1.Frame_login.txt,foreground = "#3c3953",font=("OCR A Extended",15,"bold"),bg="white").place(width=300,height=30,x=-15,y=250)


#Email
emailLabel = Label(win1.Frame_login,font=("Inter",10,"bold"), text="Username",background = "white", foreground = "#3c3953")
emailLabel.place(x=280,y=93)
email = StringVar()
global e
e= re.compile(r"^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$")
emailEntry = Entry(win1.Frame_login,bg="white",foreground = "black",highlightthickness=0,font=("Inter",12),relief=FLAT, textvariable=email)
emailEntry.place(height=30,width=160,x=284,y=112)
email_line=Canvas(win1.Frame_login,width=200,height=2.0,bg="#3c3953",highlightthickness=0)
email_line.place(x=252,y=137)
email_icon= PIL.Image.open(r"/Users/jahanvisachdeva/Downloads/HTM/i1.png") #profile icon
photo=ImageTk.PhotoImage(email_icon)
email_icon_label=Label(win1.Frame_login,image=photo,bg="white")
email_icon_label.image=photo
email_icon_label.place(x=250,y=112)


#Password
passwordLabel = Label(win1.Frame_login,font=("Inter",10,"bold"),text="Password ",background = "white", foreground = "#3c3953")
passwordLabel.place(x=280,y=157)  
password = StringVar()
passwordEntry = Entry(win1.Frame_login, bg="white",foreground = "black",highlightthickness=0,font=("Inter",14),relief=FLAT,textvariable=password, show='*')
passwordEntry.place(height=30,width=200,x=284,y=175)
password_line=Canvas(win1.Frame_login,width=200,height=2.0,bg="#3c3953",highlightthickness=0)
password_line.place(x=252,y=199)
pss_icon=PIL.Image.open(r"/Users/jahanvisachdeva/Downloads/HTM/i12.png") #password icon
photo=ImageTk.PhotoImage(pss_icon)
pss_icon_label=Label(win1.Frame_login,image=photo,bg="white")
pss_icon_label.image=photo
pss_icon_label.place(x=250,y=175)


#Login
lg=PIL.Image.open(r"/Users/jahanvisachdeva/Downloads/HTM/Frame.png") #login icon
photo=ImageTk.PhotoImage(lg)
lg_label=Label(win1.Frame_login,image=photo,bg="white")
lg_label.image=photo
loginButton = Button(win1.Frame_login,image=photo,text="LOGIN",borderwidth=0,command=Login,bg="white",highlightthickness=0,relief=FLAT)
loginButton.place(x=278,y=215)


#Register
rg=PIL.Image.open(r"/Users/jahanvisachdeva/Downloads/HTM/Frame2.png") #sign up icon
photo=ImageTk.PhotoImage(rg)
rg_label=Label(win1.Frame_login,image=photo,bg="white")
rg_label.image=photo
txt1="Don't have account?"
heading1=Label(win1.Frame_login,text=txt1,foreground = "#3c3953",font=("Inter",8),bg="white").place(x=281,y=255)
registerButton = Button(win1.Frame_login,image=photo,text="Register",borderwidth=0,command=Register,bg="white",highlightthickness=0,relief=FLAT)
registerButton.place(x=385,y=258)


win1.mainloop()