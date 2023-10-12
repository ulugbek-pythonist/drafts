import os
from pytube import YouTube

# from sys import argv

# link = argv[1]
link = input("link: ")
qayerga = input("qayerga yuklaymiz: ")
yt = YouTube(link)
print(f"Title: {yt.title}")

print(f"Views: {yt.views}")


yd = yt.streams.get_highest_resolution()


yd.download(qayerga)

print("Downloading...")
