import os
import shutil

#Exo1
if not os.path.exists('Exo1folder'):
    os.mkdir('Exo1folder')


Exo1 = open('Exo1.txt', 'w+')
Exo1.write("Ceci est la ligne1\nCeci est la ligne2\nCeci est la ligne3\nCeci est la ligne4")
Exo1.close()

shutil.move('Exo1.txt', 'Exo1folder')

#Exo2
if not os.path.exists('Exo2folder'):
    os.mkdir('Exo2folder')

Exo2 = open("Exo2.txt", "w+")
Exo2.write("Test1\n")
Exo2.write("Test2\n")
Exo2.write("Test3\n")
Exo2.close()

shutil.move('Exo2.txt', 'Exo2folder')

#Exo3
if not os.path.exists('Exo3folder'):
    os.mkdir('Exo3folder')

Exo3 = open("Exo3.txt", "w+")
Exo3.write("Test4\n")
Exo3.write("Test5\n")
Exo3.close()
shutil.move('Exo3.txt', 'Exo3folder')

with open("Exo3folder/Exo3.txt", "r") as Exo3:
    print(Exo3.readlines())
Exo3.close()

#Exo4

if not os.path.exists('Exo4folder'):
    os.mkdir('Exo4folder')
Exo4= "Exo4.txt"
with open(Exo4, "w") as fichier:
    fichier.write("Ceci est un exemple de fichier contenant plusieurs mots.\n")
    fichier.write("Il permet de tester la fonction split pour diviser le texte en mots.\n")


with open(Exo4, "r") as fichier:
    contenu = fichier.read()
    mots = contenu.split()
    nombre_de_mots = len(mots)

print(f"Le fichier contient {nombre_de_mots} mots.")
shutil.move('Exo4.txt', 'Exo4folder/Exo4.txt')

#Exo5
if not os.path.exists('Exo5depart') and not os.path.exists('Exo5destination'):
    os.mkdir('Exo5depart')
    os.mkdir('Exo5destination')

Exo5= open("Exo5depart.txt", "w+")
Exo5.write("Test8\n")
Exo5.write("Test9\n")
Exo5.close()
shutil.move('Exo5depart.txt', 'Exo5depart')

shutil.move('Exo5depart/Exo5depart.txt', 'Exo5destination/')


