# Chemin: C:/Users/DIGITAL MARKET/Desktop/Pyhton/projet maxi pandas/services/export.py
from utils.nettoyage import nettoyage
from services.analyse import *
from services.dechargement import Dechargement
from pandas import DataFrame

data=nettoyage()

def statistique_generale_export():
    resultat = DataFrame({
        'Indeicateur': ['nombre total de commande', 'montant total', "montant moyen d'une commande",
                        "nombre de commande livrées", "nombre de commande annulées", "Total Commission"],
        'Valeur': [
            nombre_total_commande(),
            montant_total(),
            montant_moyenne_commande(),
            nombre_commande_livre(),
            nombre_commande_annulee(),
            total_commision()
        ]
    })

    resultat.to_csv("C:/Users/DIGITAL MARKET/Desktop/Pyhton/projet maxi pandas/output/statistiques_generales.csv",
                    index=False)
    resultat.to_excel("C:/Users/DIGITAL MARKET/Desktop/Pyhton/projet maxi pandas/output/statistiques_generales.xlsx",
                    index=False)


def chiffre_affaire_restaurant_export():
    # chiffre d'afaire par restaurant
    chiffre_affaire_retaurant().to_csv(
        "C:/Users/DIGITAL MARKET/Desktop/Pyhton/projet maxi pandas/output/chifrre_restaurant.csv", index=False)
    chiffre_affaire_retaurant().to_excel(
        "C:/Users/DIGITAL MARKET/Desktop/Pyhton/projet maxi pandas/output/chifrre_restaurant.xlsx", index=False)

def chiffre_affaire_ville_export():
    chiffre_affaire_ville().to_csv("C:/Users/DIGITAL MARKET/Desktop/Pyhton/projet maxi pandas/output/chiffre_ville.csv", index=False)
    chiffre_affaire_ville().to_excel("C:/Users/DIGITAL MARKET/Desktop/Pyhton/projet maxi pandas/output/chiffre_ville.xlsx",
                                   index=False)


def nombre_commande_restaurant_export():
    nombre_commande_restaurant().to_csv("C:/Users/DIGITAL MARKET/Desktop/Pyhton/projet maxi pandas/output/commande_restaurant.csv",index=False)
    nombre_commande_restaurant().to_excel(
        "C:/Users/DIGITAL MARKET/Desktop/Pyhton/projet maxi pandas/output/commande_restaurant.xlsx", index=False)

def nombre_commande_statut_export():
    nombre_commande_statut().to_csv("C:/Users/DIGITAL MARKET/Desktop/Pyhton/projet maxi pandas/output/commande_statut.csv",index=False)
    nombre_commande_statut().to_excel(
        "C:/Users/DIGITAL MARKET/Desktop/Pyhton/projet maxi pandas/output/commande_statut.xlsx", index=False)


def best_client():
    DataFrame(client_plus_commande()).to_csv("C:/Users/DIGITAL MARKET/Desktop/Pyhton/projet maxi pandas/output/best_client.csv",index=False)
    DataFrame(client_plus_commande()).to_excel(
        "C:/Users/DIGITAL MARKET/Desktop/Pyhton/projet maxi pandas/output/best_client.xlsx", index=False)

def all_commande():
    data.to_csv("C:/Users/DIGITAL MARKET/Desktop/Pyhton/projet maxi pandas/output/commande_analysees.csv",index=False)
    data.to_excel("C:/Users/DIGITAL MARKET/Desktop/Pyhton/projet maxi pandas/output/commande_analysees.xlsx", index=False)
    with Dechargement("C:/Users/DIGITAL MARKET/Desktop/Pyhton/projet maxi pandas/data/commande_analysees.json",data.to_dict(orient="records")) as export:
        if export:
            print("exporter avec success")
