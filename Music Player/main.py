import os
import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player By Umar")
        self.root.geometry("600x400")

        self.playlist = []
        self.current_track = 0

        self.setup_ui()

    def setup_ui(self):
        # Buttons
        self.play_button = tk.Button(self.root, text="Play", command=self.play_music)
        self.play_button.pack(pady=10)

        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_music )
        self.stop_button.pack(pady=10)

        self.next_button = tk.Button(self.root, text="Next", command=self.next_music)
        self.next_button.pack(pady=10)

        self.prev_button = tk.Button(self.root, text="Previous", command=self.prev_music)
        self.prev_button.pack(pady=10)

        self.add_button = tk.Button(self.root, text="Add Song", command=self.add_song)
        self.add_button.pack(pady=10)

        # Song information label
        self.song_label = tk.Label(self.root, text="")
        self.song_label.pack(pady=20)

    def play_music(self):
        if self.playlist:
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.unpause()
            else:
                pygame.mixer.music.load(self.playlist[self.current_track])
                pygame.mixer.music.play()
                self.update_song_label()
        else:
            print("Playlist is empty. Add songs before playing.")

    def stop_music(self):
        pygame.mixer.music.stop()

    def next_music(self):
        self.current_track = (self.current_track + 1) % len(self.playlist)
        self.play_music()

    def prev_music(self):
        self.current_track = (self.current_track - 1) % len(self.playlist)
        self.play_music()

    def add_song(self):
        song_path = filedialog.askopenfilename(filetypes=[("song", "*.mp3")])
        if song_path:
            self.playlist.append(song_path)
            self.update_song_label()

    def update_song_label(self):
        if self.playlist:
            song_name = os.path.basename(self.playlist[self.current_track])
            self.song_label.config(text=song_name)
        else:
            self.song_label.config(text="No song in playlist")

if __name__ == "__main__":
    root = tk.Tk()
    pygame.mixer.init()
    music_player = MusicPlayer(root)
    root.mainloop()
