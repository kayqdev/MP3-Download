from pytube import YouTube
import os
import shutil

link = input('link: ')

name = input('nome da musica: ')

yt = YouTube(link)

# Escolha a qualidade do áudio
audio = yt.streams.filter(only_audio=True).first()

# Inicie o download
out_file = audio.download()

base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)

shutil.move(f'/storage/emulated/0/{yt.title}.mp3', f'/storage/emulated/0/musicas/{yt.title}.mp3')
