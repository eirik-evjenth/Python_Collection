sum_of_differences = 0

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

    minst_left = 100000

    for i in range(len(left)):
        if int(left[i]) < minst_left:
            minst_left = int(left[i])
            index_left = i

    minst_right = 100000

    for i in range(len(right)):
        if int(right[i]) < minst_right:
            minst_right = int(right[i])
            index_right = i

    sum_of_differences += (abs(minst_left - minst_right))

    if index_right < len(right):
        right.pop(index_right)
    if index_left < len(left):
        left.pop(index_left)

print(sum_of_differences)