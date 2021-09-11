from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

folder_name = ""
def Folder_Save():
    global folder_name
    folder_name = filedialog.askdirectory()
def DownloadVideo():
    choice = ytdchoices.get()
    url = ytdEntry.get()
    if(len(url)>1):
        ytdmess.config(text = "")
        yt = YouTube(url)
        
        if(choice == choices[0]):
            select = yt.streams.filter(progressive = True).first()
        elif(choice == choices[1]):
            select = yt.streams.filter(progressive = True,file_extension = 'mp4').last()
        elif(choice == choices[2]):
            select = yt.streams.filter(only_audio = True).first()
        else:
            ytdEmess.config(text = "Paste Link again!!", fg = "red")
            
    select.download(folder_name)
    ytdmess.config(text = "Download Completed")

Win = Tk()
Win.title("YouTube Downloader")
Win.geometry("350x200")
Win.columnconfigure(0, weight = 1)

ytdLabel = Label(Win, text = "Enter the URL of the video", font = ("jost", 15))
ytdLabel.grid()

ytdEntryVar = StringVar()

ytdEntry = Entry(Win, width = 50, textvariable = ytdEntryVar)
ytdEntry.grid()

saveEntry = Button(Win, width = 10, bg = "yellow", fg = "green", text = "Chose Path", command = Folder_Save)
saveEntry.grid()


ytdQuality = Label(Win, text = "Select Quality", font = ("jost", 15))
ytdQuality.grid()

choices = ["720p", "144p", "only Audio"]
ytdchoices = ttk.Combobox(Win, values = choices)
ytdchoices.grid()

downloadbtn = Button(Win, text = "Download", width = 10, bg = "yellow", fg = "green", command = DownloadVideo)
downloadbtn.grid()

ytdmess = Label(Win, text = "-"*90, fg = "green", font = ("jost", 10))
ytdmess.grid()

ytdmess = Label(Win, text = "YouTube: Nga it", fg = "green", font = ("jost", 10))
ytdmess.grid()

Win.mainloop()
