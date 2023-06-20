import pytube

link = input("Enter Link :")
yt = pytube.YouTube(link)
yt.streams.get_highest_resolution().download()
print("Video Downloaded")