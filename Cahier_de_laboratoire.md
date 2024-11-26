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


## DATE : 06/11/2024

### Tâche : Script générant un tableau regroupant les besthits du blastp et les (plusieurs ou uniques) protéines qui ont hit sur celles ci (Martin)
- versions : python 3.13.0 / pandas 2.2.3
- match_besthits.py

- utilise le tableau généré par extract_besthits.py et génère un tableau avec en nom de colonne les best hits et dans chaque colonne les différentes protéines pour lesquelles on a obtenu ce besthit
- utilisé pour générér :  /data/projet6/data/1_work/Analyse_BLASTp/Oriolus_Galus_MatchBesthits.csv

### But : 
- permettra d'identifier à partir du tableau de sortie des protentielles protéines fragmentées ayant donc hit sur leurs homolgues communes 

### Problèmes :
- on retrouve pour quelques besthits 2 protéines mais pas plus

### A faire :
- relier les liens besthits/prot avec le score pour voir si les cas ou on a 2 potéines pour 1 besthit ont du sens
- refléchir à ne pas prendre que le besthit du blastp en fonction des scores en dessous
- a terme si cela permet d'identifier 2 protéines dans les protéomes fragmentés qui n'en sont en réalité qu'une seule, retrouver la séquence complète dans le génome 


## DATE : 18/11/2024

### Tâche : Analyse des décalages dans les alignements BLASTp (difstart et diffend) (Jérémie)

- Versions : Python 3.12.7 / Pandas 2.2.3 / Matplotlib 3.8.0 / Seaborn 0.12.0
- Developpement du Script: AnnotationCorrectionTest1.py

### But :
- Analyser les différences de décalage entre les positions de début (difstart) et de fin (diffend) des alignements dans les résultats de BLASTp, afin de déterminer si des protéines fragmentées peuvent être identifiées et de définir un critère pour considérer un alignement comme complet.

### Méthodes :
1. Tri des meilleurs alignements : Avant de procéder à l'analyse des décalages, nous avons trié les alignements pour ne conserver que les meilleurs résultats, en filtrant notamment les hits avec une valeur evalue égale à 0.0, qui sont considérés comme aberrants.
2. Calcul des différences de décalages : Calcul des décalages de début et de fin pour chaque alignement, après avoir appliqué un filtrage rigoureux.
3. Statistiques : Calcul des statistiques descriptives (moyenne, médiane, écart-type, etc.) pour les colonnes difstart et diffend.
4. Visualisation : Création d'histogrammes pour visualiser la distribution des différences de décalages.
5. Analyse des décalages à 0 : Comptage des cas où les décalages sont égaux à 0, ce qui pourrait suggérer un alignement parfait entre les protéines.

### Problèmes rencontrés :
- Une grande proportion des alignements ont des décalages proches de zéro pour difstart et diffend, ce qui pourrait indiquer que de nombreuses protéines sont déjà parfaitement alignées.
- Le nombre de décalages à zéro reste significatif malgré le filtrage, ce qui nécessite une analyse plus approfondie pour interpréter ces résultats.

### À faire :
1. Définir un seuil d'alignement complet basé sur les décalages et les statistiques observées.
2. Explorer les cas de décalages faibles pour mieux comprendre s'ils représentent des alignements de protéines fragmentées.
3. Analyser les protéines avec des décalages importants afin d'identifier celles qui pourraient être des protéines incomplètes ou mal alignées.


## DATE : 23/11/24 

### Tâche : Installation et exécution de AGAT (Jérémie)

- Versions : 
- agat		0.8.1
- perl		5.26.2
- conda		24.9.1
- python	3.12.7

- Script : AgatAutomatisationExecut.sh

- installation de Agat pour agat_sp_keep_longest_isoform.pl
- dl de tout les gff pour nos espèces
- automatisation de la commande pour l'appliquer à toutes les espèces 

### But :
- Récupérer les isoforme avec les séquences les plus longues de nos espèces pour permettre de meilleur alignements par BALSTP. 

### workflow : 

#### Télechargement de tout les fichiers gff : ( à exécuter dans chaque répertoire approprié (data\0_data\{nom_espece} )

