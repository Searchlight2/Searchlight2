
def get_gene_ne_stats(global_variables,gene_dictionary):

    values_list = []

    # adds the means, medians and stdevs:
    sample_groups_default_order = global_variables["sample_groups_default_order"]


    for sample_group in sample_groups_default_order:
        values_list.append(gene_dictionary["mean_" + sample_group])
    for sample_group in sample_groups_default_order:
        values_list.append(gene_dictionary["median_" + sample_group])
    for sample_group in sample_groups_default_order:
        values_list.append(gene_dictionary["stdev_" + sample_group])

    return values_list




