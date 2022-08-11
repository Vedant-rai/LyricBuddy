import requests, json
from tkinter import *
import tkinter.messagebox as tkmb
from tkmacosx import Button
def extract():
    global song, artist
    song_name = song.get()
    artist_name = artist.get()
    url = 'https://api.lyrics.ovh/v1/'+artist_name+'/'+song_name
    response = requests.get(url)
    json_data = json.loads(response.text)
    try:
        lyric = json_data['lyrics']
        print(lyric)
        tkmb.showinfo(message='Done')
    except:
        tkmb.showerror(message='No such song found')

root = Tk()
root.title("Lyrics Extractor")
root.geometry("550x210")
Label(root, text='Song Lyrics Extractor', font=("Comic Sans MS", 18, 'bold')).pack(side=TOP,fill=X)
song = StringVar()
artist = StringVar()
e1 = Entry(root, width=50, textvariable=song).place(x=64, y=50)
e2 = Entry(root, width=50, textvariable=artist).place(x=64, y=100)
l1 = Label(root, text="SONG:", font=("Comic Sans MS", 13)).place(x=0, y=50)
l2 = Label(root, text="ARTIST:", font=("Comic Sans MS", 13)).place(x=0, y=100)
button_extract = Button(root, text="DOWNLOAD", padx=30, pady=10,bg="grey",fg="white", command=extract).place(x=185, y=150)
root.mainloop()
