import sys

def main():
    """
    main() : Affiche tous les arguements passés en ligne de commande
    """
    nb_args = len(sys.argv)
    if nb_args == 1:
        print("No arguments")
    elif nb_args > 1:
        for element in sys.argv :
            print(element)

if __name__ == "__main__":
    main()