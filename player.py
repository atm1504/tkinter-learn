from tkinter import *
from PIL import ImageTk, Image
import pygame
from tkinter import filedialog
import time
from mutagen.mp3 import MP3
import tkinter.ttk as ttk


root = Tk()
root.title("Learning Tkinter")
root.iconbitmap("./images/quality.ico")
root.geometry("500x450")

# Initialize Pygame Mixer
pygame.mixer.init()

## Grab song length time
def playTime():
    currentTime = pygame.mixer.music.get_pos() / 1000
    convertedCurrentTime = time.strftime('%H:%M:%S', time.gmtime(currentTime))

    # Get curent p laying song
    # current_one = songBox.curselection()
    song = songBox.get(ACTIVE)
    song = f'/Users/amartyamondal/Documents/project/tkinter/audio/{song}.mp3'
    song_mut = MP3(song)

    global song_length
    song_length=song_mut.info.length
    convertedSongLength = time.strftime('%H:%M:%S', time.gmtime(song_length))

    statusBar.config(text=f'Time Elapsed {convertedCurrentTime} of {convertedSongLength}')
    mySlider.config(value=int(currentTime))

    statusBar.after(1000,playTime)

# Add Song Function
def addSong():
    song = filedialog.askopenfilename(initialdir='audio/', title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"),))
    # print(song)
    song = song.replace("/Users/amartyamondal/Documents/project/tkinter/audio/", "")
    song = song.replace(".mp3", "")
    songBox.insert(END, song)

# Add many songs at a time
def addManySongs():
    songs = filedialog.askopenfilenames(initialdir='audio/', title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"),))
    for song in songs:
        song = song.replace("/Users/amartyamondal/Documents/project/tkinter/audio/", "")
        song = song.replace(".mp3", "")
        songBox.insert(END, song)

# Play selected song
def play():
    song = songBox.get(ACTIVE)
    song = f'/Users/amartyamondal/Documents/project/tkinter/audio/{song}.mp3'
    
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    playTime()

    slider_position = int(song_length)
    mySlider.config(to=slider_position, value=0)

# Stop curentn playing music
def stop():
    pygame.mixer.music.stop()
    songBox.selection_clear(ACTIVE)
    statusBar.config(text="")

# Create Global Pause Variable
global paused
paused = False


def pause(is_paused):
    global paused
    paused = is_paused
    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.pause()
        paused = True
    
def nextSong():
    next_one = songBox.curselection()
    next_one = next_one[0] + 1
    song = songBox.get(next_one)

    song = f'/Users/amartyamondal/Documents/project/tkinter/audio/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    songBox.selection_clear(0, END)
    songBox.activate(next_one)
    songBox.selection_set(next_one, last=None)

def previousSong():
    next_one = songBox.curselection()
    next_one = next_one[0] - 1
    song = songBox.get(next_one)

    song = f'/Users/amartyamondal/Documents/project/tkinter/audio/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    songBox.selection_clear(0, END)
    songBox.activate(next_one)
    songBox.selection_set(next_one, last=None)

# Delete A Song
def delete_song():
	songBox.delete(ANCHOR)
	pygame.mixer.music.stop()

# Delete All Songs from Playlist
def delete_all_songs():
	songBox.delete(0, END)
	pygame.mixer.music.stop()

## Slider function
def slide(x):
    slider_label.config(text=f'{int(mySlider.get())} of {int(song_length)}')

songBox = Listbox(root, bg="black", fg="green", width=60, selectbackground ="gray", selectforeground="black")
songBox.pack(pady=20)

# Create Player  Control Buttons
back_btn_img = PhotoImage(file="images/back50.png")
forward_btn_img = PhotoImage(file="images/forward50.png")
play_btn_img = PhotoImage(file="images/play50.png")
pause_btn_img = PhotoImage(file="images/pause50.png")
stop_btn_img = PhotoImage(file="images/stop50.png")

# Create Player control Frames
controlFrame = Frame(root)
controlFrame.pack()

# Create Player Control Buttons
back_button = Button(controlFrame, image=back_btn_img, borderwidth=0, command=previousSong)
forward_button = Button(controlFrame, image=forward_btn_img, borderwidth=0, command=nextSong)
play_button = Button(controlFrame, image=play_btn_img, borderwidth=0, command=play)
pause_button = Button(controlFrame, image=pause_btn_img, borderwidth=0, command=lambda:pause(paused))
stop_button = Button(controlFrame, image=stop_btn_img, borderwidth=0, command=stop)

back_button.grid(row=0,column=0, padx=10)
forward_button.grid(row=0,column=1, padx=10)
play_button.grid(row=0,column=2, padx=10)
pause_button.grid(row=0,column=3, padx=10)
stop_button.grid(row=0, column=4, padx=10)

# Create Menu
myMenu = Menu(root)
root.config(menu=myMenu)


# Add add Song Menu
addSongMenu = Menu(myMenu)
myMenu.add_cascade(label="Add songs", menu=addSongMenu)
addSongMenu.add_command(label="Add One Song to Playlist", command=addSong)
addSongMenu.add_command(label="Add Many Song to Playlist", command=addManySongs)

# Remove song menu
remove_song_menu = Menu(myMenu)
myMenu.add_cascade(label="Remove Songs", menu=remove_song_menu)
remove_song_menu.add_command(label="Delete A Song From Playlist", command=delete_song)
remove_song_menu.add_command(label="Delete All Songs From Playlist", command=delete_all_songs)

# Create status bar
statusBar = Label(root, text='', bd=1, relief=GROOVE, anchor=E)
statusBar.pack(fill=X, side=BOTTOM, ipady=2)


mySlider = ttk.Scale(root, from_=0, to=100, orient=HORIZONTAL, value=0 , command=slide, length=360)
mySlider.pack(pady=30)

## Temporary slider Labell
slider_label = Label(root, text="0")
slider_label.pack(pady=10)



root.mainloop();
