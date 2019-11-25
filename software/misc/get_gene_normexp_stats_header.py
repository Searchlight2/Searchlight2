def get_gene_normexp_stats_header(global_variables):

    header_list = []

    # adds the means, medians and stdevs:
    sample_groups_default_order = global_variables["sample_groups_default_order"]

    for sample_group in sample_groups_default_order:
        header_list.append(sample_group + "_mean")
    for sample_group in sample_groups_default_order:
        header_list.append(sample_group + "_median")
    for sample_group in sample_groups_default_order:
        header_list.append(sample_group + "_stdev")

    return header_list