def get_coordinate_columns_from_file(infile):

    coordinate_columns = {}

    header_split = infile[0].rstrip().split("\t")

    for column_index in range(0, len(header_split)):
        if header_split[column_index].upper() == "CHROMOSOME":
            coordinate_columns["CHROMOSOME"] = column_index
        elif header_split[column_index].upper() == "START":
            coordinate_columns["START"] = column_index
        elif header_split[column_index].upper() == "STOP":
            coordinate_columns["STOP"] = column_index

    return coordinate_columns