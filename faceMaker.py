from distutils.command.clean import clean
import tkinter
from tkinter import *
from PIL import Image, ImageTk
import threading
from client import *

client = Client()
obj = {
        'happy': Image.open('./emotion emoji/happy.png'),
        'sad' : Image.open('./emotion emoji/sad.png'),
        'neutral' : Image.open('./emotion emoji/neutral.png')
    }
def pathMaker(emo):
    emoInStr = str(emo)
    path = "./emotion emoji/" + emoInStr + ".png"
    return path

root = Tk()
       
start = Image.open('./emotion emoji/start.png')
test = ImageTk.PhotoImage(start)

label1 = tkinter.Label(root,image=test)
label1.image = test

label1.place(x=200, y=200,anchor="center")
        

root.geometry("400x400")
    

prevEmo = 'empty'
currentEmo = 'sad'
def threadFunc():
    prev = 'prev'
    currentEmotion = 'empty'
    while True:
        currentEmotion = client.recieve()
        if prev != currentEmotion:
            image =  Image.open(pathMaker(currentEmotion))
            newTest = ImageTk.PhotoImage(image)
            label1.config(image=newTest)
            prev = currentEmotion

thread = threading.Thread(target=threadFunc)


thread.start()
root.mainloop()


