# Chemin: C:/Users/DIGITAL MARKET/Desktop/Pyhton/projet maxi pandas/main.py
import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)

from services.export import *
from services.ajout import ajout
from services.chargement import Chargement,Recherche
from exception.exception import Value
from utils.env import URL
from services.operation import Operation
import time

def analyse():


    print("=====Analyse Complet des donne recu Veillez retrouver le Resultat dans output=====")
    print("========Statistique General========")


    statistique_generale_export()
    for i in range(101):
        print(f"\rTéléchargement : {i}%", end="")
        time.sleep(0.05)

    print("\nTerminé !")

    print("========Chiffre d'affaire restaurant========")
    chiffre_affaire_restaurant_export()
    for i in range(101):
        print(f"\rTéléchargement : {i}%", end="")
        time.sleep(0.02)

    print("\nTerminé !")

    print("========Chiffre d'affaire ville========")
    chiffre_affaire_ville_export()
    for i in range(101):
        print(f"\rTéléchargement : {i}%", end="")
        time.sleep(0.02)

    print("\nTerminé !")

    print("========Nombre commande========")
    nombre_commande_restaurant_export()

    nombre_commande_statut_export()
    for i in range(101):
        print(f"\rTéléchargement : {i}%", end="")
        time.sleep(0.04)

    print("\nTerminé !")

    print("========Meilleur Client========")


    best_client()
    for i in range(101):
        print(f"\rTéléchargement : {i}%", end="")
        time.sleep(0.01)

    print("\nTerminé !")

    print("========Export de toutes les commande analyse========")

    all_commande()
    for i in range(101):
        print(f"\rTéléchargement : {i}%", end="")
        time.sleep(0.05)

    print("\nTerminé !")






if __name__ == "__main__":
    print("Bonjour Monsieur BienVenue sur le Rapport de MBOA")

    analyse()


    while True:
        choix=int(input("""
        Que Voulezz Vous Faire:
        1.Ajouter une Commande 
        2.Afficher les commande comme un tableau 
        3.Afficher les commande de base comme un tableau       
        4.Faire une autre analyse  
        5.Modifier une Commande
        6.Supprimer une Commande
        7.Afficher les commande trier par ordre decroissant
        8.Arrete :
        """))
        if choix == 1:
            try:
                client = input("Entrez le nom du client: ")
                ville = input("Entrez la ville du client: ")
                restaurant = input("Entre le restaurant de la commande: ")
                montant = int(input("Entrez le montant de la commande: "))
                statut = input("Entrez le statut de la commande livree/annulee: ")

                for i in range(101):
                    print(f"\rAjout : {i}%", end="")
                    time.sleep(0.01)

                if ajout(client, ville, restaurant, montant, statut):

                    print("\nCommande Ajouter avec succes")

                    print(
                        "**CONSEIL: Veillez refaire une analyse car on vient de modifier le contenue des donne de base des Commande")

                else:
                    print("\nErreur lors de l'Ajout de la commande")

            except ValueError :
                print("La valeur entre ne respecte pas le type ")



        elif choix == 2:
            with Chargement("C:/Users/DIGITAL MARKET/Desktop/Pyhton/projet maxi pandas/data/commande_analysees.json") as f:
                data = pd.DataFrame(f)

                print(data.to_string(index=False))

        elif choix == 3:
            with Chargement(URL) as f:
                data =pd.DataFrame(f)

                print(data.to_string(index=False))

        elif choix == 4:
            analyse()

            print("***Vous pouvez Observe les differente analyse sur les Tableaux***")

        elif choix == 5:
            try:
                _id = int(input("entrez l'id de la commande a modifier: "))

                with Recherche(URL, _id) as data:
                    operation = Operation(data['client'], data['ville'], data['restaurant'], data['montant'],
                                          data['statut'])
                    for i in range(101):
                        print(f"\rModification : {i}%", end="")
                        time.sleep(0.02)

                    operation.modifier()

                print(
                    "**CONSEIL: Veillez refaire une analyse car on vient de modifier le contenue des donne de base des Commande")
            except ValueError:
                print("La valeur entre ne respecte pas le type ")

        elif choix == 6:
            try:

                _id = int(input("entrez l'id de la commande  a Supprimer: "))
                with Recherche(URL, _id) as data:
                    operation = Operation(data['client'], data['ville'], data['restaurant'], data['montant'],
                                          data['statut'])

                    for i in range(101):
                        print(f"\rSuppression: {i}%", end="")
                        time.sleep(0.01)

                    operation.supprimer()

                print(
                    "**CONSEIL: Veillez refaire une analyse car on vient de modifier le contenue des donne de base des Commande")

            except ValueError:
                print("La valeur entre ne respecte pas le type ")

        elif choix == 7:
            print(trie_decroissant())

        elif choix == 8:
            break





