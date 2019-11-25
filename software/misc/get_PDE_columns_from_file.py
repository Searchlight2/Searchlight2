
def get_PDE_columns_from_file(infile):

    PDE_columns = {}

    header_split = infile[0].rstrip().split("\t")

    for column_index in range(0, len(header_split)):
        if header_split[column_index].upper() == "LOG2FOLD":
            PDE_columns["LOG2FOLD"] = column_index
        elif header_split[column_index].upper() == "P":
            PDE_columns["P"] = column_index
        elif header_split[column_index].upper() == "P.ADJ":
            PDE_columns["P.ADJ"] = column_index
        elif header_split[column_index].upper() == "SIG":
            PDE_columns["SIG"] = column_index
        elif header_split[column_index].upper() == "PDE_VALID":
            PDE_columns["PDE_VALID"] = column_index


    return PDE_columns
