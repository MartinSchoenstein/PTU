#!/bin/bash

# Liste des fichiers GFF
GFF_FILES=(
    "/data/projet6/data/0_raw/Galus_raw_data/GCF_016699485.2_bGalGal1.mat.broiler.GRCg7b_genomic.gff"
    "/data/projet6/data/0_raw/data/Calcarius_raw_data/GCA_013397715.1_ASM1339771v1_genomic.gff"
    "/data/projet6/data/0_raw/Piprites_raw_data/GCA_013399295.1_ASM1339929v1_genomic.gff"
    "/data/projet6/data/0_raw/Herpetotheres_raw_data/GCA_013399355.1_ASM1339935v1_genomic.gff"
    "/data/projet6/data/0_raw/Anseranas_raw_data/GCA_013399115.1_ASM1339911v1_genomic.gff"
    "/data/projet6/data/0_raw/Taeniopygia_raw_data/GCF_003957565.2_bTaeGut1.4.pri_genomic.gff"
    "/data/projet6/data/0_raw/Oriolus_raw_data/GCA_013400235.1_ASM1340023v1_genomic.gff"
)

# Liste des noms de fichiers de sortie
OUTPUT_FILES=( 
    "/data/projet6/data/1_work/AGAT/Galus_AGAT.gff"
    "/data/projet6/data/1_work/AGAT/Calcarius_AGAT.gff"
    "/data/projet6/data/1_work/AGAT/Piprites_AGAT.gff"
    "/data/projet6/data/1_work/AGAT/Herpetotheres_AGAT.gff"
    "/data/projet6/data/1_work/AGAT/Anseranas_AGAT.gff"
    "/data/projet6/data/1_work/AGAT/Taeniopygia_AGAT.gff"
    "/data/projet6/data/1_work/AGAT/Oriolus_AGAT.gff"
)

# Boucle sur les fichiers et exécution du script
for i in "${!GFF_FILES[@]}"; do
    gff_file="${GFF_FILES[$i]}"
    output_file="${OUTPUT_FILES[$i]}"
    
    # Vérification si le fichier GFF existe
    if [[ ! -f "$gff_file" ]]; then
        echo "Erreur : Le fichier $gff_file n'existe pas !"
        continue
    fi
    
    # Exécution du script AGAT pour chaque fichier
    echo "Processing $gff_file..."
    /data/projet6/conda/carabin/agat_env/bin/agat_sp_keep_longest_isoform.pl --gff "$gff_file" --output "$output_file"
    
    # Vérification si le script a réussi
    if [[ $? -eq 0 ]]; then
        echo "Output written to $output_file"
    else
        echo "Erreur lors du traitement de $gff_file"
    fi
done

