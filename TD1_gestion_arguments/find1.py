# !/usr/bin/env python3
import os
import sys

def affiche(path):
    return os.listdir(path)

def aide():
    """main() : Passage d'un argument afin de pouvoir afficher le contenu 
    d'un dossier ou non 
    
    UTILISATION : python3 script.py /dir/"""
    return help(aide)
    
def start_find1():
    nb_arg = len(sys.argv)
    if nb_arg == 2:
        file_path = sys.argv[1] 
        if os.path.exists(file_path):
            print(f"Chemin trouvé")
            print(affiche(file_path))
        else:
            print("Chemin non trouvé")
            
    else:
        print(aide())
        print("Pas d'argument passé en parametre !")
    
if __name__ == "__main__":
    start_find1()
