import csv

# Les inn serienumrene fra fil2 (tab-separert, serienummer i kolonne 5 - indeks 4)
serienummer_fil2 = set()
with open("fil2.txt", encoding="utf-8") as f:
    for linje in f:
        deler = linje.strip().split("\t")
        if len(deler) >= 5:
            serienummer_fil2.add(deler[4].strip())

# Kolonner vi vil hente ut fra fil1, i samme rekkefølge som fil2
kolonner_som_skal_med = [
    "Device Name",
    "Platform",
    "Device Series",
    "Device Family",
    "Serial Number",
    "MAC Address",
]

# Les fil1 (ordentlig CSV-parsing, håndterer anførselstegn/kommaer i felt)
with open("fil1.txt", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)
    indekser = [header.index(kol) for kol in kolonner_som_skal_med]
    serial_kolonne = header.index("Serial Number")

    match = []
    avvik = []
    for rad in reader:
        serienummer = rad[serial_kolonne].strip()
        verdier = [rad[i].strip() for i in indekser]
        if serienummer in serienummer_fil2:
            match.append(verdier)
        else:
            avvik.append(verdier)

# Skriv enkel, lesbar tekstfil i fil2-format
with open("resultat.txt", "w", encoding="utf-8") as f:
    f.write("=== MATCH: Finnes i BEGGE filer ===\n")
    f.write(f"({len(match)} stk)\n\n")
    for verdier in match:
        f.write("\t".join(verdier) + "\n")

    f.write("\n=== AVVIK: Finnes i fil1 men IKKE i fil2 ===\n")
    f.write(f"({len(avvik)} stk)\n\n")
    for verdier in avvik:
        f.write("\t".join(verdier) + "\n")

print(f"Match: {len(match)}")
print(f"Avvik: {len(avvik)}")
print("Resultat lagret i resultat.txt")