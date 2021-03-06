# Solution to Project Euler #6: Find the difference of the
# Square of Sums and Sum of Squares for the first 100 integers.

sum_o_squares = 0
square_o_sum = 0

for i in range(1, 101):
    sum_o_squares = sum_o_squares + i**2
    square_o_sum = square_o_sum + i

square_o_sum = square_o_sum ** 2

print(square_o_sum - sum_o_squares)