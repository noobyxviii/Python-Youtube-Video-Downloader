from pytube import pytube

url = "" #url

my_vid = YouTube(url)

print(my_vid.title)

my_video = my_video.stream.get_highest_resolution()
my_video.download()
