def get_gene_mde_header(de_IDs):

    header_list = []

    for de_ID in de_IDs:
        header_list.append(de_ID + "_log2fold")
    for de_ID in de_IDs:
        header_list.append(de_ID + "_p")
    for de_ID in de_IDs:
        header_list.append(de_ID + "_p.adj")
    for de_ID in de_IDs:
        header_list.append(de_ID + "_sig")
    for de_ID in de_IDs:
        header_list.append(de_ID + "_de_valid")

    return header_list