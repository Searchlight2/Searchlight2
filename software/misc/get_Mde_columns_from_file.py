def get_Mde_columns_from_file(infile, de_id):

    Mde_columns = []

    header_split = infile[0].rstrip().split("\t")

    for column_index in range(0, len(header_split)):
        if header_split[column_index].upper() == de_id.upper() + "_LOG2FOLD":
            Mde_columns.append(column_index)
        elif header_split[column_index].upper() == de_id.upper() + "_P":
            Mde_columns.append(column_index)
        elif header_split[column_index].upper() == de_id.upper() + "_P.ADJ":
            Mde_columns.append(column_index)
        elif header_split[column_index].upper() == de_id.upper() + "_SIG":
            Mde_columns.append(column_index)
        elif header_split[column_index].upper() == de_id.upper() + "_DE_VALID":
            Mde_columns.append(column_index)

    return Mde_columns