
# The following code completed the exercise, but computation time was ~ 2 minutes
# see pe005v2 for a faster algorithm

winner = False
k = 2520

while not winner:
    for i in range(1, 21):
        if k % i != 0:
            k += 2
            break
        elif i == 20 and k % i == 0:
            winner = True

print(k)

