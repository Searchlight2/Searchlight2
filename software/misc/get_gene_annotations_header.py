

def get_gene_annotations_header(global_variables):

    header_list = []

    # adds any annotations
    if global_variables["annotations_flag"]:
        header_list += global_variables["annotation_headers"]

    return header_list










