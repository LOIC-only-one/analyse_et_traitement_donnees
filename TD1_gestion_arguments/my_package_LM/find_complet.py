# !/usr/bin/env python3
import os, sys

def recherche_(dossier, name):
    """
    Recherche le fichier spécifié dans le dossier donné et ses sous-dossiers.

    Args:
        dossier (str): Le chemin du dossier à explorer.
        name (str): Le nom du fichier à rechercher.

    Returns:
        tuple: Un tuple contenant deux listes : listeDossiers (contenant les dossiers) et listeFichiers (contenant les fichiers).
    """
    listeFichiers = []
    listeDossiers = []
    liste = os.listdir(dossier)
    try:
        
        for elt in liste:
            # Joindre le chemin complet
            chemin_complet = os.path.join(dossier, elt)
            if os.path.isfile(chemin_complet):
                if name == elt:
                    listeFichiers.append(chemin_complet)
                else:
                    listeFichiers.append(elt)
            elif os.path.isdir(chemin_complet):
                listeDossiers.append(elt)
                
                # Recherche dans les sous-dossiers
                sous_dossiers, sous_fichiers = recherche_(chemin_complet, name)
                listeDossiers.extend(sous_dossiers)
                listeFichiers.extend(sous_fichiers)

        return listeDossiers, listeFichiers
    except IndexError:
        print("Veuillez passer un argument en paramètre.")
        print("Exemple: python3 find_complet.py /chemin/dossier nom_fichier")
        quit()
    except PermissionError:
        print("Permission refusée pour le dossier", dossier)
        quit()

def main():
    dossier = sys.argv[1]
    name = sys.argv[2]
    
    listeDossiers, listeFichiers = recherche_(dossier, name)
    print("Liste des dossiers :", listeDossiers)
    print("\nListe des fichiers :", listeFichiers)

if __name__ == "__main__":
    main()
