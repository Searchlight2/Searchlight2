

def get_gene_ne(global_variables,gene_dictionary):

    values_list = []

    # gets the ordered samples
    sample_list = global_variables["sample_list"]

    for sample in sample_list:
        values_list.append(gene_dictionary[sample])

    return values_list



