nombre_photocopies = int(input("Entrez le nombre de photocopies effectuées : "))

facture = 0.0

if nombre_photocopies <= 10:
    facture = nombre_photocopies * 0.10
elif nombre_photocopies <= 30:
    facture = 10 * 0.10 + (nombre_photocopies - 10) * 0.09
else:
    facture = 10 * 0.10 + 20 * 0.09 + (nombre_photocopies - 30) * 0.08

print(f"Le coût total est de : {facture:.2f} €")
