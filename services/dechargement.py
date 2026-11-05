# Chemin: C:/Users/DIGITAL MARKET/Desktop/Pyhton/projet maxi pandas/services/dechargement.py
from json import dump, JSONDecodeError

from exception.exception import JsonNotFound, JsonValue




class Dechargement:

    def __init__(self, fichier,contenue):
        self.fichier = fichier
        self.f = None
        self.contenue=contenue

    def __enter__(self):
        try:
            self.f = open(self.fichier,"w",encoding="utf-8")

            dump(self.contenue,self.f,ensure_ascii=False,indent=4)

            return True

        except JSONDecodeError:
            print("Votre contenu m'est pas bon")
            raise JsonValue()

        except FileNotFoundError:
            print("votre fichier n'existe pas")
            raise JsonNotFound()

        
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print("Il y'a une erreur de type: ",exc_type)

        if self.f is not None:
            self.f.close()

        return False





