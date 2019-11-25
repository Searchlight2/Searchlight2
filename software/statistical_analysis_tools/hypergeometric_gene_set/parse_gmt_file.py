import os


def parse_gmt_file(gene_sets_dict,background_dict,min_set_size,max_set_size,out_path,type,out_path_tag):


    gene_sets_dict_parsed = {}

    # iterates through the gene sets:
    for gene_set in gene_sets_dict:

        genes_in_gene_set = gene_sets_dict[gene_set]
        genes_in_gene_set_parsed = []

        # iterates through the genes and checks that they are in the background list
        for gene in genes_in_gene_set:
            if gene.upper() in background_dict:
                genes_in_gene_set_parsed.append(gene.upper())

        # tests for a parsed gene set that isn't too big or small
        if len(genes_in_gene_set_parsed) >= min_set_size and len(genes_in_gene_set_parsed) <= max_set_size:
            gene_sets_dict_parsed[gene_set] = genes_in_gene_set_parsed

    # prints the output
    out_file = open(os.path.join(out_path,type,"valid_gene_sets.gmt"),"w")

    for gene_set in gene_sets_dict_parsed:
        out_file.write(gene_set + "\t" + type + "\t" + "\t".join(gene_sets_dict_parsed[gene_set]) + "\n")

    return gene_sets_dict_parsed







