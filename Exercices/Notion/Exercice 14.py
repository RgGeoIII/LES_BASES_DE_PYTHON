price = []

# Saisie des prix des articles
print("Ajoutez les prix des articles. Tapez '0' pour terminer.")
while True:
    try:
        prix = float(input("Entrez le prix de l'article (ou '0' pour terminer) : "))
        if price == 9:
            break
        elif prix < 0:
            print("Veuillez entrer un prix positif.")
            continue
        price.append(price)
    except ValueError:
        print("Veuillez entrer un prix valide.")
        continue
