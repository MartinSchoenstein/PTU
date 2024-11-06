# Cahier de laboratoire Projet 6 

## 09/10/2024

### Taches:
* Mise en place de l'architecture de l'espace de travail (serveur tuto.lbgi.fr / data / Projet6) (Jérémie)
* Ecriture du fichier README.md pour expliquer la structure (Jérémie et Théo)
* Création du GIT et du GITHUB (Martin)
* recherche de logiciel et approche pour caractériser la Fragmentation (Théo)

### Problèmes : 
* Push les GIT pour les collaborateurs

### A faire :
* Télécharger les data
* Trouver une approche pour caractériser les fragments (avec conda  - QUAST ? galaxy ? BUSCO ? )


## 14/10/2024 :

### Taches: 
* teste sur la caractérisation de la fragmentation (Jérémie)

téléchargement pour l'espèce 'Piprites chloris' :

wget -P data/ https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/013/399/295/GCA_013399295.1_ASM1339929v1/GCA_013399295.1_ASM1339929v1_cds_from_genomic.fna.gz
wget -P data/ https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/013/399/295/GCA_013399295.1_ASM1339929v1/GCA_013399295.1_ASM1339929v1_genomic.gff.gz
wget -P data/ https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/013/399/295/GCA_013399295.1_ASM1339929v1/GCA_013399295.1_ASM1339929v1_protein.faa.gz

gunzip *.gz


comptage du nombre de gène : 

grep -c ">lcl" GCA_013399295.1_ASM1339929v1_cds_from_genomic.fna 

15627 


grep ">lcl" 0_raw/GCA_013399295.1_ASM1339929v1_cds_from_genomic.fna > 1_work/cds_localisationPerGene.txt

exemple de donnée : 
>lcl|VXAH01000001.1_cds_NXK29741.1_10 [gene=Calhm5] [locus_tag=PIPCHL_R09291] [protein=CAHM5 protein] [partial=5',3'] [protein_id=NXK
29741.1] [location=join(<1891222..1891761,1894659..>1895045)] [gbkey=CDS]

-> gène "normal"


>lcl|VXAH01000002.1_cds_NXK29772.1_82 [gene=Eya4] [locus_tag=PIPCHL_R09283] [protein=EYA4 protein] [partial=5',3'] [protein_id=NXK297
72.1] [location=join(<6651492..6651541,6672803..6672927,6674055..6674123,6679182..6679274,6685053..6685119,6687116..6687258,6687398..
6687541,6688392..6688471,6688841..6689024,6695641..6695777,6697360..6697443,6706194..6706283,6712552..6712610,6712723..6712883,671501
1..6715125,6716882..6717003,6717938..6718038,6719651..>6719728)] [gbkey=CDS]

-> gène fragmenté 

https://www.nature.com/articles/nature03154 -> les oiseaux auraient moins d'exon que les vertébrés (5 à 7 exons) 


Comparaison avec Gallus Gallus : 

wget -P data/ https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/016/699/485/GCF_016699485.2_bGalGal1.mat.broiler.GRCg7b/GCF_016699485.2_bGalGal1.mat.broiler.GRCg7b_cds_from_genomic.fna.gz

src : pour excuter script
CDS_FragmentationAnalyse.py pour la distribution de la fragmentation


-> voir résultats 2_final : distribution.pdf 
-> ne montre pas la fragmentation par le nombre de CDS 

### Problèmes : 
* Le nombre de CDS élevé représente vraiment un nombre de fragmentation élevé? NON


## DATE 23/10/24

### Taches:

#### Création de l'environnement busco (Theo)

##### la commande pour activer l'environnement : 
- conda activate busco_env dans conda/dessaint
- version : Busco 5.8.0

#### test d'assemblage sur Busco avec Piprites (Theo et Jérémie)
- Détails des options : busco -i proteins.fasta -o analyse_proteins -l eukaryota_odb10 - -m proteins --out_path /chemin/vers/dossier_sortie
- -i : Chemin vers ton fichier FASTA contenant les séquences protéiques.
- -o : Nom du projet. Un dossier avec ce nom sera créé pour les résultats.
- -l : Ligneage de la base de données BUSCO, eukaryota_odb10.
- -m : Mode d'analyse, ici proteins pour indiquer que l'analyse concerne des séquences protéiques.
- --out_path : Chemin vers le dossier où tu souhaites que les résultats soient enregistrés.

-  fichier fasta protéique piprites : wget -P data/ https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/013/399/295/GCA_013399295.1_ASM1339929v1/GCA_013399295.1_ASM1339929v1_protein.faa.gz

- fichier fasta protéique Galus : 
wget -P data/ https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/016/699/485/GCF_016699485.2_bGalGal1.mat.broiler.GRCg7b/GCF_016699485.2_bGalGal1.mat.broiler.GRCg7b_cds_from_genomic.fna.gz

