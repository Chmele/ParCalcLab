import string, random

strings = []
for _ in range(750000):
    s = ''.join(random.choices(string.ascii_letters, k=random.randint(1,10)))
    strings.append(s)

with open('input75.txt', 'w') as f:
    for s in strings:
        f.write(s + '\n')