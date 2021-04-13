from tkinter import * 
from tkinter.ttk import *
import tkinter.font as font
import pytube
from pytube import YouTube
from tkinter import messagebox

def download():
    link =  video_Link.get()
      
    yt = YouTube(link)


    
#Getting the highest resolution possible
    ys = yt.streams.get_highest_resolution()

#Starting download
    messagebox.askquestion("Download Video","Are you sure you want to download?")
    ys.download()
    messagebox.showinfo("Download Information","Download completed!!")
  
# creates a Tk() object
master = Tk()
master.title("YouTube Video Downloader")
master.resizable(0,0)
master.configure(bg='pink')

  
# sets the geometry of main 
# root window

master.geometry("800x500")

myFont = font.Font(family='Helvetica', size=24, weight='bold')
greeting =Label(text="YouTube Video Downloader",foreground="blue",background="pink")
greeting['font'] = myFont
greeting.pack()

myFont1 = font.Font(family='Helvetica', size=18, weight='bold')
link=Label(text="Enter The URL",foreground="black",background="pink")

link['font'] =myFont1

link.pack(pady=40,padx=190)
video_Link = StringVar()
myFont2 = font.Font(family='Helvetica', size=14)
linkText = Entry(master,width=50,textvariable=video_Link)
linkText['font']=myFont2
linkText.pack(pady=1)

myFont3= font.Font(family='Helvetica', size=14)
Download_B = Button(master,text="Download",width=30,command=download)

Download_B.pack(pady=10)


master.mainloop()