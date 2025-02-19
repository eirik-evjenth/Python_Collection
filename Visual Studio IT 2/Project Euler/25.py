import time

start_time = time.time()

start = 0
next = 1
index = 0
running = True

while running:
    if len(str(next)) >= 1000:
        running = False
    else:
        start += next
        index += 1
        next += start
        index += 1

end_time = time.time()
execution_time = end_time - start_time

print(f"The first fib sequence with over 1000 digits is: {index}")
print(f"Execution time: {execution_time} seconds")