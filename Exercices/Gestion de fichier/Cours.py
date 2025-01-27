import os
import shutil

if not os.path.exists('Exo1folder'):
    os.mkdir('Exo1folder')

Exo1 = open('Exo1.txt', 'w+')
Exo1.write("Ceci est la ligne1\nCeci est la ligne2\nCeci est la ligne3\nCeci est la ligne4")

shutil.move('Exo1.txt', 'Exo1folder')
