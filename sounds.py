import tkinter as tk
from tkinter import filedialog
import pygame
import os

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("300x400")  # Definindo o tamanho da janela

        pygame.init()
        pygame.mixer.init()

        self.playlist = []
        self.current_track = 0

        self.create_ui()

    def create_ui(self):
        self.playlist_box = tk.Listbox(self.root, selectmode=tk.SINGLE, bg="black", fg="white")
        self.playlist_box.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.add_button = tk.Button(self.root, text="Adicionar Música", command=self.add_music)
        self.add_button.pack()

        self.prev_button = tk.Button(self.root, text="Anterior", command=self.prev_track)
        self.prev_button.pack()

        self.play_button = tk.Button(self.root, text="Play", command=self.play_music)
        self.play_button.pack()

        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_music)
        self.stop_button.pack()

        self.next_button = tk.Button(self.root, text="Próxima", command=self.next_track)
        self.next_button.pack()

    def add_music(self):
        file_path = filedialog.askopenfilename(filetypes=[("Arquivos de Áudio", "*.mp3 *.wav")])
        if file_path:
            self.playlist.append(file_path)
            self.playlist_box.insert(tk.END, os.path.basename(file_path))

    def play_music(self):
        if not pygame.mixer.music.get_busy():
            track = self.playlist[self.current_track]
            pygame.mixer.music.load(track)
            pygame.mixer.music.play()

    def stop_music(self):
        pygame.mixer.music.stop()

    def prev_track(self):
        if self.current_track > 0:
            self.current_track -= 1
            self.play_music()

    def next_track(self):
        if self.current_track < len(self.playlist) - 1:
            self.current_track += 1
            self.play_music()

if __name__ == "__main__":
    root = tk.Tk()
    player = MusicPlayer(root)
    root.mainloop()
