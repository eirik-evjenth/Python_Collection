xmas_count = 0

with open("Dec_4.txt", "r") as file:
    text = [line.strip() for line in file.readlines()]

# Check for X-MAS pattern
for i in range(1, len(text) - 1):
    for j in range(1, len(text[i]) - 1):
        if text[i][j] == 'A':
            positions = [(i-1, j-1), (i-1, j+1), (i+1, j-1), (i+1, j+1)]
            if all(0 <= pos[0] < len(text) and 0 <= pos[1] < len(text[i]) for pos in positions):
                values = [text[pos[0]][pos[1]] for pos in positions]
                for value in values:
                    if value == 'X':
                        break
                else:
                    m_count = values.count('M')
                    s_count = values.count('S')
                    if m_count != 2 or s_count != 2:
                        continue
                    print("Pattern found")
                    print(f"Checking positions: {positions}")
                    print(f"Values: {values}")
                    xmas_count += 1


print(xmas_count)
