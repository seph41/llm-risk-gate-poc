# Exemple vulnérable : injection de commande
import os

def supprimer_fichier():
    fichier = input("Nom du fichier à supprimer : ")
    # Vulnérabilité : l'entrée utilisateur est directement injectée dans la commande système
    os.system("rm -f " + fichier)

supprimer_fichier()
def dangerous_function():
    # Vulnérabilité volontaire : exécution de code arbitraire
    user_input = input("Enter something: ")
    eval(user_input)