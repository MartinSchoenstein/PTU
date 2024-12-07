import pandas as pd 
from LengthFromFasta import length_from_fasta

#df = pd.read_csv("/data/projet6/data/1_work/recovery_anseranas.csv")
#blast = open("/data/projet6/data/1_work/Analyse_AGAT_BLASTp/BLASTp_refGallus_Anseranas.txt", "r")
#length = pd.read_csv("/data/projet6/data/1_work/length_prot_Gallus.csv")

def frag_pos(recov, blast):
    length = pd.read_csv("/data/projet6/data/1_work/length_prot_Gallus.csv")
    df = pd.read_csv(recov)
    blast = open(blast, "r")
    fragments = []
    for x in range(0, len(df)):
        if df.iloc[x, 2] < 0.6:
            fragments.append(df.iloc[x, 0])

    output = pd.DataFrame(columns = ["#Ref", "Start", "Length", "Ratio"])
    count = 0
    for l in blast:
        split = l.split("\t")
        for x in fragments:
            if x == split[0]:
                if count == 0:
                    output.loc[count, "#Ref"] = split[1]
                    output.loc[count, "Start"] = split[8]
                    for y in range(0, len(length)):
                        if length.loc[y, "ID"][1:] == split[1]:
                            output.loc[count, "Length"] = length.loc[y, "Length"]
                            output.loc[count, "Ratio"] = int(output.loc[count, "Start"])/ int(output.loc[count, "Length"])
                            count = count + 1
                elif output.loc[count -1 , "#Ref"] != split[1]:
                    output.loc[count, "#Ref"] = split[1]
                    output.loc[count, "Start"] = split[8]
                    for y in range(0, len(length)):
                        if length.loc[y, "ID"][1:] == split[1]:
                            output.loc[count, "Length"] = length.loc[y, "Length"]
                            output.loc[count, "Ratio"] = int(output.loc[count, "Start"])/ int(output.loc[count, "Length"])
                            count = count + 1
    return output

#output.to_csv("/data/projet6/data/1_work/fragment_positions_anseranas.csv")