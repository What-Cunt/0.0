# 0.0
My name is Cody and this is my first actaul project

# What this project will be
Youtube downloading, and segwaying onto server building; and, for the future, create an automatic scanning app. 

# Notes
#Dash: Dynamic Adaptive Streaming, more preferred than HTTP for Youtube. Higher quality
#Legacy/Progressive: Contains both audio and vidoe and is only 720p and bellow.
##How to convert webm files to Mp3, had the capabilities to convert to FLAC(hi rez audio)
# https://cloudconvert.c/webm-to-mp3

# Playlists weird Functionality (it is all coming together) 
the function to pick which tag/file to download will change what is the steps for choosing.

The get_by_itag lets each individual video choose it's quality, perhaps that functionality is good. However what is also needed to be considered is that the choice is an int and the input() function is what alllows for that choice. I think using the GUI/console to choose is much better. Deleting the int(input()) will allow you to input a tag yourself. The tag will choose the file within the playlist to be downloaded.

# Sending the audios downloaded to a local file. 
from pytube import YouTube
yt = YouTube('https://youtu.be/z15wKo0r-74')
print(yt.title)
stream = yt.streams.get_by_itag(int(input()))
input('enter to continue')
stream.download(output_path='Graduation/', filename='IDo.webm', filename_prefix='dino')