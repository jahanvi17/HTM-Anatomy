from tkinter import *
from tkvideo import tkvideo
import os
os.chdir('/Users/jahanvisachdeva/Downloads/HTM/')
root = Tk()
my_label = Label(root)
my_label.pack()
player = tkvideo("screen-20220916-182043.mp4", my_label, loop = 1, size = (1280,720))#(add the directory of the other video/hologram)
player.play()

root.mainloop()