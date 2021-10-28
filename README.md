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

# Aftermath

Maybe I could  make an Eminem reference but nah, already did. Any case I finished with bracnhing adnd all all I have to do is continue the tutorial. Furthermore this would be used for my replit project. I do want to use Visual Studio Code, it is not as easy yet it is not as intense for computational power as Pycharm seems to be. nonetheless the best course is being well-versed in English and Linux. Oh a little boy can dream. 

# Replit and GOOGLE DRIVE and etc. 

It is a possible thing but the thing is being that replit runs on a server that isn't completely connected to the internet. There is a lot of different function that allow it to be but the main thing is that
# google docs (pydrive) is unable to work on replit, unless i figure out making a local server or use an acutal computer there will always be conflict with the code.
However the best thing I can do is download zip files and extract the folder with the music, perhaps a huge amount of music being zipped and a program that decipher that would be best. 

# Make a local IDE (integrated development enviroment)
visual studio code on the internet?