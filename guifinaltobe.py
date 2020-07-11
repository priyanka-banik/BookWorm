import tkinter as tk
from tkinter import *
import pyttsx3
import webbrowser
from pygame import mixer
from tkinter import messagebox
from tkinter import filedialog
import tkinter.font as font
import os
from wand.image import Image as wi
import pytesseract
from gtts import gTTS
import platform
import glob
from googletrans import Translator
from PIL import Image,ImageTk
translator=Translator()

root=tk.Tk()
root.geometry("1550x1550")
engine = pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
canvas=Canvas(root,width=850,height=900,bg='black',relief="raised")
listt = []
framez = tk.Frame(canvas, width=30, height=8, bg='black')
framez.config( width=1,height=8 )
listForLanguage = Listbox(framez,bg="black",fg="white",width=20,height=5)

mixer.init()

#root.resizable(0,0)
root.iconbitmap('logo1.ico')
root.title("BookWorm")
#root.geometry("500x500")
sidebar = LabelFrame(root, width=100, relief='sunken', borderwidth=2, bg="black")
Label(sidebar, text="About us:", bg="black",fg="white").pack()
Label(sidebar, bg="black",fg="white",font=("Century Gothic",9),text="We here understand that studies can be really tough\n at times.Going through several materials,watching\nYouTube videos,but still being unable to learn the\nconcepts.But don't loose hope.We here make learning\nway easier and fun.You can read the audiobooks and\nask questions whenever you feel find something confusing.").pack()
sidebar.pack(expand=True, side='left', anchor='nw',ipady=500)

canvas.pack(ipadx=105)
load = Image.open("book4.jpg")
load= load.resize((1050, 650), Image.ANTIALIAS)
render = ImageTk.PhotoImage(load)
canvas.create_image(0,0,image=render,anchor=NW)
#eer = Label(canvas2, text="“Change is the end result of all true learning.” ― Leo Buscaglia", bg="black", fg="white")
#eer.pack()
load1 = Image.open("image.png")
load1= load1.resize((180, 180), Image.ANTIALIAS)
render1 = ImageTk.PhotoImage(load1)
#render1.resize((250, 250), Image.ANTIALIAS) ## The (250, 250) is (height, width)

canvas.create_image(0,10,image=render1,anchor=NW)
canvas.create_text(330,100,text="                                                           “Change is the end result of all true learning.” \n                                                                                                                                                  ― Leo Buscaglia",font=("Cooper Black",15),fill="#F22F25")

framez3= tk.Frame(canvas, width=100, height=100, bg='black')
listbox = Listbox(framez3,background="black",fg="white")
listbox.config(width=20,height=7)


def play_music():
	try:
		paused
	except NameError:
		try:
			selected = listbox.curselection()
			selected = int(selected[0])
			# print(listt)
			play_it = listt[selected]
			# print(type(listt[0]))
			print(play_it)
			mixer.music.load(play_it)
			mixer.music.play()
		except:
			tkinter.messagebox.showerror('File not found','Audio is not present')
	else:
		mixer.music.unpause()

#def pause_music():
#	global paused
#	paused=True
#	mixer.music.pause()
def stop_music():
	mixer.music.stop()

def set_vol(val):
	volume = int(val) / 100
	mixer.music.set_volume(volume)


def browse1():
	global sett
	global file_path
	canvas.create_window((100, 350), window=framez, anchor=SE)

	file_path = filedialog.askopenfilename()
	print(file_path + "1")
	# listbox.pack()
	sett = True
	if len(listt) != 0:
		sett = False

	# mixer.music.load(file_path)
	# mixer.music.play()
	# print(file_path)
	playlist(str(file_path), sett)


# login part
import speech_recognition as sr

r = sr.Recognizer()
voice_data = 0
from time import ctime


def record_voice(ask=False):
	with sr.Microphone() as source:
		if ask:
			alexis_speak(ask)
		audio = r.listen(source)
		try:
			voice_data = r.recognize_google(audio)
		except sr.UnknownValueError:
			alexis_speak('Sorry,I did not get that')
		except sr.RequestError:
			alexis_speak('Sorry my bad')
	return voice_data


def alexis_speak(audio_string):
	engine = pyttsx3.init()
	engine.say(audio_string)
	engine.runAndWait()


def ask_question():
	vdata = record_voice()
	if 'what is your name' in vdata:
		alexis_speak('Hey       I am your BookWorm guide   Alexis')
	if 'what time is it' in vdata:
		alexis_speak(ctime())
	if 'search' in vdata:
		search = record_voice('What do you want to search for?')
		url = 'https://google.com/search?q=' + search
		webbrowser.get().open(url)
		alexis_speak('Here is what I found for' + search)
	if 'find location' in vdata:
		find = record_voice('What is the location?')
		url = 'https://google.nl/maps/place/' + find + '/&amp; '
		webbrowser.get().open(url)
		alexis_speak('Here is what I found for' + find)


