from pytube import YouTube 
from pytube import Playlist
##How to convert webm files to Mp3, had the capabilities to convert to FLAC(hi rez audio)
# https://cloudconvert.com/webm-to-mp3
print('hi')
p = Playlist('https://youtube.com/playlist?list=PLAUxsgLNM2Bt8apMzywvdzOJSzlfW4OQa')
yt = YouTube('https://youtu.be/z15wKo0r-74')

#Basic
def Basic():
  print('The title: ', yt.title, "\n")
  print('The Url', yt.thumbnail_url, '\n')
  print('The title: ', p.title, "\n")
  print('The Url', p.thumbnail_url, '\n')


#What is there to download
print(yt.streams.filter(progressive=True), '\n')
print(yt.streams.filter(adaptive=True), '\n')
print(yt.streams.filter(only_audio=True), '\n')
# print(yt.streams.filter(file_extension='mp4'))
# print(yt.streams.filter(file_extension=''))('wtf is happening dawg???')

#playlist
print(f'Downloading: {p.title}')
for video in p.videos: video.streams.get_by_itag(int(input())).download()

#choosing which file/tag to download 
stream = yt.streams.get_by_itag(int(input()))
input('enter to continue')
stream.download()