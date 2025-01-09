import re

middle_pages = 0

with open("Dec_5.txt", "r") as file:
    text = [line.strip() for line in file.readlines()]

regex_code = r","

total = 0

for line in text:
    line = str(line)
    line = line.replace(",", "")
    for number in line:
        total += 1

    total //= 2

    line = line[total-1:total + 1]
    print(f"You added {line} to the already existing middle page sum of {middle_pages}")
    middle_pages += int(line)
        
    total = 0

print(middle_pages)