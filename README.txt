Descritpions de l'architecture

description générale : 

projet6/
          /data
          /src
          README.md
          Cahier_de_laboratoire.md


data/
     /0_raw
     /1_work
          /Analyse_BLASTp
          /Analyse_BUSCO
          /gallus_db_blastp
     /2_final 

0_raw/ : Contient les données brutes non modifiées, prêtes à être utilisées dans les scripts. Ce sont les fichiers de base d'où part le traitement.

1_work/ : Contient les données intermédiaires générées par les scripts, qui peuvent être modifiées ou réanalysées. Il peut y avoir plusieurs versions des mêmes fichiers avant d'obtenir les données finales.

2_final/ : Contient les résultats finaux des analyses ou traitements, qui sont sauvegardés comme version finale des données, prêtes à être utilisées ou partagées.   

/Analyse_BLASTp : contient les résultats sous fichier txt et leurs traitements des blastp effectué entre protéomes fragmentés et protéome de référence

/Analyse_BUSCO  : toutes les informations et résultats des runs Busco pour chaque protéome

/gallus_db_blastp : database blastp contenant le protéome de gallus, utilisée pour les blastp 

src/ : contient les scripts

     CDS_FragmentationAnalyse.py : génère des graphs de distribution des cds par gène dans un génome à partir d'un fichier fasta (exemple résultats : /data/projet6/data/2_final/distribution.pdf )
     extract_besthit.py : génère un tableau csv contenant le besthit pour chaque query blastp avec les caractéristiques du hit (exemple output : /data/projet6/data/1_work/Analyse_BLASTp/Oriolus_Galus_Besthit.csv)