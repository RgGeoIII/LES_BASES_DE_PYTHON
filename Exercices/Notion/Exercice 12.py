number = int(input("Enter a number: "))

produit = 1
calcul = ""

for i in range(1, number + 1):
    produit *= i
    if i == number:
        calcul += f"{i}"
    else:
        calcul += f"{i} x "

print(f"Le calcul est : {calcul} = {produit}")