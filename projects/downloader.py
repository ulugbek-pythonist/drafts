from pytube import YouTube
import time

link = input("Linkni kiriting: ")

ytube = YouTube(link)
yuklanvotti = "Yuklanmoqda..."

text = """-------------------------------------
--- Yuqori sifatli (1)
--- Quyi sifatli (2)
--- Ovozli (3)

Qaysi biri: """

papka = "/home/ulugbekpy/github/drafts/projects"

print("-------------------------------")
print("Nomi: ", ytube.title)
print("-------------------------------")
print(ytube.views, " marta ko'rilgan")
print("-------------------------------")
ask = input(
    "Yuklashni boshlaysizmi?\n\
(ha(1)/yo'q(2)): "
)


c = 1

if ask == "1":
    options = input(text)
    if options == "1":
        print(yuklanvotti)
        yuklash1 = ytube.streams.get_highest_resolution()
        start = time.time()
        yuklash1.download(papka)
    elif options == "2":
        yuklash2 = ytube.streams.get_lowest_resolution()
        print(yuklanvotti)
        start = time.time()
        yuklash2.download(papka)
    elif options == "3":
        yuklash3 = ytube.streams.get_audio_only()
        print(yuklanvotti)
        start = time.time()
        yuklash3.download(papka)
    else:
        c = 0
        print("Nimadir xato ketdi..")
else:
    c = 0
    print("-------------------------------")
    print("Xayr, salomat bo'ling!")

stop = time.time()
if c == 1:
    print(f"Yuklash uchun {round(stop - start,2)} soniya vaqt ketdi")
