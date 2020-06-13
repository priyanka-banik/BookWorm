import tkinter as tk
from tkinter import *
import pyttsx3
from tkinter import messagebox
from tkinter import filedialog
window=tk.Tk()
engine=pyttsx3.init()
window.config(background="#2F4F4F")
window.title("BookWorm")
window.geometry("1300x1300")
window.iconbitmap('logo1.ico')
def browse1():
	file=filedialog.askopenfile()
#login part
engine=pyttsx3.init()
c=Canvas(window,width=220,height=200)
c.pack()
def signup():
	Username.destroy()
	k['text']="Sign up"
	b2.destroy()
def submit1():
   
	mainFrame.destroy()
	engine.say("Hi            To    retrieve    your    older     files   press   Browse   And   to   create    new    files    press    new")
	engine.runAndWait()
	secondframe=LabelFrame(window,bg='#F5FCFF',width=500,height=500)
	secondframe.pack(expand=True,side='right')
	browse=Button(secondframe,text="Browse old files",command=browse1)
	browse.pack()
	New=Button(secondframe,text="New")
	New.pack()
photo=PhotoImage(file=r"Screenshot (580).png")
c.create_image(0,0,image=photo,anchor=NW)
mainFrame=LabelFrame(window,bg='#F5FCFF', width=1000, height=1000)
mainFrame.pack(expand=True,side='right')

k=Label(mainFrame,text="Sign in",font=("Times",25),bg="white",fg="black")
k.pack()

Username=Entry(mainFrame)
Username.insert(0,"Username")
Username.pack()
Email=Entry(mainFrame)
Email.insert(0,"Email ID or Phone no.")
Email.pack()
Password=Entry(mainFrame)
Password.insert(0,"Password")
Password.pack()
b1=Button(mainFrame,text="Submit",command=submit1)
b1.pack()
b2=Button(mainFrame,text="Sign Up",command=signup)
b2.pack() 

window.mainloop()