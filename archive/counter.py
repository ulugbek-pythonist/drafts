def scores():
    students = {"Ulugbek": 0}
    student = input("Name of student: ")
    score = int(input("Enter score: "))

    if student in students.keys():
        students[student] += score
    else:
        students[student] = score

    a = input("Continue (y/n)? ")
    if a.lower() == "y":
        scores()

    for talaba, ball in students.items():
        print(f"{talaba} -- {ball}")


scores()
