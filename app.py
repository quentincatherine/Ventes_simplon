import pandas as pd
import plotly.express as px

# 1. Chargement des données
df = pd.read_csv('ventes.simplon.csv')

# 2. Calcul du Chiffre d'Affaires (Prix x Quantité)
df['ca'] = df['prix'] * df['qte']

# --- 6.a : Ventes par produit (Quantités) ---
ventes_prod_qte = df.groupby('produit')['qte'].sum().reset_index()
fig_qte = px.bar(
    ventes_prod_qte, 
    x='produit', 
    y='qte', 
    title='Ventes par produit (Quantités)', 
    color='produit'
)
fig_qte.write_html('ventes-par-produit.html')

# --- 6.b : Chiffre d'affaires par produit (€) ---
ventes_prod_ca = df.groupby('produit')['ca'].sum().reset_index()
fig_ca = px.bar(
    ventes_prod_ca, 
    x='produit', 
    y='ca', 
    title='Chiffre d\'Affaires par produit (€)', 
    color='produit'
)
fig_ca.write_html('ca-par-produit.html')

print("Les 2 graphiques ont été générés avec succès !")