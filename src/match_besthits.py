import pandas as pd

df = pd.read_csv("/data/projet6/data/1_work/Analyse_BLASTp/Oriolus_Galus_Besthit.csv")

dico = {}

for x in range(0, len(df)):
    if df["best_hit"][x] in dico.keys():
        dico[df["best_hit"][x]] = [dico[df["best_hit"][x]], df["query"][x]]
    else:
        dico[df["best_hit"][x]] = [df["query"][x]]


df_frag = pd.DataFrame(dict([(key, pd.Series(value)) for key, value in dico.items()]))

df_frag.to_csv('/data/projet6/data/1_work/Analyse_BLASTp/Oriolus_Galus_MatchBesthits.csv', index=False)