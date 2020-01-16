
alpha_values = {
    'A': 1,  'N': 14,
    'B': 2,  'O': 15,
    'C': 3,  'P': 16,
    'D': 4,  'Q': 17,
    'E': 5,  'R': 18,
    'F': 6,  'S': 19,
    'G': 7,  'T': 20,
    'H': 8,  'U': 21,
    'I': 9,  'V': 22,
    'J': 10, 'W': 23,
    'K': 11, 'X': 24,
    'L': 12, 'Y': 25,
    'M': 13, 'Z': 26
}

with open('data\\p022_names.txt') as file:
    names = file.read().replace('"', '').split(',')

names.sort()
total_value = 0;
for pos, name in enumerate(names, start=1):

    name_value = 0
    for char in name:
        name_value += alpha_values[char]

    name_value *= pos
    total_value += name_value

print(total_value)
