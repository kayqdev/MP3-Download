from pytube import YouTube
import os
import shutil

link = input('URL: ')

yt = YouTube(link)

# Escolher a qualidade do audio
audio = yt.streams.filter(only_audio=True).first()

# Iniciar o download
out_file = audio.download()


# renomear para mp3
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)

print("MP3 baixado!")
