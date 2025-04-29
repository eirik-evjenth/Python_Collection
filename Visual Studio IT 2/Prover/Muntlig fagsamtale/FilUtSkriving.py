
result = "This is the result of the program."

output_file_path = "output.txt"


with open(output_file_path, "w") as fil:
    fil.write(result)

print(f"Result has been written to {output_file_path}")