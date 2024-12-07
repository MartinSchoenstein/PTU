Descritpions de l'architecture

description générale : 

projet6/
          /data
          /src
          /conda
	     /archive
          /pipeline
          README.txt
          Cahier_de_laboratoire.md



archive/ : Ce répertoire contient d'anciennes versions des scripts, des tests moins utilisés, ainsi que des données qui ne sont plus utilisées ou qui ne sont plus pertinentes pour l'analyse actuelle.

src/ : contient les scripts

conda/ : contient les environnements conda, les dossiers/fichiers générés par cela et les fichiers les décrivant

pipeline/ : contient les scripts du pipeline de correction de génome ainsi qu'un README.txt et un schéma expliquant son fonctionnement.

data/ :
 
0_raw/ : Contient les données brutes non modifiées, prêtes à être utilisées dans les scripts. Ce sont les fichiers de base d'où part le traitement.

1_work/ : Contient les données intermédiaires générées par les scripts, qui peuvent être modifiées ou réanalysées. Il peut y avoir plusieurs versions des mêmes fichiers avant d'obtenir les données finales. Contient un dossier par type d'analyse/processus.

2_final/ : Contient les résultats finaux des analyses ou traitements, qui sont sauvegardés comme version finale des données, prêtes à être utilisées ou partagées.   

2_final/Correction/ : Contient un dossier par espèce avec les annotations corrigées. 
