# import os
# import shutil

# try:
#     a = 10
#     b = 0
#     # print(a / b)
# except Exception as e:
#     print("Xato ketdi: {}".format(e))
# finally:
#     print("doimmi?")


# if os.path.exists(paths):
#     print("exists")
# else:
#     print("No bro")

# print(os.path.isfile(paths))

# with open("just.txt") as file:
#     print(file.read())

# textim = "\nPython programming"

# with open("just.txt", "a") as faylim:
#     faylim.write(textim)

# with open("just.txt") as file:
#     print(file.read())

# users
# posts(title,content,image,)
# faculties(title)
# info images(faculty/info pk,imagefield)
# partners (fullname,image,about)
# books(image,name,file)
# questions(name,phone number,email,question)
# infos (aloqa,kollej tarixi)
# comments(otzivlar)

# import shutil

# shutil.copyfile(".gitignore", "gitignore.docs")

# src = "just.docs"
# moving_place = "/home/ulugbekpy/just.docs"

# try:
#     if os.path.exists(moving_place):
#         print("there is already a file there!")
#     else:
#         os.replace(src, moving_place)
#         print(src + " has been moved")
# except FileNotFoundError:
#     print(src + " was not found")

# fayl = "trash.py"
# folder = "deletable"

# try:
#     # os.remove(fayl)
#     # os.rmdir(folder)
#     shutil.rmtree(folder)
#     print(f"{folder} removed")
# except Exception as e:
#     print("Exception: {}".format(e))

# a = 0
# del a
