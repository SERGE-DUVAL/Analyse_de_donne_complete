# Chemin: C:/Users/DIGITAL MARKET/Desktop/Pyhton/projet maxi pandas/services/ajout.py
from models.commande import Commande
def ajout(client,ville,restaurant,montant,statut):

    if(client
        and ville
        and restaurant
        and montant > 0
        and (statut == "livree"
                or statut == "annulee"
            )
    ):
        return Commande(client,ville,restaurant,montant,statut).ajout()
    else:
        return False





