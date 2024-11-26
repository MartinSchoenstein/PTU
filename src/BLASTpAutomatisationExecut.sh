/bin/bash

# Liste des fichiers fasta
FASTA_FILES=(
    "/data/projet6/data/0_raw/Calcarius_raw_data/GCA_013397715.1_ASM1339771v1_protein.faa"
    "/data/projet6/data/0_raw/Piprites_raw_data/GCA_013399295.1_ASM1339929v1_protein.faa"
    "/data/projet6/data/0_raw/Herpetotheres_raw_data/GCA_013399355.1_ASM1339935v1_protein.faa"
    "/data/projet6/data/0_raw/Anseranas_raw_data/GCA_013399115.1_ASM1339911v1_protein.faa"
    "/data/projet6/data/0_raw/Oriolus_raw_data/GCA_013400235.1_ASM1340023v1_protein.faa"
)

# Liste des noms de fichiers de sortie
OUTPUT_FILES=( 
    "Calcarius.txt"
    "Piprites.txt"
    "Herpetotheres.txt"
    "Anseranas.txt"
    "Oriolus.txt"
    
)

# Boucle sur les fichiers et exécution du script
for i in "${!FASTA_FILES[@]}"; do
    fasta_file="${FASTA_FILES[$i]}"
    output_file="${OUTPUT_FILES[$i]}"
    
    # Vérification si le fichier fasta existe
    if [[ ! -f "$fasta_file" ]]; then
        echo "Erreur : Le fichier $fasta_file n'existe pas !"
        continue
    fi
    
    # Exécution du script AGAT pour chaque fichier
    echo "Processing $fasta_file..."
    blastp -query "$fasta_file" -db /data/projet6/data/1_work/AGAT/dataBase_AGAT_Gallus/gallus_AGAT_db -out /data/projet6/data/1_work/Analyse_AGAT_BLASTp/BLASTp_refGallus_"$output_file" -outfmt 6  -max_target_seqs 2 2>> /data/projet6/blastp_errors.txt
    
    # Vérification si le script a réussi
    if [[ $? -eq 0 ]]; then
        echo "Output written to $output_file"
    else
        echo "Erreur lors du traitement de $fasta_file"
    fi
done
