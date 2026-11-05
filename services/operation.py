# Chemin: C:/Users/DIGITAL MARKET/Desktop/Pyhton/projet maxi pandas/services/operation.py
from models.commande import Commande

from services.chargement import Ajout,Supprimer,RechercheId

from utils.env import URL

class Operation(Commande):
    def __init__(self,client,ville,restaurant,montant,statut):
        super().__init__(client,ville,restaurant,montant,statut)

    def modifier(self):
        try:
            client = input(f"entrer le nouveau nom (ancien: {self.client}): ") or self.client
            ville = input(f"entrer le nouveau Ville (ancien: {self.ville}): ") or self.ville
            restaurant = input(f"entrer le nouveau Restaurant (ancien: {self.restaurant}): ") or self.restaurant
            montant = int(input(f"entrer le nouveau montant (ancien: {self.montant}): ")) or self.montant
            statut = input(f"entrer le nouveau statut (ancien: {self.statut}): ") or self.statut
        except ValueError:
            print("erreur lors de l'entrer")


        with RechercheId(URL,{
            'client':self.client,
            'ville':self.ville,
            'restaurant':self.restaurant,
            'montant':self.montant,
            'statut':self.statut
        }) as donne:
            with Supprimer(URL,donne) as supprimer:
                if supprimer:
                    with Ajout(URL,{
                        'id':donne,
                        'client': client,
                        'ville': ville,
                        'restaurant': restaurant,
                        'montant': montant,
                        'statut': statut
                    }) as add:
                        if add:
                            print("Donne Modifier avec Succes")

                        else:
                            print("Donne non Modifier Et peux etre Supprimer")

                else:
                    print("Donne non Modifier")




    def supprimer(self):

        with RechercheId(URL,{
                'client':self.client,
                'ville':self.ville,
                'restaurant':self.restaurant,
                'montant':self.montant,
                'statut':self.statut
            }) as _id:

            with Supprimer(URL,_id) as supp:
                if supp:
                    print("Donne Supprimer")
                else:
                    print("Donne non Supprimer")





