import pandas as pd
from LengthFromFasta import length_from_fasta

df_length = length_from_fasta("/data/projet6/data/1_work/AGAT/Galus_AGAT_proteome.faa")
df = pd.DataFrame(columns = ["#Query", "Ref", "ratio"])
blast = open("/data/projet6/data/1_work/Analyse_AGAT_BLASTp/BLASTp_refGallus_Piprites.txt", "r")

count = 0
for l in blast:
    split = l.split("\t")
    if count == 0:
        df.loc[count, "#Query"] = split[0]
        df.loc[count, "Ref"] = split[1]
        df.loc[count, "ratio"] = int(split[3])
        for i in range(0, len(df_length)):
            if df_length.loc[i, "ID"][1:] == split[1]:
                df.loc[count, "ratio"] = int(split[3]) / int(df_length.loc[i, "Length"])
        count = count + 1
    elif split[1] != df.loc[count -1, "Ref"]:
        df.loc[count, "#Query"] = split[0]
        df.loc[count, "Ref"] = split[1]
        df.loc[count, "ratio"] = int(split[3])
        for i in range(0, len(df_length)):
            if df_length.loc[i, "ID"][1:] == split[1]:
                df.loc[count, "ratio"] = int(split[3]) / int(df_length.loc[i, "Length"])
        count = count + 1

df.to_csv('/data/projet6/data/1_work/recovery_piprites.csv', index=False)
