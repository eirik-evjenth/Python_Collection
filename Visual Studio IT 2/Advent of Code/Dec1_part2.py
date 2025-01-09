check = 0

with open("Dec_1.txt", "r") as file:
    data = file.readlines()

    left = []
    right = []

    for i in data:
        left.append(i.split()[0])
        right.append(i.split()[1])

turn = 0
index_left = 0
index_right = 0

while turn < 1000:

    turn += 1

    similarity_score = 0

    for num in left:
        count_in_right = right.count(num)
        similarity_score += int(num) * count_in_right

print("Similarity Score:", similarity_score)