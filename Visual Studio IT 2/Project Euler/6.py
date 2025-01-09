sum_squares =0
sum_addition = 0
sum_all = 0


for i in range(1, 101):
    sum_squares += i**2
    sum_addition += i

sum_all += sum_addition**2

difference = sum_all - sum_squares

print(difference)


