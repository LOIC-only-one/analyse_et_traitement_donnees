# !/usr/bin/env python3

import find1
import find2
from my_package_LM import find_complet
import sys

def display_menu():
    """
    Affiche le menu de choix des options.
    """
    print("Menu:")
    print("1. find1")
    print("2. find2")
    print("3. find3")
    print("4. Quitter")

def get_user_choice():
    """
    Demande à l'utilisateur de choisir une option.
    
    Returns:
        str: L'option choisie par l'utilisateur.
    """
    while True:
        choix = input("Veuillez choisir une option (1-4): ")
        if choix in ['1', '2', '3', '4']:
            return choix
        else:
            print("Option invalide. Veuillez saisir un nombre entre 1 et 4.")

def main():
    """
    Fonction principale pour exécuter le menu.
    """
    try:
        while True:
            display_menu()
            option = get_user_choice()
            
            if option == '1':
                find1.start_find1()
            elif option == '2':
                find2.start_find2()
            elif option == '3':
                find_complet()
            else:
                print("See you soon bro !")
                break
    except IndexError:
        print("Veuillez passer un argument en paramètre.")
        print("Exemple: python3 menu.py /chemin/dossier")
        quit()

if __name__ == "__main__":
    main()
