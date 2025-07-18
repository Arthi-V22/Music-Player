
import tkinter as tk
from tkinter import filedialog
import pygame
import os

pygame.mixer.init()

class MusicPlayer:
    def __init__(self, root):  
        self.root = root
        self.root.title("🎵 Python Music Player")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        self.current_song = ""

        self.song_label = tk.Label(root, text="No song selected", font=("Arial", 12), fg="blue")
        self.song_label.pack(pady=20)

        tk.Button(root, text="Select Song", width=20, command=self.load_song).pack(pady=5)
        tk.Button(root, text="Play", width=20, command=self.play_music).pack(pady=5)
        tk.Button(root, text="Pause", width=20, command=self.pause_music).pack(pady=5)
        tk.Button(root, text="Resume", width=20, command=self.resume_music).pack(pady=5)
        tk.Button(root, text="Stop", width=20, command=self.stop_music).pack(pady=5)

    def load_song(self):
        self.current_song = r"C:\Users\arthi\Downloads\MP3 files.mp3"
        song_name = os.path.basename(self.current_song)
        self.song_label.config(text=f"🎶 Now Playing: {song_name}")
        pygame.mixer.music.load(self.current_song)

    def play_music(self):
        if self.current_song:
            pygame.mixer.music.play()

    def pause_music(self):
        pygame.mixer.music.pause()

    def resume_music(self):
        pygame.mixer.music.unpause()

    def stop_music(self):
        pygame.mixer.music.stop()

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()
