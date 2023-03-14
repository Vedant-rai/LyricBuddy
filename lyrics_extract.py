import requests, json
from tkinter import *
import tkinter.messagebox as tkmb
from tkmacosx import Button
def extract():
    global song, artist
    song_name = song.get()
    artist_name = artist.get()
    api_key = 'f67fce6ee1f286b31b362709285703eb'
    endpoint = f"http://api.musixmatch.com/ws/1.1/track.search?q_track={song_name}&q_artist={artist_name}&apikey={api_key}"
    response = requests.get(endpoint)
    json_data = response.json()

    try:
    # Extract the track ID from the response JSON
        track_id = json_data["message"]["body"]["track_list"][0]["track"]["track_id"]
    
    # Define the API endpoint for getting the lyrics
        endpoint = f"http://api.musixmatch.com/ws/1.1/track.lyrics.get?track_id={track_id}&apikey={api_key}"
    
    # Send a request to the API endpoint and get the response
        response = requests.get(endpoint)

    # Parse the response JSON to get the lyrics
        json_data = response.json()
        
        # Extract the lyrics from the response JSON
        lyrics = json_data["message"]["body"]["lyrics"]["lyrics_body"]

        # Print the lyrics
        print(lyrics)
        tkmb.showinfo(message='Done')
    except:
        tkmb.showerror(message='No such song found')

root = Tk()
root.title("Lyrics Extractor")
root.geometry("550x210")
Label(root, text='Song Lyrics Extractor', font=("Times New Roman", 18, 'bold')).pack(side=TOP,fill=X)
song = StringVar()
artist = StringVar()
e1 = Entry(root, width=50, textvariable=song).place(x=64, y=50)
e2 = Entry(root, width=50, textvariable=artist).place(x=64, y=100)
l1 = Label(root, text="SONG:", font=("Comic Sans MS", 13)).place(x=0, y=50)
l2 = Label(root, text="ARTIST:", font=("Comic Sans MS", 13)).place(x=0, y=100)
button_extract = Button(root, text="DOWNLOAD", padx=30, pady=10,bg="grey",fg="white", command=extract).place(x=185, y=150)
root.mainloop()
