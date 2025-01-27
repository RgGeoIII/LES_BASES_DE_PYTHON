number = int(input("Enter a number: "))

somme = 0
calcul =""

for i in range(1, number + 1):
    somme += i
    if i == number:
        calcul += f"{i}"
    else:
        calcul += f"{i} + "
print(calcul)
print(f"La somme des entiers de 1 à {number} est : {somme}")