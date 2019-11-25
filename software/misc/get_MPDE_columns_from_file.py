def get_MPDE_columns_from_file(infile, pde_id):

    MPDE_columns = []

    header_split = infile[0].rstrip().split("\t")

    for column_index in range(0, len(header_split)):
        if header_split[column_index].upper() == pde_id.upper() + "_LOG2FOLD":
            MPDE_columns.append(column_index)
        elif header_split[column_index].upper() == pde_id.upper() + "_P":
            MPDE_columns.append(column_index)
        elif header_split[column_index].upper() == pde_id.upper() + "_P.ADJ":
            MPDE_columns.append(column_index)
        elif header_split[column_index].upper() == pde_id.upper() + "_SIG":
            MPDE_columns.append(column_index)
        elif header_split[column_index].upper() == pde_id.upper() + "_PDE_VALID":
            MPDE_columns.append(column_index)

    return MPDE_columns