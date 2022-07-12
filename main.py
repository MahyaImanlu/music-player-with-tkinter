
import tkinter
from tkinter import *
import pygame
from pygame import mixer
from tkinter import filedialog

Music = Tk()
Music.title('MUSIC_PLAYER')
Music.geometry("770x330")
frame1 = Frame(Music, highlightbackground="#808080")
frame2 = Frame(Music, highlightbackground="#808080")


def menu():
    music = filedialog.askopenfilenames()
    for music in music:
        if music:
            play = open(music, 'r')
            print(play.read)
        else:
            show = 'chose a file'
            label1.config(text=show)
        song_playlist.insert(END, music)


def play_pause():
    try:
        music = song_playlist.get(ACTIVE)
        mixer.init()
        s = mixer.music.get_pos()

        if s == -1:
                pygame.mixer.music.load(song_playlist.get(tkinter.ACTIVE))
                pygame.mixer.music.play()
        elif mixer.music.get_busy():
            mixer.music.pause()
        else:
            mixer.music.unpause()
    except:
        show = 'chose a file or enter time'
        label1.config(text=show)


def repeat():
    music = song_playlist.get(ACTIVE)
    mixer.init()
    if mixer.music.get_busy():
        if music:
            pygame.mixer.music.load(music)
            pygame.mixer.music.play()


def next():   # (first choose a song from playlist then push the 'Next' button)
    try:
        Next_music = song_playlist.curselection()
        for i in Next_music:
            i += 1
            music = song_playlist.get(i)
            pygame.mixer.music.load(music)
            pygame.mixer.music.play()
            song_playlist.selection_clear(0, END)
            song_playlist.activate(i)
            song_playlist.selection_set(i)

    except pygame.error:
        song_playlist.selection_clear(0, END)
        song_playlist.selection_set(0, 0)
        pygame.mixer.music.load(song_playlist.get(0))
        pygame.mixer.music.play()



lst = []
def go():
    try:
        if mixer.music.get_busy():
            s1 = Time.get()
            if s1:
                position = pygame.mixer.music.get_pos() / 1000
                current_time = (position + int(s1))
                lst.append(current_time)
                s = sum(lst)
                pygame.mixer.music.set_pos(int(s))
            else:
                position = pygame.mixer.music.get_pos() / 1000
                current_time = (position + 15)
                lst.append(current_time)
                s = sum(lst)
                pygame.mixer.music.set_pos(int(s))
    except:
        show = 'chose a file or enter time'
        label1.config(text=show)


def back():
    try:
        if mixer.music.get_busy():
            s1 = Time.get()
            if s1:
                position = pygame.mixer.music.get_pos() / 1000
                current_time = (position - int(s1))
                lst.append(current_time)
                s = sum(lst)
                pygame.mixer.music.play(loops=0, start=s)
            else:
                position = pygame.mixer.music.get_pos() / 1000
                current_time = (position - 15)
                lst.append(current_time)
                s = sum(lst)
                pygame.mixer.music.play(loops=0, start=s)
    except:
        show = 'chose a file or enter time'
        label1.config(text=show)

'-----------------------------------------------------------------------------------------------------------------------'

songs = LabelFrame(frame2, text="songs",  bg="#C0C0C0", font=('arial', 9), height=100, width=200)
songs.grid(row=15, column=3, columnspan=1,padx=30, pady=1)

song_playlist = tkinter.Listbox(songs, bg="#B2FF63", font=('arial', 9), selectmode=SINGLE, height=10, width=50)
song_playlist.grid(row=0, column=1)
song_playlist.pack(fill=BOTH)

'-----------------------------------------------------------------------------------------------------------------------'

label1 = Label(frame1, fg='#000000', width=20, bd=3, font=('arial', 12))
label1.grid(row=13, column=3, sticky=E, columnspan=1, padx=20)

Time = Entry(frame1, bg="#B2FF63", width=40)
Time.grid(row=9, column=3, sticky=E, columnspan=1, padx=1, pady=1)
Label(frame1, text="inter time", bg='#E5FFCC', padx=1, pady=1, fg='#336600', font=('arial', 10)).grid(row=9, column=2, sticky=E)

Speed = Entry(frame1, bg="#B2FF63", width=40)
Speed.grid(row=8, column=3, sticky=E, columnspan=1, padx=1, pady=1)
Label(frame1, text="inter %", bg='#E5FFCC', padx=1, pady=1, fg='#336600', font=('arial', 10)).grid(row=8, column=2, sticky=E)

Button(frame1, text="<<", bg="#4C9900", fg='#000000', width=20, bd=3,
           font=('arial', 9), command=back).grid(row=9, column=1, sticky=E, columnspan=1, padx=30, pady=1)

Button(frame1, text=">>", bg="#4C9900", fg='#000000', width=20, bd=3,
           font=('arial', 9), command=go).grid(row=9, column=4, sticky=E,columnspan=1, padx=30, pady=1)

Button(frame1, text="Play/pause", bg="#4C9900", fg='#000000', width=20, bd=3,
           font=('arial', 9), command=play_pause).grid(row=13, column=1, sticky=E, columnspan=1, padx=30, pady=1)

menu = Button(frame1, text="menu", bg="#4C9900", fg='#000000', width=20, bd=3, font=('arial', 9), command=menu)
menu.grid(row=12, column=1, sticky=E, columnspan=1, padx=30, pady=1)

Button(frame1, text="Next", bg="#4C9900", fg='#000000', width=20, bd=3,
           font=('arial', 9), command=next).grid(row=13, column=4, sticky=E, columnspan=1, padx=30, pady=1)

Button(frame1, text="repeat", bg="#4C9900", fg='#000000', width=20, bd=3,
           font=('arial', 9), command=repeat).grid(row=12, column=4, sticky=E, columnspan=1,padx=30, pady=1)

Label(frame1, bg="#4C9900", fg='#000000', width=20, bd=3,
           font=('arial', 9)).grid(row=8, column=1, sticky=E, columnspan=1, padx=30, pady=1)

Button(frame1, text="speed", bg="#4C9900", fg='#000000', width=20, bd=3,
           font=('arial', 9)).grid(row=8, column=4, sticky=E, columnspan=1, padx=30, pady=1)


frame1.grid(padx=20)
frame2.grid(padx=20)

Music.mainloop()


