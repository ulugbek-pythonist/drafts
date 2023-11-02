a = []
b = []
teams = set()

for i in range(8):
    team = input("team: ")
    teams.add(team)

for i in range(8):
    if i < 4:
        a.append(teams.pop())
    else:
        b.append(teams.pop())

print("----------------------------")
print("A guruh")
for s in a:
    print(s)
print("----------------------------")
print("B guruh")
for d in b:
    print(d)
