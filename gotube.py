from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube #pip install pytube3

root = Tk()
root.title("YTD Downloader")
root.geometry("350x400") #set window
root.columnconfigure(0,weight=1)#set all content in center.

#Ytd Link Label
ytdLabel = Label(root,text="Enter the URL of the Video",font=("jost",15))
ytdLabel.grid()

#Entry Box
ytdEntryVar = StringVar()
ytdEntry = Entry(root,width=50,textvariable=ytdEntryVar)
ytdEntry.grid()

#Error Msg
ytdError = Label(root,text="Error Msg",fg="red",font=("jost",10))
ytdError.grid()

#Asking save file label
saveLabel = Label(root,text="Save the Video File",font=("jost",15,"bold"))
saveLabel.grid()

#btn of save file
saveEntry = Button(root,width=10,bg="red",fg="white",text="Choose Path")
saveEntry.grid()

#Error Msg location
locationError = Label(root,text="Error Msg of Path",fg="red",font=("jost",10))
locationError.grid()

#Download Quality
ytdQuality = Label(root,text="Select Quality",font=("jost",15))
ytdQuality.grid()

#combobox
choices = ["720p","144p","Only Audio"]
ytdchoices = ttk.Combobox(root,values=choices)
ytdchoices.grid()

#donwload btn
downloadbtn = Button(root,text="Donwload",width=10,bg="red",fg="white")
downloadbtn.grid()

#developer Label
developerlabel = Label(root,text="NP Developer",font=("jost",15))
developerlabel.grid()
root.mainloop()