- Gallus gallus : wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/016/699/485/GCF_016699485.2_bGalGal1.mat.broiler.GRCg7b/GCF_016699485.2_bGalGal1.mat.broiler.GRCg7b_genomic.gff.gz

- Calcarius ornatus : wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/013/397/715/GCA_013397715.1_ASM1339771v1/GCA_013397715.1_ASM1339771v1_genomic.gff.gz

- Piprites chloris : wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/013/399/295/GCA_013399295.1_ASM1339929v1/GCA_013399295.1_ASM1339929v1_genomic.gff.gz

- Herpetotheres cachinnans : wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/013/399/355/GCA_013399355.1_ASM1339935v1/GCA_013399355.1_ASM1339935v1_genomic.gff.gz

- Anseranas semipalmata : wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/013/399/115/GCA_013399115.1_ASM1339911v1/GCA_013399115.1_ASM1339911v1_genomic.gff.gz

- Taeniopygia guttata : wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/003/957/565/GCF_003957565.2_bTaeGut1.4.pri/GCF_003957565.2_bTaeGut1.4.pri_genomic.gff.gz

- Oriolus oriolus : wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/013/400/235/GCA_013400235.1_ASM1340023v1/GCA_013400235.1_ASM1340023v1_genomic.gff.gz

- tout dézipper : gunzip {nom_fichier_.zip}

#### Conda : Création d'un nouveau conda pour cette tache

- conda create --prefix /data/projet6/conda/carabin/agat_env python=3.9
- conda activate /data/projet6/conda/carabin/agat_env
- conda install perl

- instalastion AGAT :
- cpan install Module::Build
- conda install -c bioconda agat


#### commande : 

- conda activate conda/carabin/agat_env/

- /data/projet6/conda/carabin/agat_env/bin/agat_sp_keep_longest_isoform.pl --gff data/0_raw/Galus_raw_data/GCF_016699485.2_bGalGal1.mat.broiler.GRCg7b_genomic.gff --output /data/projet6/data/1_work/AGAT/Galus.AGAT.gff

-  Affin de faire ce processus sur toutes les espèces, création d'un script .sh

- nohup bash AgatAutomatisationExecut.sh > output_AgatScriptAutomatiosation.txt 2>&1




### Problèmes rencontrés :

### À faire :
- Analyse des résultats Agat agat_sp_keep_longest_isoform.pl.


## DATE 24/11/24

### Taches: Analyse de la fragmentation avec OMArk
Le but de cet analyse est de comparer en utilisant une autre méthode avant de valider les étaats de fragmentation trouvé en utilisant BUSCO
conda create -n omark_env python=3.9 -y
conda activate omark_env
conda install -c bioconda omark


### Problèmes :

### A faire :

 

### Tâche2 : Alignement BLASTP avec les fichier agat (Jérémie)

- Création de la nouvelle base de données BLASTp avec les séquences ref de Galus de chaque isoforme le plus long pour chaque protéine. 
- Création d'un script .sh pour lancer l'alignement de tout nos génomes sur la db Galus avec seulement les protéines issues de AGAT 


- Versions : 
- python	3.12.7
- bash      	5.1.16
- BLASTp    	2.12.0

- script : 
* LongestIsoformeNewFasta.py
* BLASTpAutomatisationExecut.sh


### But : 
- Permet de refaire les alignements avec suelement les isoformes les plus long de chaque protéine pour la référence Galus. 

### workflow : 

#### Création des fichiers fasta avec seulement les isoformes les plus long : 

- LongestIsoformeNewFasta.py : permet de créer un fichier fasta avec suelement les isoformes les plus longs, à partir du protéome entier de l'espèce (fasta)
et du gff sortie par AGAT agat_sp_keep_longest_isoform.pl.
- Usage : python script.py <whole_proteome> <gffAGAT> <fastaOUTPUT>
- <whole_proteome> : Chemin vers le fichier FASTA contenant les séquences protéiques complètes
- <gffAGAT>        : Chemin vers le fichier GFF annoté par AGAT
- <fastaOUTPUT>    : Chemin où le fichier FASTA de sortie sera généré