mkdir Oriolus_raw_data
wget -P ./Oriolus_raw_data/ https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/013/400/235/GCA_013400235.1_ASM1340023v1/GCA_013400235.1_ASM1340023v1_protein.faa.gz
gunzip ./Oriolus_raw_data/*

mkdir Calcarius_raw_data
wget -P ./Calcarius_raw_data/ https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/013/397/715/GCA_013397715.1_ASM1339771v1/GCA_013397715.1_ASM1339771v1_protein.faa.gz
gunzip ./Calcarius_raw_data/*

mkdir Herpetotheres_raw_data
wget -P ./Herpetotheres_raw_data/ https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/013/399/355/GCA_013399355.1_ASM1339935v1/GCA_013399355.1_ASM1339935v1_protein.faa.gz
gunzip ./Herpetotheres_raw_data/*

mkdir Anseranas_raw_data
wget -P ./Anseranas_raw_data/ https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/013/399/115/GCA_013399115.1_ASM1339911v1/GCA_013399115.1_ASM1339911v1_protein.faa.gz
gunzip ./Anseranas_raw_data/*

mkdir Taeniopygia_raw_data
wget -P ./Taeniopygia_raw_data/ https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/003/957/565/GCF_003957565.2_bTaeGut1.4.pri/GCF_003957565.2_bTaeGut1.4.pri_protein.faa.gz
gunzip ./Taeniopygia_raw_data/*



- busco -i Piprites_raw_data/GCA_013399295.1_ASM1339929v1_protein.faa -o analyse_Piprites  -l eukaryota_odb10 -m proteins
Comparer avec base de données des eukaryotes
- busco -i Piprites_raw_data/GCA_013399295.1_ASM1339929v1_protein.faa -o analyse_Piprites_metazo  -l metazoa_odb10 -m proteins
Comparer avec base de données des metazoaires
- busco -i Piprites_raw_data/GCA_013399295.1_ASM1339929v1_protein.faa -o analyse_Piprites_aves  -l aves_odb10 -m proteins
Comparer avec base de données des oiseaux
- mv analyse_Piprites* ./Piprite_work_data/
Pour tout déplacer dans le dossier work data de l'espece

### Problèmes :
- Seulement Martin a les droits de /data

### A faire :
- déplacer dossier Piprites/Galus_raw_data dans 0_raw
- deplacer les analyses busco dans 1_work


## DATE  25/10/24

### Blastp entre un protéome fragmenté (Oriolus) et un protéome de référence (Galus) (Martin):: 
version : blastp 2.12.0

makeblastdb -in <chemin_proteome> -dbtype prot -parse_seqids -out <nom_db>

blastp -query <chemin_proteome_query> -db <nom_blastdb> -out <chemin_fichier_output>

### Problèmes :
- long et génère un lourd fichier, beaucoup de résultats

### A faire :
- Traiter le fichier de résultats afin de pouvoir mettre en avant plusieurs protéines d'Oriolus qui se mapperaint sur une seule de Galus et des protéines d'Oriolus qui ne se mapperaient pas sur toute la longueur de la protéine de référence


## DATE 05/11/24

### BUSCO sur les génomes de Anseranas, Galus, Oriolus, Calcarius, Herpetotheres et Taeniopygia (Theo)
- version : Busco 5.8.0

##### but :
- pouvoir faire un état des lieux des différents génomes en les comparant à la base de données de BUSCO pour les oiseaux, on obtient les pourcentages de complétudes du génomes, de fragmentation et de manquant.

### Script permettant d'extraire les best hits et ses caractéristiques sous forme d'un tableau à partir d'un résulat blast (Martin)
- versions : python 3.13.0 / pandas 2.2.3

##### but : 
- pouvoir mettre en avant des protéines de nos protéomes d'intêret potentiellement fragmentées qui hit à plusieurs sur la même protéine d'un protéome de référence

##### résulats :
- script extract_besthit.py
- génère un fichier csv

### nouveau BlastP pour avoir la sortie sous forme de TSV (Jérémie)
version : blastp 2.12.0

##### but : 
- Cette analyse nous permettra d'analyser le recouvrement avec l'homologue complet grâce à un programme Python.
- Objectif : Analyser les protéines d'Oriolus qui sont plus longues ou plus courtes que celles de la référence (Galus gallus), afin d'évaluer l'annotation du génome de référence par comparaison éventuelle des séquences nucléiques.

##### commandes : 

makeblastdb -in <chemin_proteome_gallus_gallus> -dbtype prot -parse_seqids -out gallus_db

blastp -query <chemin_proteome_oriolus> -db gallus_db -out oriolus_vs_gallus.txt -outfmt 6


makeblastdb -in data/0_raw/Galus_raw_data/GCF_016699485.2_bGalGal1.mat.broiler.GRCg7b_protein.faa -dbtype prot -parse_seqids -out data/1_work/gallus_db

blastp -query data/0_raw/Oriolus_raw_data/GCA_013400235.1_ASM1340023v1_protein.faa -db data/1_work/gallus_db/gallus_db -out ./oriolus_vs_gallus_TSV.txt -outfmt 6

##### format du fichier de sortie en TSV :

query_id    subject_id    100.0    100    0    0    1    100    1    100    0.0    200.0


qseqid : Identifiant de la séquence de la requête (query).
sseqid : Identifiant de la séquence sujet (subject).
pident : Pourcentage d'identité de l'alignement.
length : Longueur de l'alignement.
mismatch : Nombre de mismatches (écarts) dans l'alignement.
gapopen : Nombre de gaps ouverts dans l'alignement.
qstart : Position de départ de l'alignement sur la séquence de la requête.
qend : Position de fin de l'alignement sur la séquence de la requête.
sstart : Position de départ de l'alignement sur la séquence sujet.
send : Position de fin de l'alignement sur la séquence sujet.
evalue : Valeur E, qui indique la significativité de l'alignement (plus la valeur est faible, plus l'alignement est significatif).
bitscore : Score en bits, qui mesure la qualité de l'alignement.

##### commande pour le faire tourner en fond :

nohup blastp -query data/0_raw/Oriolus_raw_data/GCA_013400235.1_ASM1340023v1_protein.faa -db data/1_work/gallus_db/gallus_db -out ./oriolus_vs_gallus_TSV.txt -outfmt 6 &

id nohup : [1] 1981611

### Problèmes :

### A faire :
- analyser les résultats TSV 


## DATE

### Taches: 

### Problèmes :

### A faire :


## DATE

### Taches: 

### Problèmes :

### A faire :