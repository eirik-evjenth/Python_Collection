def count_x_mas(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    patterns = [
        ('M', 'A', 'S', 'M', 'S'),
        ('M', 'A', 'S', 'S', 'M'),
        ('S', 'A', 'M', 'S', 'M'),
        ('S', 'A', 'M', 'M', 'S')
    ]

    for i in range(rows - 2):
        for j in range(cols - 2):
            for pattern in patterns:
                if (grid[i][j] == pattern[0] and grid[i+1][j+1] == pattern[1] and grid[i+2][j+2] == pattern[2] and
                    grid[i+2][j] == pattern[3] and grid[i][j+2] == pattern[4]):
                    count += 1
    return count

# Read the grid from the file
with open("Dec_4.txt", "r") as file:
    grid = [list(line.strip()) for line in file.readlines()]

print(count_x_mas(grid))  # Output the count of X-MAS patterns
