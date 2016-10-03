import random as sluchainost

def soderzhit_element(massiv, x):
    for chislo in massiv:
        if chislo == x:
            return True
    return False

massiv = list(range(101))

# Esli by massiv bul otsortirovan, mozhno bylo by ispolzovat binarny poisk
sluchainost.shuffle(massiv)

print(soderzhit_element(massiv, 1000)) # => False
print(soderzhit_element(massiv, 10))   # => True
