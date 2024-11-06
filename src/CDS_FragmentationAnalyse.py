"""
PTU - 2024

Jérémie Carabin 

Python 3.12.4


fichier_fasta -> argument 1 (fichier fasta cds pour analyse des cds par gène)
filename_graphe -> argument 2 (chemin et nom du fichier de sortie)
"""
import sys
from Bio import SeqIO
import re
import matplotlib.pyplot as plt



# fichier = "/home/coursM2/PTU/data/1_work/cds_localisationPerGene.txt"

# fichier_fasta = "/home/coursM2/PTU/data/0_raw/GCA_013399295.1_ASM1339929v1_cds_from_genomic.fna"
# filename_graphe = "/home/coursM2/PTU/data/1_work/DistributionNombreCDS.png"

def CDS_recup (description) :
        pattern = r'\[location=(.*?)\]'
        matches = re.findall(pattern, description)
        if matches : 
                pattern = r'(join\(.*?\))'
                matches = re.findall(pattern, description)
                if matches : 
                        matches=matches[0]
                        return matches[7:-1].split(",")


def compte_cdsPerGene(fichier_fasta,list_taille_CDS=[]) :
        with open(fichier_fasta, "r") as handle:
                for record in SeqIO.parse(handle, "fasta"):
                        description = record.description
                        cds = CDS_recup(description)
                        if cds :   list_taille_CDS.append(len(cds))
        return list_taille_CDS

def distributionGraph(liste, filename_graphe):
        """Affiche l'histogramme de la distribution des longueurs des CDS."""
        plt.figure(figsize=(20, 15))  # Créer une nouvelle figure
        plt.hist(liste, bins=50)
        plt.title("Distribution du nombre de CDS par gène")
        plt.xlabel("Nombre de CDS")
        plt.ylabel("Fréquence")
        plt.savefig(filename_graphe)
        plt.show()
                

if len(sys.argv) < 3:
    print("Usage: python script.py <chemin_vers_le_fichier_genome>")
    sys.exit(1) 
    sys.exit(2) 

fichier_fasta = sys.argv[1]
filename_graphe = sys.argv[2]

longueurs_cds = compte_cdsPerGene(fichier_fasta)

distributionGraph(longueurs_cds, filename_graphe)
