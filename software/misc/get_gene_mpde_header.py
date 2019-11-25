def get_gene_mpde_header(pde_IDs):

    header_list = []

    for pde_ID in pde_IDs:
        header_list.append(pde_ID + "_log2fold")
    for pde_ID in pde_IDs:
        header_list.append(pde_ID + "_p")
    for pde_ID in pde_IDs:
        header_list.append(pde_ID + "_p.adj")
    for pde_ID in pde_IDs:
        header_list.append(pde_ID + "_sig")
    for pde_ID in pde_IDs:
        header_list.append(pde_ID + "_pde_valid")

    return header_list