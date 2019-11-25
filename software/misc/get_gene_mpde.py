def get_gene_mpde(global_variables,gene_dictionary,pde_IDs):

    values_list = []

    for pde_ID in pde_IDs:
        pde_Dict = gene_dictionary[pde_ID]
        values_list.append(pde_Dict["log2fold"])
    for pde_ID in pde_IDs:
        pde_Dict = gene_dictionary[pde_ID]
        values_list.append(pde_Dict["p"])
    for pde_ID in pde_IDs:
        pde_Dict = gene_dictionary[pde_ID]
        values_list.append(pde_Dict["p.adj"])
    for pde_ID in pde_IDs:
        pde_Dict = gene_dictionary[pde_ID]
        values_list.append(pde_Dict["sig"])
    for pde_ID in pde_IDs:
        pde_Dict = gene_dictionary[pde_ID]
        values_list.append(pde_Dict["valid"])

    return values_list

