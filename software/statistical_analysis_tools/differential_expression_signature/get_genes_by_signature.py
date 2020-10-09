def get_genes_by_signature(data, de_IDs):

    signature_coord_sig = []
    signature_coord_log2fold = []
    genes_by_signature = {}
    signatures_by_gene = {}


    # get column index of each de sig and log2fold
    header_split = data[0].rstrip().split("\t")
    for column_index in range(0, len(header_split)):
        for i in range(0, len(de_IDs)):
            if header_split[column_index] == de_IDs[i] + "_sig":
                signature_coord_sig.append(int(column_index))
            if header_split[column_index] == de_IDs[i] + "_log2fold":
                signature_coord_log2fold.append(int(column_index))


    # fetch the signature of current row based on de coordinates
    header = True
    for line in data:

        if header:
            header = False
        else:
            line_split = line.rstrip().split("\t")
            gene = line_split[0] + "\t" + line_split[1]
            signature = ""

            # gets the signature for the current gene
            for de_index in range(0,len(signature_coord_sig)):
                if line_split[signature_coord_sig[de_index]] == "False":
                    signature += "False"
                elif float(line_split[signature_coord_log2fold[de_index]]) > 0:
                    signature += "Up"
                elif float(line_split[signature_coord_log2fold[de_index]]) < 0:
                    signature += "Down"

            # updates the list of genes for the signature
            if signature in genes_by_signature:
                signature_gene_dictionary = genes_by_signature[signature]
            else:
                signature_gene_dictionary = {}

            signature_gene_dictionary[gene] = {}
            genes_by_signature[signature] = signature_gene_dictionary
            signatures_by_gene[gene] = signature

    return genes_by_signature, signatures_by_gene