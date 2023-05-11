# Opdracht 3

# 3.1 en 3.2
with open("eff_large_wordlist.txt") as f:
    regels = f.readlines()

woorden = []
for regel in regels:
    getal, woord = regel.split()
    woord = woord.strip()
    woorden.append(woord)

# Alternatief:
woorden = []
with open("eff_large_wordlist.txt") as f:
    for regel in f:
        getal, woord = regel.split()
        woorden.append(woord.strip())

# Alternatief:
with open("eff_large_wordlist.txt") as f:
    woorden = [regel.split()[-1].strip() for regel in f]


# 3.3
letters = "abcdefghijklmnopqrstuvwxyz"
resultaten = dict()
for letter in letters:
    resultaten[letter] = 0
    for woord in woorden:
        if woord[0] == letter:
            resultaten[letter] += 1

print(resultaten)

# Alternatief
import string

resultaten = dict.fromkeys(string.ascii_lowercase, 0)
for woord in woorden:
    resultaten[woord[0]] += 1

print(resultaten)

# Alternatief
from collections import Counter

resultaten = Counter(woord[0] for woord in woorden)
print(resultaten)
print(dict(resultaten))


# 3.4
# aantal = 0
# for woord1 in woorden:
#     for woord2 in woorden:
#         if woord1 != woord2 and sorted(woord1) == sorted(woord2):
#             aantal += 1
# print(aantal)

# Alternatief / 3.5
anagrammen = dict()
for woord in woorden:
    anagram = "".join(sorted(woord))
    if anagram not in anagrammen:
        anagrammen[anagram] = []
    anagrammen[anagram].append(woord)

aantal = 0
for sleutel, waarde in anagrammen.items():
    if len(waarde) > 1:
        aantal += len(waarde)
print(aantal)

print(
    {sleutel: len(waarde) for sleutel, waarde in anagrammen.items() if len(waarde) > 1}
)
