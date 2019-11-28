from misc.get_gene_annotations_header import get_gene_annotations_header

def get_gene_annotations(global_variables,gene_dictionary):

    values_list = []

    # adds any annotations
    if global_variables["annotations_flag"]:
        if "annotations" in gene_dictionary:
            values_list += gene_dictionary["annotations"]
        else:
            values_list += ["NA"] * len(get_gene_annotations_header(global_variables))

    return values_list




