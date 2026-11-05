# Chemin: C:/Users/DIGITAL MARKET/Desktop/Pyhton/projet maxi pandas/models/commande.py
from services.chargement import Ajout
from services.chargement import idf

class Commande:

    def __init__(self,client,ville,restaurant,montant,statut):
        self._id = idf() + 1
        self._client = client
        self._ville = ville
        self._restaurant = restaurant
        self._montant = montant
        self._statut = statut



#region Getter
    @property
    def client(self):
        return self._client

    @property
    def ville(self):
        return self._ville

    @property
    def restaurant(self):
        return self._restaurant

    @property
    def montant(self):
        return self._montant

    @property
    def statut(self):
        return self._statut

    @property
    def id(self):
        return self._id

#endregion

    @client.setter
    def client(self,client):
        self._client = client

#region Setter
    @id.setter
    def id(self,id):
        self._id=id

    @ville.setter
    def ville(self,ville):
        self._ville=ville

    @restaurant.setter
    def restaurant(self,restaurant):
        self._restaurant=restaurant

    @montant.setter
    def montant(self,montant):
        self._montant=montant

    @statut.setter
    def statut(self,statut):
        self._statut=statut


#endregion

#Fonction de presentation de la commande
    def presentation(self):
        return f"===Commande Id: {self._id} | Client: {self._client} | Ville: {self._ville} \n Restaurant: {self._restaurant} | Montant: {self._montant} | Statut: {self._statut}\n"


    def ajout(self):
        donne={
            "id": self._id,
            "client": self._client,
            "ville": self._ville,
            "restaurant": self._restaurant,
            "montant": self._montant,
            "statut": self._statut
        }

        with Ajout("C:/Users/DIGITAL MARKET/Desktop/Pyhton/projet maxi pandas/data/commandes.json",donne) as response:
             return response






