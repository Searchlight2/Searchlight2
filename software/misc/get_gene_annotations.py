
def get_gene_annotations(global_variables,gene_dictionary):

    values_list = []

    # adds any annotations
    if global_variables["annotations_flag"]:
        values_list += gene_dictionary["annotations"]

    return values_list




