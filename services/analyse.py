# Chemin: C:/Users/DIGITAL MARKET/Desktop/Pyhton/projet maxi pandas/services/analyse.py
from utils.nettoyage import nettoyage

df = nettoyage()
def nombre_total_commande():
    return  len(df)

def montant_total():
    return df['montant'].sum()

def montant_moyenne_commande():
    return df['montant'].mean()

def nombre_commande_livre():
    return len(df[df['statut'] == "livree"])

def nombre_commande_annulee():
    return len(df[df['statut'] == "annulee"])

def chiffre_affaire_retaurant():
    return df.groupby('restaurant')['montant'].sum().reset_index()

def chiffre_affaire_ville():
    return df.groupby('ville')['montant'].sum().reset_index()

def nombre_commande_restaurant():
    return df.groupby('restaurant').size().reset_index()

def nombre_commande_statut():
    return df.groupby('statut').size().reset_index()

def client_plus_commande():
    return{
        'client':[df.groupby('client')['montant'].size().idxmax()],
        'nombre':[df.groupby('client')['montant'].size().max()]
    }

def total_commision():
    return df['commission'].sum()

def commission_resto():
    return df.groupby('restaurant')['commission'].sum().reset_index()

def trie_decroissant():
    return df.sort_values(['montant'],ascending=False).to_string(index=False)





