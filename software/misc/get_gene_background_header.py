def get_gene_background_header(global_variables):

    header_list = []

    # adds the background information
    if global_variables["GENE_SYMBOL_FLAG"]:
        header_list.append("symbol")
    if global_variables["GENE_BIOTYPE_FLAG"]:
        header_list.append("biotype")
    if global_variables["GENE_CHROMOSOME_FLAG"]:
        header_list.append("chromosome")
    if global_variables["GENE_START_FLAG"]:
        header_list.append("start")
    if global_variables["GENE_STOP_FLAG"]:
        header_list.append("stop")


    return header_list
