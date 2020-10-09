def get_gene_mde(global_variables,gene_dictionary,de_IDs):

    values_list = []

    for de_ID in de_IDs:
        de_Dict = gene_dictionary[de_ID]
        values_list.append(de_Dict["log2fold"])
    for de_ID in de_IDs:
        de_Dict = gene_dictionary[de_ID]
        values_list.append(de_Dict["p"])
    for de_ID in de_IDs:
        de_Dict = gene_dictionary[de_ID]
        values_list.append(de_Dict["p.adj"])
    for de_ID in de_IDs:
        de_Dict = gene_dictionary[de_ID]
        values_list.append(de_Dict["sig"])
    for de_ID in de_IDs:
        de_Dict = gene_dictionary[de_ID]
        values_list.append(de_Dict["valid"])

    return values_list

