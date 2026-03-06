count = 0
with open("bob.txt", "r", encoding="utf-8") as f:
    text = f.read()

slova = text.split()

print(print(f"Počet slov v souboru: {len(slova)}"))

# pismena

text1 = text.replace(" ", "").replace("\n", "")
print(f"Počet písmen v souboru: {len(text1)}")

#jednotliva pismena 

pocet = {}
for pismeno in text1:
    if pismeno in pocet:
        pocet[pismeno] += 1
    else:
        pocet[pismeno] = 1
print("Počet výskytů jednotlivých písmen:", pocet)

# seřazení pismen

pocet_sort = sorted(pocet.items(), key=lambda x: x[1], reverse=True)
print("Top 5 nejčastějších písmen:", pocet_sort[:5])

#nejcastejsi slova

pocet_slov = {}

for slovo in slova:
    if slovo in pocet_slov:
        pocet_slov[slovo] += 1
    else:
        pocet_slov[slovo] = 1
print("Počet výskytů jednotlivých slov:",)
pocet_slov_sort = sorted(pocet_slov.items(), key=lambda x: x[1], reverse=True)
print("Top 5 nejčastějších slov:", pocet_slov_sort[:5])

#osmipismena 

osmipismena = set()
for slovo in slova:
    if len(slovo) == 8:
        osmipismena.add(slovo)
print("Slova s 8 písmeny:", osmipismena)
print(f"Počet slov s 8 písmeny: {len(osmipismena)}")




