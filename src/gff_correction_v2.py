#!/data/projet6/conda/carabin/PTU_groupe6

import argparse



def  get_protein_liste(ratioFragmentation, proteinListe): 
    listProteinFragmented, dict_relation, dict_relation_ref_to_es= [], {}, {}
    with open(proteinListe, "r") as l : 
        for line in l : 
            if line[0] != '#' : 
                dat = line.rsplit(",")
                ratio = dat[2]
                if float(ratio) <= ratioFragmentation :
                    dict_relation[dat[0]] = dat[1]
                    dict_relation_ref_to_es[dat[1]] = dat[0]
                    listProteinFragmented.append(dat[0])
    print(f"proteins fragmented : {len(listProteinFragmented)}")
    return dict_relation_ref_to_es, dict_relation, listProteinFragmented


def get_annotation_gff(datapart2) :
    dictionnaire = {}
    datapart2 = datapart2.rsplit(";")
    for e in datapart2 : 
        a = e.split("=")
        dictionnaire[a[0]] = a[1]
    return dictionnaire


def get_prot_for_gene(gffFile, listProteinFragmented) : 
    dict_prot_to_gene = {}
    with open(gffFile, 'r') as gff : 
        for line in gff :
            if line[0] != "#" and "protein_id" in line and ";gene" in line :
                dat = line.rsplit("\t")
                data1, data2 = dat[0:-1], dat[-1]
                data2 =  get_annotation_gff(data2) 
                if "protein_id" in data2 and "gene" in data2 : 
                    protein = data2["protein_id"] 
                    if protein in listProteinFragmented : 
                        gene = data2["gene"]
                        dict_prot_to_gene[protein] = gene
    print(f"Nombre de gènes : {len(dict_prot_to_gene)}")
    return dict_prot_to_gene

def get_new_annotation(miniprotAlign, dict_prot_to_gene, dict_relation_ref_to_es) : 
    dict_gene_new_born = {}
    with open(miniprotAlign, "r") as mn : 
        for line in mn : 
            if line[0] != "#" and "Target=" in line:
                dat = line.rsplit("\t")
                data1, data2 = dat[0:-1], dat[-1]
                data2 =  get_annotation_gff(data2) 
                protein_ref = data2["Target"].split(" ")[0]
                if protein_ref in dict_relation_ref_to_es : 
                    protein_es = dict_relation_ref_to_es[protein_ref]
                    if protein_es in dict_prot_to_gene :
                        gene_ref = dict_prot_to_gene[protein_es]
                        seq, b, e, sens, locus, phase =  data1[2], data1[3],data1[4], data1[6], data1[0], data1[7]
                        if gene_ref in dict_gene_new_born : 
                            dict_gene_new_born[gene_ref][seq].append((b, e, sens, locus, phase))
                        else :  
                            dict_gene_new_born[gene_ref] = {"CDS" : [], "mRNA" : []}
                            dict_gene_new_born[gene_ref][seq].append((b, e, sens, locus, phase))

    print(f"Nombre de gènes avec correction : {len(dict_gene_new_born)}")
    return dict_gene_new_born


def get_dict_gene_check(dict_gene_new_born):
    dict_gene_check = {}
    for gene in dict_gene_new_born : 
        dict_gene_check[gene] = False 
    return dict_gene_check

def get_new_gff(gffFile, dict_gene_new_born) : 
    dict_line_gff = {}
    c = 0
    dict_gene_check = get_dict_gene_check(dict_gene_new_born)
    with open(gffFile, 'r') as gff : 
        for line in gff :
            if line[0] != "#":
                if ";gene=" not in line : 
                    dict_line_gff[c] = line 
                    c+=1
                else : 
                    dat = line.rsplit("\t")
                    data1, data2 = dat[0:-1], dat[-1]
                    ann = data2
                    data2 =  get_annotation_gff(data2) 
                    gene = data2["gene"]
                    if gene not in dict_gene_new_born : 
                        dict_line_gff[c]= line 
                        c+=1
                    else : 
                        if dict_gene_check[gene] == False :
                            #création de lignes avec modifications 
                            #b, e, sens, locus

                            #Gene and mRNA
                            for mRNA in dict_gene_new_born[gene]["mRNA"] :
                                new = mRNA
                                new_line = f"{new[3]}\tminiprot\tgene\t{new[0]}\t{new[1]}\t.\t{new[2]}\t{new[4]}\t{ann}"
                                dict_line_gff[c] =  new_line
                                c += 1

                                new_line = f"{new[3]}\tminiprot\tmRNA\t{new[0]}\t{new[1]}\t.\t{new[2]}\t{new[4]}\t{ann}"
                                dict_line_gff[c] =  new_line
                                c += 1

                                #exon
                                for exon in dict_gene_new_born[gene]["CDS"]: 
                                    new = exon 
                                    new_line = f"{new[3]}\tminiprot\texon\t{new[0]}\t{new[1]}\t.\t{new[2]}\t.\n"
                                    dict_line_gff[c] =  new_line
                                    c += 1

                                #CDS
                                for cds in dict_gene_new_born[gene]["CDS"]: 
                                    new = cds 
                                    new_line = f"{new[3]}\tminiprot\tCDS\t{new[0]}\t{new[1]}\t.\t{new[2]}\t{new[4]}\n"
                                    dict_line_gff[c] =  new_line
                                    c += 1

                                dict_gene_check[gene] = True
    print(f"Nombre de ligne dans gff : {len(dict_line_gff)}")
    return dict_line_gff


def write_newGFF(dict_line_gff,output) : 
    with open(output, 'w') as nGFF : 
        for key in dict_line_gff : 
            new_line = dict_line_gff[key]
            nGFF.write(new_line)
    print(f"Ecriture du fichier {output}")


def main(gffFile, proteinListe, miniprotAlign, output, ratioFragmentation):
    dict_relation_ref_to_es, dict_relation_es_to_ref, listProteinFragmented = get_protein_liste(ratioFragmentation, proteinListe)
    dict_prot_to_gene = get_prot_for_gene(gffFile, listProteinFragmented)
    dict_gene_new_born = get_new_annotation(miniprotAlign, dict_prot_to_gene, dict_relation_ref_to_es) 
    dict_line_gff = get_new_gff(gffFile, dict_gene_new_born)
    write_newGFF(dict_line_gff,output)
    print('DONE')


if __name__=='__main__':
    parser = argparse.ArgumentParser(description="GFF fragmented correction.")
    parser.add_argument('-g', '--gffFile', help='The input fragmented GFF.', required=True, default=None)
    parser.add_argument('-l', '--proteinListe', help='The input Protein fragmented liste.', required=True, default=None)
    parser.add_argument('-m', '--miniprotAlign', help='The input Miniprot Align', required=True, default=None)
    parser.add_argument('-o', '--output', help='The output GFF corrected', required=True, default=None)
    parser.add_argument('-p', '--ratioFragmentation', help='The output GFF corrected', required=False, default=0.6)

    args = parser.parse_args()

    if args.gffFile is None:
        raise RuntimeError("Must specify the input fragmented GFF with -g or --gffFile.")

    if args.proteinListe is None:
        raise RuntimeError("Must specify the input Protein fragmented list with -l or --proteinListe.")

    if args.miniprotAlign is None:
        raise RuntimeError("Must specify the input Miniprot alignment with -m or --miniprotAlign.")

    if args.output is None:
        raise RuntimeError("Must specify the output GFF corrected file with -o or --output.")

    main(args.gffFile, args.proteinListe, args.miniprotAlign, args.output, args.ratioFragmentation)
