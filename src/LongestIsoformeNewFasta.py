#python 
"""
Premet la création d'un nouveau fichier fatsa avec le protéome d'une espèce comportant uniquement
les isoforme les plus long à partir d'un fichier agat (agat_sp_keep_longest_isoform.pl) et d'un 
protéome complet 

PTU 2024 BBS 
Jermeie Carabin 
"""

import sys 

def get_data_fasta(ligne) : 
    head = ligne[1:].split(" ")
    id_prot = head[0]
    ann = ""
    for e in head[1:] : 
        ann += e + " "
    return id_prot, ann[:-2]
     

def get_proteome(whole_proteome) : 
    dict_whole_proteome = {}
    with open(whole_proteome, 'r') as protfile : 
        list_seq =[]
        for ligne in protfile : 
            if ligne[0] == ">" : 
                if len(list_seq) != 0 : 
                    seq = "".join(e for e in list_seq)
                    dict_whole_proteome[ID_prot] = (ann, seq)
                    list_seq =[]
                ID_prot, ann = get_data_fasta(ligne) 
            else : 
                list_seq.append(ligne)
            # Ajouter la dernière séquence au dictionnaire
        if ID_prot and list_seq:
            seq = "".join(list_seq)
            dict_whole_proteome[ID_prot] = (ann, seq)

    return dict_whole_proteome


def get_annotation_gff(datapart2) :
    dictionnaire = {}
    for e in datapart2 : 
        a = e.split("=")
        dictionnaire[a[0]] = a[1]
    return dictionnaire


def get_data_gff(ligne) : 
    datapart1 = ligne.split("\t")[0:-1]
    datapart2 = ligne.split("\t")[-1].split(";")
    locus = datapart1[0]
    source = datapart1[1]
    seqType = datapart1[2]
    begin = datapart1[3]
    end = datapart1[4]
    strand = datapart1[6]
    dict_ligne_gff = {"locus": locus,
                   "source" : source,
                   "seqType" : seqType, 
                   "begin" : begin,
                   "end" : end,
                   "strand" : strand                    
                   }
    dict_part2 = get_annotation_gff(datapart2)
    for key in dict_part2 : dict_ligne_gff[key] = dict_part2[key]    
    return dict_ligne_gff


def get_one_isoformePerGene(gff_agat) :
    liste_isoforme_AGAT = []
    with open(gff_agat, 'r') as agat_file : 
        for ligne in agat_file :
            if ligne[0] != "#" : 
                dict_ligne_gff = get_data_gff(ligne) 
                if "protein_id" in dict_ligne_gff : 
                    id_prot = dict_ligne_gff["protein_id"][:-1]
                    if id_prot not in liste_isoforme_AGAT : 
                        liste_isoforme_AGAT.append(id_prot)
    return liste_isoforme_AGAT


def get_sortied_gff(dict_whole_proteome, liste_isoforme_AGAT) : 
    dict_sortied = {}
    for key in dict_whole_proteome : 
        if key in liste_isoforme_AGAT : 
            id_prot = key 
            ann = dict_whole_proteome[key][0]
            seq = dict_whole_proteome[key][1]
            newKey = id_prot + " " + str (ann)
            dict_sortied[newKey] = seq
    return dict_sortied
        

def new_gff_write(dict_fasta_output, fasta_output) : 
    with open(fasta_output, "w") as output : 
        for key in dict_fasta_output : 
            head = key 
            seq = dict_fasta_output[key]
            output.write(">")
            output.write(head)
            output.write("\n")
            output.write(seq)


def main(whole_proteome, gff_agat, fasta_output) : 
    dict_whole_proteome = get_proteome(whole_proteome) 
    liste_isoforme_AGAT = get_one_isoformePerGene(gff_agat) 
    dict_fasta_output = get_sortied_gff(dict_whole_proteome, liste_isoforme_AGAT)
    new_gff_write(dict_fasta_output, fasta_output)
    print("DONE")


if __name__ == "__main__":
    # Vérification du nombre d'arguments
    if len(sys.argv) != 4:
        print(
            "\nErreur : Nombre d'arguments incorrect.\n"
            "Usage : python script.py <whole_proteome> <gffAGAT> <fastaOUTPUT>\n\n"
            "Description des arguments :\n"
            "  <whole_proteome> : Chemin vers le fichier FASTA contenant les séquences protéiques complètes.\n"
            "  <gffAGAT>        : Chemin vers le fichier GFF annoté par AGAT.\n"
            "  <fastaOUTPUT>    : Chemin où le fichier FASTA de sortie sera généré.\n"
        )
        sys.exit(1) 

    # Extraction des arguments
    whole_proteome = sys.argv[1]
    gff_agat = sys.argv[2]
    fasta_output = sys.argv[3]

    main(whole_proteome, gff_agat, fasta_output)
