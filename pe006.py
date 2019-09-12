#Solution to Project Euler #6

sum_o_squares = 0
square_o_sum = 0

for i in range(1, 101):
    sum_o_squares = sum_o_squares + i**2
    square_o_sum = square_o_sum + i

square_o_sum = square_o_sum ** 2

print(square_o_sum - sum_o_squares)