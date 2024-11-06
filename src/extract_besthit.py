import pandas as pd

file = open("/data/projet6/data/1_work/blastp_Oriolus_Galus.txt", "r")

query = ""
line_query = 0
length_query = ""
hit = ""
e_value = ""
score = ""

df = pd.DataFrame(columns= ["query", "length_query", "best_hit", "e_value", "score"])

line_count = 0
for x in file:
    line_count = line_count + 1
    if x[0:6] == "Query=":
        query = x[7:]
        line_query = line_count
        print(query)
    if x[0:7] == "Length=" and line_count == line_query + 2:
        length_query = x[7:]
        print(length_query)
    if x[1:2] == "P" and line_count == line_query + 6:
        hit = x[0:68]
        score = x[70:73]
        e_value = x[78:].replace(" ","")
        print(hit, score, e_value)
        new_row = [query, length_query, hit, e_value, score]
        df.loc[len(df)] = new_row
    

df.to_csv('/data/projet6/data/1_work/Oriolus_Galus_Besthit.csv', index=False)
file.close()