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

### A faire :


## DATE 23/10/24

### Taches: 
#### Création de l'environnement busco (Theo), la commande pour activer l'environnement : 
conda activate busco_env dans conda/dessaint
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
- Seulement Martin a les droits de data 
### A faire :
- déplacer dossier Piprites/Galus_raw_data dans 0_raw
- deplacer les analyses busco dans 1_work


## DATE  25/10/24

### Taches: 
- Blast entre une protéome fragmenté (Oriolus) et un protéome de référence (Galus) :

makeblastdb -in <chemin_proteome> -dbtype prot -parse_seqids -out <nom_db>

blastp -query <chemin_proteome_query> -db <nom_blastdb> -out <chemin_fichier_output>

### Problèmes :
- long et génère un lourd fichier, beaucoup de résultats
### A faire :
- Traiter le fichier de résultats afin de pouvoir mettre en avant plusieurs protéines d'Oriolus qui se mapperaint sur une seule de Galus et des protéines d'Oriolus qui ne se mapperaient pas sur toute la longueur de la protéine de référence


## DATE 05/11/24

### Taches: 
- BUSCO sur les génomes de Anseranas, Galus, Oriolus, Calcarius, Herpetotheres et Taeniopygia (Theo)
- 

### Problèmes :

### A faire :



## DATE

### Taches: 

### Problèmes :

### A faire :


## DATE

### Taches: 

### Problèmes :

### A faire :