inf = 0
year = int(input('tape the date :\nYear:>>'))
while True:
    if year in range(1900, 2022):
        break
    year = int(input("[The year must be between 1900 and 2022]\nYear:>>"))
    inf += 1
inf2 = 0
mount = int(input('Mount:>>'))
while True:
    if 1 <= mount <= 12:
        break
    mount = int(input("[The month must be between 1 and 12\nMount:>>"))
    inf2 += 1

day = int(input('Day:>>'))
while True:
    if 1 <= day <= 31:
        break
    day = int(input("[The day must be between 1 and 31\nِDay:>>"))

print(str(year) + '/' + str(mount) + '/' + str(day))

print(inf, inf2)
