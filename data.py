import sqlite3

DB = "Employees.db"


def create_table():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Employees(
                   id TEXT PRIMARY KEY,
                   name TEXT,
                   role TEXT)"""
    )

    conn.commit()
    conn.close()


def get_employees():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Employees")
    employees = cursor.fetchall()
    conn.close()
    return employees


def insert_employee(id, name, role):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO Employees(id,name,role) VALUES (?,?,?)", (id, name, role)
    )
    conn.commit()
    conn.close()


employees = get_employees()

for i in employees:
    for j in i:
        print(j, end=" | ")
    print("\b ")

# n = int(input("How many employees do you add: "))

# for i in range(n):
#     Id = input("id: ")
#     name = input("name: ")
#     role = input("role: ")

#     insert_employee(Id, name, role)

# employees = get_employees()

# for i in employees:
#     for j in i:
#         print(j, end=" | ")
#     print("\b ")

# emp_list = get_employees()

# for i in emp_list:
#     for j in i:
#         print(j, end=" | ")
#     print("\b ")


def delete_employee(id):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Employees WHERE id = ?", (id,))
    conn.commit()
    conn.close()


# emp_list = get_employees()

# for i in emp_list:
#     for j in i:
#         print(j, end=" | ")
#     print("\b ")

# Id = input("delete by id: ")

# delete_employee(Id)

# emp_list = get_employees()

# for i in emp_list:
#     for j in i:
#         print(j, end=" | ")
#     print("\b ")


def update_employee(new_name, new_role, id):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE Employees SET name = ?, role = ? WHERE id = ?", (new_name, new_role, id)
    )
    conn.commit()
    conn.close()


emp_list = get_employees()

for i in emp_list:
    for j in i:
        print(j, end=" | ")
    print("\b ")

Id = input("update by id: ")
name = input("New name: ")
role = input("New role: ")
update_employee(name, role, Id)

emp_list = get_employees()

for i in emp_list:
    for j in i:
        print(j, end=" | ")
    print("\b ")
