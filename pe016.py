# Exercise 16
string_result = str(2 ** 1000)
print(type(string_result))

sum_c = 0
for c in string_result:
    sum_c += int(c)

print(sum_c)
