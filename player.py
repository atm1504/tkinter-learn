from tkinter import *
from PIL import ImageTk, Image
import pygame
from tkinter import filedialog


root = Tk()
root.title("Learning Tkinter")
root.iconbitmap("./images/quality.ico")
root.geometry("400x400")

# Initialize Pygame Mixer
pygame.mixer.init()

# Add Song Function
def addSong():
    song = filedialog.askopenfilename(initialdir='audio/', title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"),))
    # print(song)
    song = song.replace("/Users/amartyamondal/Documents/project/tkinter/audio/", "")
    song = song.replace(".mp3", "")
    songBox.insert(END, song)

# Play selected song
def play():
    song = songBox.get(ACTIVE)
    song = f'/Users/amartyamondal/Documents/project/tkinter/audio/{song}.mp3'
    
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

# Stop curentn playing music
def stop():
    pygame.mixer.music.stop(song)
    songBox.selection_clear(loops=0)

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
back_button = Button(controlFrame, image=back_btn_img, borderwidth=0)
forward_button = Button(controlFrame, image=forward_btn_img, borderwidth=0)
play_button = Button(controlFrame, image=play_btn_img, borderwidth=0, command=play)
pause_button = Button(controlFrame, image=pause_btn_img, borderwidth=0)
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


root.mainloop();
