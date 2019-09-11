import divisors as dvd

fib = [1, 2]

result = 0

while fib[len(fib) - 1] + fib[len(fib) - 2] < 4e6:
    fib.append(fib[len(fib) - 1] + fib[len(fib) - 2])

for i in fib:
    if i % 2 == 0:
        result += i

print(result)