def playlist(filename, sett):
	filename = os.path.basename(filename)
	if file_path == '':
		messagebox.showinfo("Oops", "You did'nt select the file")
	else:
		index = 0
		# print(filename)
		listbox.insert(index, filename)
		canvas.create_window((100, 500), window=framez3, anchor=SE)

		listbox.pack()
		listt.insert(index, file_path)
		print(file_path)
		# print(listt[index])
		index += 1
		playButton = Button(framez3, text="PLAY", command=play_music, bg="black", width=16, fg="white")
		#canvas.create_window((200, 500), window=framez3, anchor=CENTER)
		#playButton.pack()
		#pauseButton = Button(framez3, text="Pause", command=pause_music, bg="black", width=16, fg="white")
		# canvas.create_window((200, 500), window=framez3, anchor=CENTER)
		#stopButton.pack()
		stopButton=Button(framez3,text="Stop",command=stop_music,bg="black",width=16,fg="white")
		askButton = Button(framez3, text="Ask your doubts", command=ask_question,bg="black",width=16,fg="white")

		#addButton = Button(framez3, text="Add more audio", command=add_music, bg="black", width=16, fg="white")
		# canvas.create_window((200, 500), window=framez3, anchor=CENTER)
		#addButton.pack()

		scale = Scale(framez3, from_=0, to=100, orient=HORIZONTAL, command=set_vol, bg='black', fg="white", width=18)
		# canvas.create_window((200, 500), window=framez3, anchor=CENTER)
		canvas.create_window((230, 490), window=framez3, anchor=CENTER)

		if sett == True:
			canvas.create_window((230, 490), window=framez3, anchor=NE)
			playButton.pack()
			#canvas.create_window((200, 500), window=framez3, anchor=CENTER)
			#pauseButton.pack()
			stopButton.pack()
			#canvas.create_window((200, 500), window=framez3, anchor=CENTER)
			askButton.pack()
			#canvas.create_window((200, 500), window=framez3, anchor=CENTER)
			scale.pack()
			canvas.create_window((230, 490), window=framez3, anchor=CENTER)

			sett = False

def download_pdf():
	url = 'https://www.google.com/webhp?hl=en&sa=X&ved=0ahUKEwjvjMvt-ZbqAhUsyDgGHa9KB4sQPAgH'
	webbrowser.open_new(url)


def download_tess():
	url1 = 'https://github.com/tesseract-ocr/tesseract/wiki/Downloads'
	webbrowser.open_new(url1)


def know_more():
	new = 2
	url2 = "file:///C:/Users/BHAIRAB%20DAS/Documents/Project/ALERT-/cssblog.html"  # add the local url address from you machine from the browser
	webbrowser.open(url2, new=new)

frame9=Frame(sidebar,bg='black')
Label(frame9, text="To download tesseract",font=("Century Gothic",13), bg="black", fg="WHITE").pack(side=LEFT)
but5 = Button(frame9, text="Download\n Tesseract\n from here",fg="blue",bg="black", command=download_tess)
but5.pack(side=RIGHT)
frame9.pack(side=BOTTOM)

frame8=Frame(sidebar,bg='black')
Label(frame8, text="To search for materials from internet",font=("Century Gothic",13), bg="black", fg="white").pack(side=LEFT)
but3 = Button(frame8, text="click here", bg="black",fg="blue" ,command=download_pdf)
but3.pack(side=RIGHT)
frame8.pack(side=BOTTOM)


frame=Frame(sidebar,bg='#7E7877')
but1 = Button(frame, text="click here", bg="black", fg="BLUE", command=know_more)
but1.pack(side=RIGHT)
Label(frame, text="To know how to use our platform",font=("Century Gothic",13), bg="black", fg="WHITE").pack(side=LEFT)
frame.pack(side=BOTTOM)

# mainFrame=LabelFrame(window,bg='#F5FCFF', width=1000, height=1000)
# ainFrame.pack(expand=True,side='right')
"""
def browse_convert():
	global file_path1
	file_path1 = filedialog.askopenfile()
"""

