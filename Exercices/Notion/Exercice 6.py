year = int(input("Entrez votre âge : "))
DLyear = int(input("Depuis combien d'années avez-vous le permis ? "))
accidents = int(input("Combien d'accidents avez-vous eu ? "))
engagementyear = int(input("Depuis combien d'années êtes-vous client chez nous ? "))

res = 0

if year < 25 and DLyear <= 2:
    res = 0
elif (year < 25 and DLyear > 2) or (year >= 25 and DLyear <= 2):
    res = 1
else:
    res = 2

res -= accidents

if res >= 0 and engagementyear > 5:
    res += 1
elif res >= 1 and engagementyear > 5:
    res += 2
else:
    res += 3

if res < 0:
    print("Vous n'êtes pas éligible.")
elif res == 0:
    print("Votre tarif est : Rouge.")
elif res == 1:
    print("Votre tarif est : Orange.")
elif res == 2:
    print("Votre tarif est : Vert.")
else:
    print("Votre tarif est : Bleu.")
