# You may need to run following commands in terminal to get required libraries
# pip install tkinter
# Pip install pytube
# downloading a youtube video needs its link, just paste link in the dialogue box and hit download 
from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('500x300')
root.resizable(0, 0)
root.title("YouTube video downloader")

Label(root, text='Youtube Video Downloader', font='arial 20 bold').pack()

link = StringVar()

Label(root, text='Paste Link Here:', font='arial 15 bold').place(x=160, y=60)
link_enter = Entry(root, width=70, textvariable=link).place(x=32, y=90)


def Downloader():
    url = YouTube(str(link.get()))
    video = url.streams.get_by_itag(22) #use 18 for 360p,use 22 for 720p, use 137 for 1080p
    video.download()
    Label(root, text='DOWNLOADED', font='arial 15').place(x=180, y=210)


Button(root, text='DOWNLOAD', font='arial 15 bold', bg='pale violet red',
       padx=2, command=Downloader).place(x=180, y=150)

root.mainloop()
