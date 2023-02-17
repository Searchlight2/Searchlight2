

def add_background(global_variables):


    master_gene_table = {}
    background_by_gene = global_variables["background_by_gene"]

    # adds the genes
    for gene_ID in background_by_gene:

        gene_dictionary = {}
        gene_background = background_by_gene[gene_ID]

        if global_variables["GENE_SYMBOL_FLAG"]:
            gene_dictionary["SYMBOL"] = gene_background["SYMBOL"]
        if global_variables["GENE_BIOTYPE_FLAG"]:
            gene_dictionary["BIOTYPE"] = gene_background["BIOTYPE"]
        if global_variables["GENE_CHROMOSOME_FLAG"]:
            gene_dictionary["CHROMOSOME"] = gene_background["CHROMOSOME"]
        if global_variables["GENE_START_FLAG"]:
            gene_dictionary["START"] = gene_background["START"]
        if global_variables["GENE_STOP_FLAG"]:
            gene_dictionary["STOP"] = gene_background["STOP"]

        master_gene_table[gene_ID] = gene_dictionary


    # checks for duplicate gene symbols. If so replaces with the gene ID
    if global_variables["GENE_SYMBOL_FLAG"]:

        gene_symbol_count_dict = {}
        for gene_ID in master_gene_table:

            gene_dictionary = master_gene_table[gene_ID]
            symbol = gene_dictionary["SYMBOL"]

            if symbol in gene_symbol_count_dict:
                gene_symbol_count = gene_symbol_count_dict[symbol]
            else:
                gene_symbol_count = 0

            gene_symbol_count += 1
            gene_symbol_count_dict[symbol] = gene_symbol_count

        # We check for duplicate gene symbols
        for gene_ID in master_gene_table:
            gene_dictionary = master_gene_table[gene_ID]
            symbol = gene_dictionary["SYMBOL"]

            if gene_symbol_count_dict[symbol] > 1:
                gene_dictionary["SYMBOL"] = gene_ID
                gene_dictionary["DUPLICATE_SYMBOL_FLAG"] = True
            else:
                gene_dictionary["DUPLICATE_SYMBOL_FLAG"] = False

            master_gene_table[gene_ID] = gene_dictionary




    print("background added to master gene table")


    return master_gene_table


