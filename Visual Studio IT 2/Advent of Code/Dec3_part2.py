import re

mul_total = 0
regex_code = r"mul\(\d{1,3},\d{1,3}\)"
regex_do = r"do\(\)"
regex_dont = r"don't\(\)"

with open("Dec_3.txt", "r") as file:
    text = file.readlines()

enabled = True

for line in text:
    parts = re.split(f"({regex_do}|{regex_dont})", line)
    for part in parts:
        if re.search(regex_dont, part):
            enabled = False
        elif re.search(regex_do, part):
            enabled = True
        elif enabled:
            muls = re.findall(regex_code, part)
            for element in muls:
                element = element.replace("mul(", "").replace(")", "")
                comma = element.index(",")
                mul_total += int(element[:comma]) * int(element[comma + 1:])

print(mul_total)
