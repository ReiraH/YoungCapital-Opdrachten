# Opdracht 2

# 2.1
with open("sleutel_waarde.txt") as f:
    regels = f.readlines()

data = {}
for regel in regels:
    sleutel, waarde = regel.split()
    data[sleutel] = int(waarde)

# Alternatief:
data = dict()
with open("sleutel_waarde.txt") as f:
    for regel in f:
        sleutel, waarde = regel.split()
        data[sleutel] = int(waarde)

# Alternatief:
with open("sleutel_waarde.txt") as f:
    data = {regel.split()[0]: int(regel.split()[-1]) for regel in f}


# 2.2
waarden_met_a = []
for sleutel, waarde in data.items():
    if sleutel.startswith("a"):
        waarden_met_a.append(waarde)
print(sum(waarden_met_a))

# Alternatief
print(sum([waarde for sleutel, waarde in data.items() if sleutel.startswith("a")]))


# 2.3
letters = "abcdefghijklmnopqrstuvwxyz"
for letter in letters:
    waarden_met_letter = []
    for sleutel, waarde in data.items():
        if sleutel[0] == letter:
            waarden_met_letter.append(waarde)
    print(letter, sum(waarden_met_letter))

# Alternatief
import string

for letter in string.ascii_lowercase:
    print(
        letter,
        sum([waarde for sleutel, waarde in data.items() if sleutel.startswith(letter)]),
    )
