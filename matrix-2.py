import random

matrica = []

for i in range(2):
    matrica.append([])
    for j in range(3):
        matrica[i].append(random.randint(0,9))

for stroka in matrica:
    print(", ".join(str(chislo) for chislo in stroka))
