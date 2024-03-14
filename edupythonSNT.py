import random

mots = ["caramel", "robinet", "ordinateur", "papillon", "montagne", "téléphone"]
mot = random.choice(mots)
mot_cache = "_" * len(mot)
essais_restants = 6

while essais_restants > 0 and "_" in mot_cache:
    print("Mot à deviner:", " ".join(mot_cache))
    lettre = input("Devinez une lettre : ")
    if lettre in mot:
        for i in range(len(mot)):
            if mot[i] == lettre:
                mot_cache = mot_cache[:i] + lettre + mot_cache[i + 1:]
    else:
        essais_restants -= 1
        print(f"Il vous reste {essais_restants} essais.")
        
if "_" not in mot_cache:
    print("Félicitations, vous avez deviné le mot :", mot)
else:
    print("Désolé, vous avez épuisé tous vos essais. Le mot était :", mot)
