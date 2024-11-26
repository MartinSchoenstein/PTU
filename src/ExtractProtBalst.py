#Python 

import sys

def get_BlastP(BLASTP)  : 
    liste_homologue_prot = []
    with open(BLASTP, 'r') as blastp : 
        for ligne in blastp : 
            ID_subject = ligne.split("\t")[1]
            liste_homologue_prot.append(ID_subject)
    return liste_homologue_prot


def get_data_fasta(ligne) : 
    head = ligne[1:].split(" ")
    id_prot = head[0]
    ann = ""
    for e in head[1:] : 
        ann += e + " "
    return id_prot, ann[:-2]


def  get_fasta_gal(fasta_gallius) : 
    dict_fatsa_ref = {}
    with open(fasta_gallius, 'r') as protfile : 
        list_seq =[]
        for ligne in protfile : 
            if ligne[0] == ">" : 
                if len(list_seq) != 0 : 
                    seq = "".join(e for e in list_seq)
                    dict_fatsa_ref[ID_prot] = (ann, seq)
                    list_seq =[]
                ID_prot, ann = get_data_fasta(ligne) 
            else : 
                list_seq.append(ligne)
            # Ajouter la dernière séquence au dictionnaire
        if ID_prot and list_seq:
            seq = "".join(list_seq)
            dict_fatsa_ref[ID_prot] = (ann, seq)

    return dict_fatsa_ref

def get_new_fasta(liste_homologue_prot,dict_fatsa_ref) : 
    dict_new_fasta = {}
    for key in dict_fatsa_ref : 
        if key in liste_homologue_prot : 
            dict_new_fasta[key] = dict_fatsa_ref[key]
    return dict_new_fasta


def sortied_fasta(dict_new_fasta, fasta_output) :
    with open(fasta_output, "w") as output : 
        for key in dict_new_fasta : 
            head = f"{key} {dict_new_fasta[key][0]}"
            seq = dict_new_fasta[key][1]
            output.write(">")
            output.write(head)
            output.write("\n")
            output.write(seq)


def main(BLASTP, fasta_gallius, fasta_output) : 
    liste_homologue_prot = get_BlastP(BLASTP) 
    print("liste_homologue_prot",len(liste_homologue_prot))
    dict_fatsa_ref = get_fasta_gal(fasta_gallius)
    print("dict_fatsa_ref", len(dict_fatsa_ref))
    dict_new_fasta = get_new_fasta(liste_homologue_prot,dict_fatsa_ref)
    print("dict_new_fasta",len(dict_new_fasta))
    sortied_fasta(dict_new_fasta, fasta_output)
    print("DONE")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <BLASTP> <fasta_gallius> <fasta_output>")
        sys.exit(1) 

    # Extraction des arguments
    BLASTP = sys.argv[1]
    fasta_gallius = sys.argv[2]
    fasta_output = sys.argv[3]

    main(BLASTP, fasta_gallius, fasta_output)