import pandas as pd

def length_from_fasta(path):
    fasta = open(path, "r")

    df = pd.DataFrame(columns = ["ID", "Length"])

    count_df = 0
    length = 0

    for l in fasta:
        if l[0] == ">":
            if length == 0:
                split = l.split(" ")
                df.loc[count_df, "ID"] = split[0] 
            if length != 0:
                df.loc[count_df, "Length"] = length
                count_df = count_df + 1
                split = l.split(" ")
                df.loc[count_df, "ID"] = split[0]
                length = 0
        else:
            length = length + len(l) -1
    df.loc[count_df, "Length"] = length

    return(df)