- commande : python src/LongestIsoformeNewFasta.py data/0_raw/Galus_raw_data/GCF_016699485.2_bGalGal1.mat.broiler.GRCg7b_protein.faa data/1_work/AGAT/Galus_AGAT.gff data/1_work/AGAT/Galus_AGAT_proteome.faa

- création de la nouvelle db pour faire les BLASTP à partir du fichier AGTA pour la référence : 

- makeblastdb -in <chemin_proteome_gallus_gallus> -dbtype prot -parse_seqids -out gallus_AGAT_db

- commande : makeblastdb -in data/1_work/AGAT/Galus_AGAT_proteome.faa -dbtype prot -parse_seqids -out /data/projet6/data/1_work/AGAT/gallus_AGAT_db


- BlastP avec la nouvelle db : 

- blastp -query <chemin_proteome_query> -db <nom_blastdb> -out <chemin_fichier_output>

- commande :  blastp -query /data/projet6/data/0_raw/Oriolus_raw_data/GCA_013400235.1_ASM1340023v1_protein.faa -db /data/projet6/data/1_work/AGAT/dataBase_AGAT_Gallus/gallus_AGAT_db -out /data/projet6/data/1_work/Analyse_AGAT_BLASTp/BLASTp_refGalius_Orioluse.txt

automatisation pour toute les espèces : nohup bash /data/projet6/src/BLASTpAutomatisationExecut.sh > /data/projet6/logs/BLASTpAutomatisationExecut.log 2>&1 &


### Problèmes rencontrés :
- AGAT pour les protéomes de nos oiseaux sachant qu'ils sont de taille raisonnable ? 

### À faire :
- regarder resultats 
sationExecut.log 2>&1 &
[1] 2738950

## Date : 25/11/24 

### Tache1 : Relancement des BLASTp (Jérémie)

- BLASTp n'a pas marché avec le script : BLASTpAutomatisationExecut.sh

- Commande à la main : 

* nohup blastp -query /data/projet6/data/0_raw/Calcarius_raw_data/GCA_013397715.1_ASM1339771v1_protein.faa \
-db /data/projet6/data/1_work/AGAT/dataBase_AGAT_Gallus/gallus_AGAT_db \
-out /data/projet6/data/1_work/Analyse_AGAT_BLASTp/BLASTp_refGallus_Calcarius.txt \
-outfmt 6 -max_target_seqs 1 2>> /data/projet6/blastp_errors.txt &

* nohup blastp -query /data/projet6/data/0_raw/Piprites_raw_data/GCA_013399295.1_ASM1339929v1_protein.faa \
-db /data/projet6/data/1_work/AGAT/dataBase_AGAT_Gallus/gallus_AGAT_db \
-out /data/projet6/data/1_work/Analyse_AGAT_BLASTp/BLASTp_refGallus_Piprites.txt \
-outfmt 6 -max_target_seqs 1 2>> /data/projet6/blastp_errors.txt &

* nohup blastp -query /data/projet6/data/0_raw/Herpetotheres_raw_data/GCA_013399355.1_ASM1339935v1_protein.faa \
-db /data/projet6/data/1_work/AGAT/dataBase_AGAT_Gallus/gallus_AGAT_db \
-out /data/projet6/data/1_work/Analyse_AGAT_BLASTp/BLASTp_refGallus_Herpetotheres.txt \
-outfmt 6 -max_target_seqs 1 2>> /data/projet6/blastp_errors.txt &

* nohup blastp -query /data/projet6/data/0_raw/Anseranas_raw_data/GCA_013399115.1_ASM1339911v1_protein.faa \
-db /data/projet6/data/1_work/AGAT/dataBase_AGAT_Gallus/gallus_AGAT_db \
-out /data/projet6/data/1_work/Analyse_AGAT_BLASTp/BLASTp_refGallus_Anseranas.txt \
-outfmt 6 -max_target_seqs 1 2>> /data/projet6/blastp_errors.txt &

* nohup blastp -query /data/projet6/data/0_raw/Oriolus_raw_data/GCA_013400235.1_ASM1340023v1_protein.faa \
-db /data/projet6/data/1_work/AGAT/dataBase_AGAT_Gallus/gallus_AGAT_db \
-out /data/projet6/data/1_work/Analyse_AGAT_BLASTp/BLASTp_refGallus_Oriolus.txt \
-outfmt 6 -max_target_seqs 1 2>> /data/projet6/blastp_errors.txt &

