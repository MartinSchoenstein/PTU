# Projet PTU 2024 
# Python 3.12.7 
# 
# Jérémie CARABIN 

""" 
Permet de récupérer les annotations de la référence GALLUS GALLUS pour les protéines alignées à motiée 
afin de faire un BLASTN pour voir si on peut compléter les protéines et leur annotations 
"""
#Import : 

import pandas as pd
import sys

"""
if len(sys.argv) < 3:
    print("Usage: python script.py <chemin_vers_le_fichier_genome>")
    sys.exit(1) 
    sys.exit(2) 

fichier = sys.argv[1]
"""
# Chemin vers le fichier BLASTp TSV
fichier_BLASTp_TSV = "/data/projet6/data/1_work/Analyse_BLASTp/blastp_oriolus_vs_gallus_TSV.txt"

# Définir les noms des colonnes basés sur l'aperçu des données
colonnes = ['qseqid', 'sseqid', 'pident', 'length', 'mismatch', 'gapopen', 'qstart', 'qend', 'sstart', 'send', 'evalue', 'bitscore']

# Lecture du fichier TSV avec les noms de colonnes
print("Lecture du fichier TSV...")
dfTSV = pd.read_csv(fichier_BLASTp_TSV, sep="\t", names=colonnes)

# Afficher un aperçu des données
print("Aperçu des données :")
print(dfTSV.head())
print(len(dfTSV))

#enlever les valeurs abérante 
df_filtered = dfTSV[dfTSV["evalue"] != 0.0]
print("df_filterd", len(df_filtered))

# Supprimer les doublons en gardant la première occurrence pour chaque qseqid
df_best_hit = df_filtered.drop_duplicates(subset=['qseqid'], keep='first')

# Afficher un aperçu des données sans doublons
print("Données sans doublons pour chaque qseqid :")
print(df_best_hit.head())
print(len(df_best_hit))

# Analyse des différences de recouvrements :

def process_row(row):
    difstart = row['qstart'] - row['sstart'] + 1
    diffend = row['qend'] - row['send'] + 1
    return difstart, diffend

df_best_hit[['difstart', 'diffend']] = df_best_hit.apply(process_row, axis=1, result_type="expand")

print(df_best_hit)

# Print de la distribution de différence 

import matplotlib.pyplot as plt
import seaborn as sns

# Création d'un histogramme pour difstart
plt.figure(figsize=(10, 5))

# Distribution de difstart
plt.subplot(1, 2, 1)
sns.histplot(df_best_hit['difstart'], bins=20, kde=True, color='blue', label='Difstart')
plt.axvline(1, color='red', linestyle='--', label='Alignement complet (1)')
plt.title('Distribution de Difstart')
plt.xlabel('Difstart (qstart - sstart + 1)')
plt.ylabel('Fréquence')
plt.legend()

# Distribution de diffend
plt.subplot(1, 2, 2)
sns.histplot(df_best_hit['diffend'], bins=20, kde=True, color='green', label='Diffend')
plt.axvline(1, color='red', linestyle='--', label='Alignement complet (1)')
plt.title('Distribution de Diffend')
plt.xlabel('Diffend (qend - send + 1)')
plt.ylabel('Fréquence')
plt.legend()

# Affichage des graphiques
plt.tight_layout()
plt.show()

plt.savefig('/data/projet6/data/1_work/Analyse_BLASTp/distribution_d.png')

# Stat analystique : 

# Calcul des statistiques pour 'difstart' et 'diffend'
stats_difstart = df_best_hit['difstart'].describe()
stats_diffend = df_best_hit['diffend'].describe()

# Afficher les résultats
print("Statistiques pour 'difstart' :")
print(stats_difstart)

print("\nStatistiques pour 'diffend' :")
print(stats_diffend)

# Moyenne, médiane, écart-type, max, min pour difstart
mean_difstart = stats_difstart['mean']
median_difstart = stats_difstart['50%']
std_difstart = stats_difstart['std']
min_difstart = stats_difstart['min']
max_difstart = stats_difstart['max']

# Moyenne, médiane, écart-type, max, min pour diffend
mean_diffend = stats_diffend['mean']
median_diffend = stats_diffend['50%']
std_diffend = stats_diffend['std']
min_diffend = stats_diffend['min']
max_diffend = stats_diffend['max']

# Affichage des valeurs
print(f"\nMoyenne de 'difstart': {mean_difstart}")
print(f"Médiane de 'difstart': {median_difstart}")
print(f"Écart-type de 'difstart': {std_difstart}")
print(f"Minimum de 'difstart': {min_difstart}")
print(f"Maximum de 'difstart': {max_difstart}")

print(f"\nMoyenne de 'diffend': {mean_diffend}")
print(f"Médiane de 'diffend': {median_diffend}")
print(f"Écart-type de 'diffend': {std_diffend}")
print(f"Minimum de 'diffend': {min_diffend}")
print(f"Maximum de 'diffend': {max_diffend}")

# Compter le nombre de décalages à 0 pour 'difstart' et 'diffend'
count_difstart_0 = df_best_hit[df_best_hit['difstart'] == 0].shape[0]
count_diffend_0 = df_best_hit[df_best_hit['diffend'] == 0].shape[0]

print(f"Nombre de décalages à 0 pour 'difstart': {count_difstart_0}")
print(f"Nombre de décalages à 0 pour 'diffend': {count_diffend_0}")
