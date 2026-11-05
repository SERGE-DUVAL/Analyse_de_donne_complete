# Chemin: C:/Users/DIGITAL MARKET/Desktop/Pyhton/projet maxi pandas/services/chargement.py
from json import load, JSONDecodeError,dump
from exception.exception import JsonNotFound, JsonValue
import pandas as pd
from utils.env import URL

class Chargement:
    def __init__(self,fichier):
        self.fichier = fichier
        self.f = None
        self.contenue_fichier={}

    def __enter__(self):
        try:
            self.f = open(self.fichier,"r",encoding="utf-8")

            self.contenue_fichier=load(self.f)

            return self.contenue_fichier

        except FileNotFoundError:
            print("Votre fichier n'existe pas ou vos Donne ne sosnt pas stocker a cet emplacment")
            raise

        except JSONDecodeError:
            print("Les donne stocke ne corresponde pas au Format requis")
            raise

    def __exit__(self, exc_type, exc_val, exc_tb):

        if exc_type is not None:
            print("Nous avons rencontrez une erreur lors de l'execution de votre travail sur le ficher")

        if self.f is not None:
            self.f.close()


        return False






class Ajout:

    def __init__(self, fichier, contenue):
        self.fichier = fichier
        self.f = None
        self.contenue = contenue

    def __enter__(self):
        try:

            with Chargement(self.fichier) as fi:
                data = fi

            data.append(self.contenue)
            self.f = open(self.fichier, "w", encoding="utf-8")

            dump(data, self.f,ensure_ascii=False, indent=4)

            return True

        except JSONDecodeError:
            print("Votre contenu m'est pas bon")
            raise

        except FileNotFoundError:
            print("votre fichier n'existe pas")
            raise

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print("Il y'a une erreur de type: ", exc_type)

        if self.f is not None:
            self.f.close()

        return False

class Supprimer:
    def __init__(self,fichier,_id):
        self.fichier=fichier
        self.id=_id
        self.f=None

    def __enter__(self):
        try:
            with Recherche(URL,self.id) as contenue:
                with Ajout("C:/Users/DIGITAL MARKET/Desktop/Pyhton/projet maxi pandas/data/commandes_supprimer.json",contenue ) as response:
                    with Chargement(self.fichier) as data:
                        nouvelle_data = [d for d in data if d['id'] != self.id]

                    self.f = open(self.fichier, "w", encoding="utf-8")

                    dump(nouvelle_data, self.f, ensure_ascii=False, indent=4)



            return response

        except JSONDecodeError:
            print("Votre contenu m'est pas bon")
            raise JsonValue()

        except FileNotFoundError:
            print("votre fichier n'existe pas")
            raise JsonNotFound()


    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print("Il y'a une erreur de type: ", exc_type)

        if self.f is not None:
            self.f.close()

        return False


class RechercheId:
    def __init__(self,fichier,_donne):
        self.fichier=fichier
        self.donne=_donne
        self.f=None

    def __enter__(self):
        try:
            with Chargement(URL) as data:
                donne_trouve = [
                    d
                    for d in data
                    if pd.DataFrame(data)[['client','ville','restaurant','montant','statut']] ==
                       pd.DataFrame(self.donne)[['client','ville','restaurant','montant','statut']]
                ]

            return donne_trouve[0]['id']

        except JSONDecodeError:
            print("Votre contenu m'est pas bon")
            raise JsonValue()

        except FileNotFoundError:
            print("votre fichier n'existe pas")
            raise JsonNotFound()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print("Il y'a une erreur de type: ", exc_type)

        if self.f is not None:
            self.f.close()


class Recherche:
    def __init__(self,fichier,_id):
        self.fichier=fichier
        self.id=_id
        self.f=None
        self.contenue={}
        self.trouve={}

    def __enter__(self):

        try:

            self.f=open(self.fichier,"r")

            self.contenue = load(self.f)

            self.trouve=[
                d
                for d in self.contenue
                if d['id'] == self.id
            ]

            return self.trouve[0]

        except JSONDecodeError:
            print("Votre contenu m'est pas bon")
            raise JsonValue()

        except FileNotFoundError:
            print("votre fichier n'existe pas")
            raise JsonNotFound()


    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print("Il y'a une erreur de type: ", exc_type)

        if self.f is not None:
            self.f.close()


def donne():
    with Chargement(URL) as f:

        return f

def idf():
    with Chargement(URL) as f:

        return f[len(f)-1]['id']





