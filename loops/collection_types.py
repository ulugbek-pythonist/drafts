# import math

# print("%.30f" % math.e)

# Lists

# fruits = ["apple", "banana", "pear", "peach", "coconut"]
# mevalar = fruits.copy()
# # fruits.pop()
# # fruits.pop()
# print(mevalar)
# print(fruits)
# print(fruits[-3])
# print(dir(fruits)) # methods of given class
# print(help(fruits))
# # fruits.clear()  # clears the list
# fruits.insert(0, "xurmo")  # added at the beginning
# fruits.append("kiwi")  # added at the end
# fruits.sort(reverse=True)
# print(fruits.index("kiwi")) # output: 6
# print(fruits.count("kiwi")) # prints how many "kiwi"(s) in list
# print(fruits)
# fruits.remove("apple") # removes "apple"
# print(fruits)

# Sets

# print(len(fruits))
# print("apple" in fruits)


# fruits = {"apple", "banana", "pear", "peach", "coconut"}
# mevalar = {"apple", "banana", "pineapple"}
# nums = {1, 2, 3, 4, 5, 6, 7}
# fruits.add("xurmo")
# fruits.remove("apple")
# fruits.pop()
# fruits.discard("apple")
# fruits.discard("pineapple")
# print(fruits.union(nums))  # birlashma
# print(fruits.intersection(nums))  # kesishma
# print(fruits.difference(nums))  # ayirma

# print(fruits.intersection(mevalar))
# fruits.intersection_update(mevalar) #updates fruits as intersection of both sets
# print(mevalar.difference(fruits)) # mevalar dagi fruits da yo'qlari

# print(fruits)
# # fruits.difference_update(mevalar)
# print(fruits)

# fruits.clear()
# print(fruits.isdisjoint(fruits)) # kesishmada hech narsa yo'q bo'lsa True qaytadi

# fruits.update(mevalar) # like union_update
# print(fruits.symmetric_difference(mevalar))
# print(fruits.intersection(mevalar))
# fruits.symmetric_difference_update(mevalar)
# print(fruits)

# Tuples

fruits = ({"apple", "banana"}, "pear", "peach", "coconut")

# print(len(fruits))
# print(fruits.index("coconut"))  # returns index of given value

# print(fruits.count("pear"))
# print(fruits.count("apple"))
# print("apple" in fruits)

# setcha = {2, 1, 0}
# print(setcha)
# a, b, c = setcha
# print(a, b, c, "hello", "world")
# print("daraxto\b ")
print("hi", "John")
