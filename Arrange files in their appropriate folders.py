from sys import path
from tkinter import *
import os
import shutil

root = Tk()
root.geometry("390x300")
root.config(bg = "lightgrey")

def create(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def move_files(folder_name, files):
    for file in files:
        shutil.move(file, f"{folder_name}/{file}")

def submit():
    if s.get()!="":
        try:
            os.chdir(rf"{s.get()}")
            files = os.listdir()
            # files.remove("Arrange files in Appropriate Folder.py")
            create("Docs")
            create("Images")
            create("Music")
            docsExt = ['.txt','.docx','.pdf']
            imgExt = ['.png','.jpg','.jpeg', '.bmp','.gif']
            musicExt = ['.mp4','.mp3','.wav']
            docs = []
            imgs = []
            musics = []
            for file in files:
                if os.path.splitext(f"{s.get()}/{file}")[1].lower() in docsExt:
                    docs.append(file)
                elif os.path.splitext(f"{s.get()}/{file}")[1].lower() in imgExt:
                    imgs.append(file)
                elif os.path.splitext(f"{s.get()}/{file}")[1].lower() in musicExt:
                    musics.append(file)

            move_files("Docs", docs) 
            move_files("Images", imgs) 
            move_files("Music", musics)        
            s.set("")
            l2.config(text = "Done")
        except Exception as e:
            print(e)

def reset():
    s.set("")

l1 = Label(root, text = "Enter Full Path Of Your Folder: ", font = ("Arial", 15), bg = "lightgrey")
l1.pack(pady = 21)

s = StringVar()
t1 = Entry(root, font = ("Arial", 15), width =30, textvariable = s)
t1.pack(pady = 10)
t1.focus()

b1 = Button(root, text = "Submit", font = ("Arial", 12), command = submit)
b1.place(x = 100, y = 155)
b2 = Button(root, text = "Reset", font = ("Arial", 12), command = reset)
b2.place(x = 221, y  = 155)

l2 = Label(root, text = "Welcomes You", font = ("Arial", 15), bg = "lightgrey")
l2.place(x = 129, y = 225)

root.mainloop()