### tache2 : création d'un script pour extraire le protéine Gallus après le BlastP (jeremie)

script : ExtractProtBalst.py


commande : 

* nohup python /data/projet6/src/ExtractProtBalst.py /data/projet6/data/1_work/Analyse_AGAT_BLASTp/BLASTp_refGallus_Oriolus.txt /data/projet6/data/0_raw/Galus_raw_data/GCF_016699485.2_bGalGal1.mat.broiler.GRCg7b_protein.faa /data/projet6/data/1_work/DataFasta4Miniprot/FastaBestHit_Oriolus.faa &

* nohup python /data/projet6/src/ExtractProtBalst.py /data/projet6/data/1_work/Analyse_AGAT_BLASTp/BLASTp_refGallus_Anseranas.txt /data/projet6/data/0_raw/Galus_raw_data/GCF_016699485.2_bGalGal1.mat.broiler.GRCg7b_protein.faa /data/projet6/data/1_work/DataFasta4Miniprot/FastaBestHit_Anseranas.faa &

* nohup python /data/projet6/src/ExtractProtBalst.py /data/projet6/data/1_work/Analyse_AGAT_BLASTp/BLASTp_refGallus_Calcarius.txt /data/projet6/data/0_raw/Galus_raw_data/GCF_016699485.2_bGalGal1.mat.broiler.GRCg7b_protein.faa /data/projet6/data/1_work/DataFasta4Miniprot/FastaBestHit_Calcarius.faa &

* nohup python /data/projet6/src/ExtractProtBalst.py /data/projet6/data/1_work/Analyse_AGAT_BLASTp/BLASTp_refGallus_Herpetotheres.txt /data/projet6/data/0_raw/Galus_raw_data/GCF_016699485.2_bGalGal1.mat.broiler.GRCg7b_protein.faa /data/projet6/data/1_work/DataFasta4Miniprot/FastaBestHit_Herpetotheres.faa &

* nohup python /data/projet6/src/ExtractProtBalst.py /data/projet6/data/1_work/Analyse_AGAT_BLASTp/BLASTp_refGallus_Piprites.txt /data/projet6/data/0_raw/Galus_raw_data/GCF_016699485.2_bGalGal1.mat.broiler.GRCg7b_protein.faa /data/projet6/data/1_work/DataFasta4Miniprot/FastaBestHit_Piprites.faa &


### A faire : 
- refaire ces commandes quand tout les blastp auront fini de tourner. -> FAIT


### Tache3 : Alignement protéine - genome avec miniprot. (Jeremie)

- Téléchargement : de tout les .fna 

* wget -P /data/projet6/data/0_raw/Oriolus_raw_data https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/013/400/235/GCA_013400235.1_ASM1340023v1/GCA_013400235.1_ASM1340023v1_cds_from_genomic.fna.gz

* wget -P /data/projet6/data/0_raw/Calcarius_raw_data https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/013/397/715/GCA_013397715.1_ASM1339771v1/GCA_013397715.1_ASM1339771v1_cds_from_genomic.fna.gz

* wget -P /data/projet6/data/0_raw/Piprites_raw_data/ https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/013/399/295/GCA_013399295.1_ASM1339929v1/GCA_013399295.1_ASM1339929v1_cds_from_genomic.fna.gz

* wget -P /data/projet6/data/0_raw/Herpetotheres_raw_data/ https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/013/399/355/GCA_013399355.1_ASM1339935v1/GCA_013399355.1_ASM1339935v1_cds_from_genomic.fna.gz

* wget -P /data/projet6/data/0_raw/Anseranas_raw_data/ https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/013/399/115/GCA_013399115.1_ASM1339911v1/GCA_013399115.1_ASM1339911v1_cds_from_genomic.fna.gz

