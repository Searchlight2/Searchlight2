
def get_gene_background(global_variables,gene_dictionary):

    values_list = []

    # adds the background information
    if global_variables["GENE_SYMBOL_FLAG"]:
        values_list.append(gene_dictionary["SYMBOL"])
    if global_variables["GENE_BIOTYPE_FLAG"]:
        values_list.append(gene_dictionary["BIOTYPE"])
    if global_variables["GENE_CHROMOSOME_FLAG"]:
        values_list.append(gene_dictionary["CHROMOSOME"])
    if global_variables["GENE_START_FLAG"]:
        values_list.append(gene_dictionary["START"])
    if global_variables["GENE_STOP_FLAG"]:
        values_list.append(gene_dictionary["STOP"])

    return values_list
