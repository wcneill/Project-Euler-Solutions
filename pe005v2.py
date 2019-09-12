import pe003 as pe
from collections import Counter

# A faster version for finding the least common multiple of all the numbers from 1 to 20

prime_facts = {}
lcm = 1

for k in range(2, 21):

    kfacts = pe.prime_factors(k)
    print("factorization of", k, "is", kfacts)

    for i in kfacts:
        count = Counter(kfacts)[i]

        if i not in prime_facts.keys():
            prime_facts[i] = count

        elif i in prime_facts.keys() and prime_facts[i] < count:
            prime_facts[i] = count

for f in prime_facts.keys():
    lcm = lcm * f**prime_facts[f]

print(lcm)
