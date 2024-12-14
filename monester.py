from copy import deepcopy

no_of_monster = int(input("monster"))
in_experience = int(input("experience"))

poweri = []
for i in range(no_of_monster):
    poweri.append(int(input()))

bonusi = []
for i in range(no_of_monster):
    bonusi.append(int(input()))

score = 0
power = deepcopy(poweri)
poweri.sort()
# print(poweri)
for i in poweri:
    if i <= in_experience:
        in_experience += bonusi[power.index(i)]
        score += 1
    else:
        break

print(score)
