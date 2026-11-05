# Chemin: C:/Users/DIGITAL MARKET/Desktop/Pyhton/projet maxi pandas/utils/nettoyage.py
from services.chargement import donne
import pandas as pd
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)

donne_brut=donne()



#region nettoyage de donne

def nettoyage():

    data = pd.DataFrame(donne_brut)
    data = pd.DataFrame(donne_brut)
    # Uniformisaons les nom des clients et vilel

    data = data.drop_duplicates()

    data['client'] = data['client'].str.strip().str.title()

    data['ville'] = data['ville'].str.strip().str.title()

    data['statut'] = data['statut'].str.strip()
    # comblons les valeur manquante



    data['client'] = data['client'].fillna("Inconnue")

    data['ville'] = data['ville'].fillna("Inconnue")

    data['restaurant'] = data['restaurant'].fillna("Inconnue")

    data['montant'] = data['montant'].fillna(data['montant'].mean())

    data['statut'] = data['statut'].fillna('annulee')

    data['commission'] = data['montant'] * (10 / 100)

    data['montant_net'] = data['montant'] - data['commission']

    return data


#endregion