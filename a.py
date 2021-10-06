from pytube import YouTube 
from pytube import Playlist
##How to convert webm files to Mp3, had the capabilities to convert to FLAC(hi rez audio)
# https://cloudconvert.com/webm-to-mp3
print('hi')
#Basic
yt = YouTube('https://youtu.be/z15wKo0r-74')
print('The title: ', yt.title, "\n")
print('The Url', yt.thumbnail_url, '\n')


#What is there to download
print(yt.streams.filter(progressive=True), '\n')
print(yt.streams.filter(adaptive=True), '\n')
print(yt.streams.filter(only_audio=True), '\n')
print(yt.streams.filter(file_extension='mp4'))
# print(yt.streams.filter(file_extension=''))('wtf is happening dawg???')


p = Playlist('https://youtube.com/playlist?list=PLAUxsgLNM2Bt8apMzywvdzOJSzlfW4OQa')
print(f'Downloading: {p.title}')
for video in p.videos: video.streams.first().download()
#choosing wh file/tag to downloadm = yt.streams.get_by_itag(int(input()))
input('enter to continue')
stream.download()
