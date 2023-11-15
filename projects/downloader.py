# You tube video yuklab olish
import time
from pytube import YouTube

link = input("Linkni kiriting: ")

ytube = YouTube(link)

chiziq = "-------------------------------------"
papka = "/home/ulugbekpy/Videos/projects/"  # o'zing kirit

print(chiziq)

print(f"Nomi: {ytube.title}")
print(f"Muallif: {ytube.author}")
print(f"Ko'rishlar soni: {ytube.views} marta")

print(chiziq)

text = """---------------------------------------
--- Eng yuqori sifatli video yuklash (1)
--- Eng quyi sifatli video yuklash (2)
--- Faqat ovozni yuklash (3)
--- Yuklashni istamayman (4)

Tanlang(1/2/3/4): """

ask = input(text)

start = time.time()

if ask == "1":
    print(chiziq)
    print("Yuklanmoqda...")
    dwnld = ytube.streams.get_highest_resolution()
    dwnld.download(papka)
elif ask == "2":
    print(chiziq)
    print("Yuklanmoqda...")
    dwnld = ytube.streams.get_lowest_resolution()
    dwnld.download(papka)
elif ask == "3":
    print(chiziq)
    print("Yuklanmoqda...")
    dwnld = ytube.streams.get_audio_only()
    dwnld.download(papka)
elif ask == "4":
    print(chiziq)
    print("xayr!")
else:
    print(".........")

stop = time.time()
if ask in ["1", "2", "3"]:
    print(f"{round(stop - start,2)} soniya davomida yuklandi")

print("xayr!")
