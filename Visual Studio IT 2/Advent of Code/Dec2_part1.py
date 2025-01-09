with open("Dec_2.txt", "r") as file:
    sequences = [list(map(int, line.strip().split())) for line in file.readlines()]

def is_safe(sequence):
    increasing = all(x < y for x, y in zip(sequence, sequence[1:]))
    decreasing = all(x > y for x, y in zip(sequence, sequence[1:]))
    valid_difference = all(1 <= abs(x - y) <= 3 for x, y in zip(sequence, sequence[1:]))

    return (increasing or decreasing) and valid_difference

def check_sequences(sequences):
    results = []
    for seq in sequences:
        if is_safe(seq):
            results.append("safe")
        else:
            results.append("unsafe")
    return results


results = check_sequences(sequences)

safe_count = results.count("safe")
print(f"Number of safe sequences: {safe_count}")