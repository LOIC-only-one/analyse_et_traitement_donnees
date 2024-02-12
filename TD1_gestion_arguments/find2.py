# !/usr/bin/env python3
import os, sys

def recherche(dossier):
    """
    Cette fonction recherche et stocke les dossiers et les fichiers présents dans un dossier donné et ses sous-dossiers.

    Args:
        dossier (str): Le chemin du dossier à explorer.

    Returns:
        tuple: Un tuple contenant deux listes : listeDossiers (contenant les dossiers) et listeFichiers (contenant les fichiers).
    """
    listeFichiers = []
    listeDossiers = []
    liste = os.listdir(dossier)
    
    try:
        for elt in liste:
            chemin_complet = os.path.join(dossier, elt)
            if os.path.isfile(chemin_complet):
                listeFichiers.append(chemin_complet)
            elif os.path.isdir(chemin_complet):
                listeDossiers.append(chemin_complet)
                # Récursivement, recherche dans les sous-dossiers
                sous_dossiers, sous_fichiers = recherche(chemin_complet)
                listeDossiers.extend(sous_dossiers)
                listeFichiers.extend(sous_fichiers)
        
        return listeDossiers, listeFichiers
    except PermissionError:
        print("Permission refusée pour le dossier", dossier)
        quit()

def start_find2():
    dossier = sys.argv[1]
    listeDossiers, listeFichiers = recherche(dossier)
    
    print("Liste des dossiers :", listeDossiers)
    print("\nListe des fichiers :", listeFichiers)

if __name__ == '__main__':
    start_find2()