* gunzip /data/projet6/data/0_raw/Oriolus_raw_data/*.gz
* gunzip /data/projet6/data/0_raw/Calcarius_raw_data/*.gz
* gunzip /data/projet6/data/0_raw/Piprites_raw_data/*.gz
* gunzip /data/projet6/data/0_raw/Herpetotheres_raw_data/*.gz
* gunzip /data/projet6/data/0_raw/Anseranas_raw_data/*.gz


- commandes Miniprot : 


conda activate /data/projet6/conda/carabin/miniprot_env/


- indexation des génomes : 

 miniprot -d /data/projet6/data/1_work/DataFasta4Miniprot/indexOriolus.mpi  /data/projet6/data/0_raw/Oriolus_raw_data/GCA_013400235.1_ASM1340023v1_cds_from_genomic.fna

miniprot -t8 -d /data/projet6/data/1_work/DataFasta4Miniprot/indexCalcarius.mpi /data/projet6/data/0_raw/Calcarius_raw_data/GCA_013397715.1_ASM1339771v1_cds_from_genomic.fna

miniprot -t8 -d /data/projet6/data/1_work/DataFasta4Miniprot/indexPiprites.mpi /data/projet6/data/0_raw/Piprites_raw_data/GCA_013399295.1_ASM1339929v1_cds_from_genomic.fna

miniprot -t8 -d /data/projet6/data/1_work/DataFasta4Miniprot/indexHerpetotheres.mpi /data/projet6/data/0_raw/Herpetotheres_raw_data/GCA_013399355.1_ASM1339935v1_cds_from_genomic.fna

miniprot -t8 -d /data/projet6/data/1_work/DataFasta4Miniprot/indexAnseranas.mpi /data/projet6/data/0_raw/Anseranas_raw_data/GCA_013399115.1_ASM1339911v1_cds_from_genomic.fna


- Alignement :

miniprot /data/projet6/data/1_work/DataFasta4Miniprot/indexOriolus.mpi /data/projet6/data/1_work/DataFasta4Miniprot/FastaBestHit_Oriolus.faa > /data/projet6/data/1_work/Analyse_Miniprot/Align_GalusProt_on_OriolusGenome.paf

miniprot /data/projet6/data/1_work/DataFasta4Miniprot/indexCalcarius.mpi /data/projet6/data/1_work/DataFasta4Miniprot/FastaBestHit_Calcarius.faa > /data/projet6/data/1_work/Analyse_Miniprot/Align_GalusProt_on_CalcariusGenome.paf

miniprot /data/projet6/data/1_work/DataFasta4Miniprot/indexPiprites.mpi /data/projet6/data/1_work/DataFasta4Miniprot/FastaBestHit_Piprites.faa > /data/projet6/data/1_work/Analyse_Miniprot/Align_GalusProt_on_PipritesGenome.paf

miniprot /data/projet6/data/1_work/DataFasta4Miniprot/indexHerpetotheres.mpi /data/projet6/data/1_work/DataFasta4Miniprot/FastaBestHit_Herpetotheres.faa > /data/projet6/data/1_work/Analyse_Miniprot/Align_GalusProt_on_HerpetotheresGenome.paf

miniprot /data/projet6/data/1_work/DataFasta4Miniprot/indexAnseranas.mpi /data/projet6/data/1_work/DataFasta4Miniprot/FastaBestHit_Anseranas.faa > /data/projet6/data/1_work/Analyse_Miniprot/Align_GalusProt_on_AnseranasGenome.paf



### Problèmes : 

- mauvaise indexation du génome (k-mers = 0 ) forcement pas d'alignement -> Ca marche (pas mettre paramètres)

- voir : https://lh3.github.io/miniprot/miniprot.html
"""
SYNOPSIS
* Indexing a genome (recommended as indexing can be slow and memory hungry):
miniprot [-t nThreads] -d ref.mpi ref.fna
* Aligning proteins to a genome:

miniprot [-t nThreads] ref.mpi protein.faa > output.paf
miniprot [-t nThreads] ref.fna protein.faa > output.paf
"""


### A faire : 
- a lancer après avoir lancer ExtractProtBalst.py après avoir fait les BlastP -> fait

- Maintenant qu'on à les postions de chaque gènes (grace au Mapping des protéine de réf homologue) on peut vérifier et annoter nos génomes d'oiseaux. 