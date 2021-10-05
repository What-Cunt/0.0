from pytube import YouTube 
##How to convert webm files to Mp3, had the capabilities to convert to FLAC(hi rez audio)
# https://cloudconvert.com/webm-to-mp3
yt = YouTube('https://youtu.be/z15wKo0r-74')
print(yt.streams.filter(file_extension=''))
stream = yt.streams.get_by_itag(int(input()))
input('enter to continue')
stream.download()
