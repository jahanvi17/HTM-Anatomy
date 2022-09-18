import wikipedia
import tkinter as Tk
from tkinter import *
import functools

def dictionary():
    win4=Tk()
    win4.geometry('400x150')  
    win4.title('Dictionary')
    info=input()
    infoEntry=Entry(win4, textvariable=info).grid(row=1, column=1)
            
    def Wiki():
        #import wikipedia
        #wik=info.get()
        #print(wikipedia.summary(wik))
        #resultwik=wikipedia.summary(wik)
        #Tk.messagebox.showinfo(resultwik)
        #messagebox.showinfo("Dictionary Result",resultwik)
        result= wikipedia.summary(info, sentences = 2)
        print(result)

    submit= Button(win4, text="Find", command=Wiki).grid(row=1, column=0)
    Wiki()