xmas = "XMAS"
xmas_count = 0

with open("Dec_4.txt", "r") as file:
    text = [line.strip() for line in file.readlines()]

# mot høyre
for i in range(len(text)):
    for j in range(len(text[i]) - 3):
        ord = text[i][j] + text[i][j + 1] + text[i][j + 2] + text[i][j + 3]
        if xmas == ord:
            xmas_count += 1

# mot venstre
for i in range(len(text)):
    for j in range(3, len(text[i])):
        ord = text[i][j] + text[i][j - 1] + text[i][j - 2] + text[i][j - 3]
        if xmas == ord:
            xmas_count += 1

# ned
for i in range(len(text) - 3):
    for j in range(len(text[i])):
        ord = text[i][j] + text[i + 1][j] + text[i + 2][j] + text[i + 3][j]
        if xmas == ord:
            xmas_count += 1

# Vertical up
for i in range(3, len(text)):
    for j in range(len(text[i])):
        ord = text[i][j] + text[i - 1][j] + text[i - 2][j] + text[i - 3][j]
        if xmas == ord:
            xmas_count += 1

# ned til høyre
for i in range(len(text) - 3):
    for j in range(len(text[i]) - 3):
        ord = text[i][j] + text[i + 1][j + 1] + text[i + 2][j + 2] + text[i + 3][j + 3]
        if xmas == ord:
            xmas_count += 1

# opp mot høyre
for i in range(3, len(text)):
    for j in range(len(text[i]) - 3):
        ord = text[i][j] + text[i - 1][j + 1] + text[i - 2][j + 2] + text[i - 3][j + 3]
        if xmas == ord:
            xmas_count += 1

# ned til venstre
for i in range(len(text) - 3):
    for j in range(3, len(text[i])):
        ord = text[i][j] + text[i + 1][j - 1] + text[i + 2][j - 2] + text[i + 3][j - 3]
        if xmas == ord:
            xmas_count += 1

# opp mot venstre
for i in range(3, len(text)):
    for j in range(3, len(text[i])):
        ord = text[i][j] + text[i - 1][j - 1] + text[i - 2][j - 2] + text[i - 3][j - 3]
        if xmas == ord:
            xmas_count += 1


print(xmas_count)