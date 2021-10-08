from pytube import YouTube
yt = YouTube('https://youtu.be/z15wKo0r-74')
print(yt.title)
stream = yt.streams.get_by_itag(int(input()))
input('enter to continue')
# stream.download(output_path='Graduation/', filename='IDo.webm', filename_prefix='dino')