def convert(): # the code for pdf conversion
	filename = filedialog.askopenfilename()
	# print(filename)
	head_tail = os.path.split(filename)
	base = os.path.basename(filename)
	opp = os.path.splitext(base)[0]
	pdf = wi(filename=head_tail[1], resolution=300)
	pdfimage = pdf.convert("jpeg")
	i = 1
	for img in pdfimage.sequence:
		page = wi(image=img)
		page.save(filename=opp + str(i) + ".jpg")
		i += 1

	os_1 = platform.system()
	my_c = []
	if os_1 == "Windows 8.1":
		my_c = []
		print(my_c)
	my_c.append(glob.glob("C:/*/*/tesseract.exe"))
	print(my_c)
	if len(my_c) == None:
		my_c.append(glob.glob("E:/*/*/tesseract.exe"))
		if len(my_c) == None:
			my_c.append(glob.glob("F:/*/*/tesseract.exe"))
		if len(my_c) == None:
			my_c.append(glob.glob("D:/*/*/tesseract.exe"))
	elif os_1 == "Linux":
		my_c = []
	my_c.append(glob.glob("Home:/*/*/tesseract.exe"))

	# HERE ADD THE CONDITION IF THE SYSTEM IS MAC OS (ASK FOR THE TESSERACT FILE FROM USER)
	
	path_name = my_c[0]
	pytesseract.pytesseract.tesseract_cmd = path_name
	j = 1
	dir_name = str(head_tail[0] + str("/"))
	mytext = ""

	while j < i:
		file_name = opp + str(j) + ".jpg"
		mytext += pytesseract.image_to_string(dir_name + file_name)
		j = j + 1
	print("ki in convert=" + ki)
	if ki == "English":
		tts1=translator.translate(mytext,dest='en').text
		tts = gTTS(text=tts1, lang='en')
	elif ki == "Hindi":
		tts1=translator.translate(mytext,dest='hi').text
		tts = gTTS(text=tts1, lang='hi')
	elif ki == "Assamese":
		tts1=translator.translate(mytext,dest='as').text
		tts = gTTS(text=tts1, lang='as')
	elif ki == "Bengali":
		tts1=translator.translate(mytext,dest='bn').text
		tts = gTTS(text=tts1, lang='bn')

	tts.save(opp + ".mp3")

	# play the audio file in the default music player of the system
	value = os.path.isfile(head_tail[0] + "/" + os.path.splitext(base)[0] + ".mp3")
	print(type(value))
	if value == True:
		print("PDF IS SUCCESSFULLY CONVERTED")
		messagebox.showinfo("MESSAGE", "PDF IS SUCCESSFULLY CONVERTED\n GO TO BROWSE FILE BUTTON TO PLAY YOUR AUDIOBOOK")

	elif value == False:
		print("OPPS!!! PDF CANNOT BE CONVERTED")
		messagebox.showinfo("MESSAGE", "OPPS!!! PDF CANNOT BE CONVERTED")



def next_step():
	global ki
	ki = listForLanguage.get(listForLanguage.curselection()) # the language in which audio need to be made

	listForLanguage.destroy()

	but12.destroy()
	# but11 = Button(window, text="Browse", command=browse_convert)
	# but11.pack()
	framez7 = tk.Frame(canvas, width=50, height=50, bg='black')
   # canvas.create_window((200, 500), window=framez3, anchor=CENTER)

	but13 = Button(framez7, bg='#41536D', fg='white', text="CONVERT", font=("Forte", 10), command=convert, height=6,width=13)
	canvas.create_window((450, 300), window=framez7, anchor=CENTER)

	but13.pack()

	print(ki)



but12 = Button(framez,text="submit", command=next_step,width=17,bg="black",fg="white")


def create():
	listForLanguage.insert(0, "Hindi")
	listForLanguage.insert(1, "English")
	listForLanguage.insert(2, "Bengali")

	canvas.create_window((500, 350), window=framez, anchor=SE)

	listForLanguage.pack()

	but12.pack()



engine.say(
	"Hi            To    retrieve    your    older     files   press   Browse   And   to   create    new    files    press    new")
engine.runAndWait()


framez1 = tk.Frame(canvas, width=80, height=80,bg='black')
#but12 = Button(framez1,text="submit", command=next_step)
#but12.pack()
b1 = Button( framez1,text="Browse\nOld\nFiles", bg="#41536D",fg='white',font=("Forte",13),relief="raised",command=browse1,width=10,height=4)
canvas.create_window((100,300), window=framez1,anchor=CENTER )
#canvas.create_window((500,100), window=b1,anchor=CENTER )
b1.pack()

framez2=tk.Frame(canvas, width=80, height=80,bg='black')
b2 = Button(framez2,bg='#41536D',fg='white' ,text="Create\nA\nNew\nAudiobook",font=("Forte",13), command=create,width=10,height=4)
canvas.create_window((220,300), window=framez2,anchor=CENTER )
b2.pack()

root.mainloop()
