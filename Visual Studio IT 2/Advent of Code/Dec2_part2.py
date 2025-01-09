with open("Dec_2.txt", "r") as file:
    sequences = [list(map(int, line.strip().split())) for line in file.readlines()]

def is_safe(sequence):
    # Check if the sequence is strictly increasing
    increasing = all(x < y for x, y in zip(sequence, sequence[1:]))
    
    # Check if the sequence is strictly decreasing
    decreasing = all(x > y for x, y in zip(sequence, sequence[1:]))
    
    # Check if the absolute difference between consecutive elements is between 1 and 3 (inclusive)
    valid_difference = all(1 <= abs(x - y) <= 3 for x, y in zip(sequence, sequence[1:]))
    
    # Return True if the sequence is either strictly increasing or strictly decreasing
    # and the differences between consecutive elements are valid
    return (increasing or decreasing) and valid_difference

def check_sequences(sequences):
    results = []
    for sequence in sequences:
        if is_safe(sequence):
            results.append("safe")
        else:
            for i in range(len(sequence)):
                dampened_sequence = sequence[:i] + sequence[i+1:]
                if is_safe(dampened_sequence):
                    results.append("safe")
                    break
            else:
                results.append("unsafe")
    return results


results = check_sequences(sequences)

safe_count = results.count("safe")
print(f"Number of safe sequences: {safe_count}")