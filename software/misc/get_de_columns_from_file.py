
def get_de_columns_from_file(infile):

    de_columns = {}

    header_split = infile[0].rstrip().split("\t")

    for column_index in range(0, len(header_split)):
        if header_split[column_index].upper() == "LOG2FOLD":
            de_columns["LOG2FOLD"] = column_index
        elif header_split[column_index].upper() == "P":
            de_columns["P"] = column_index
        elif header_split[column_index].upper() == "P.ADJ":
            de_columns["P.ADJ"] = column_index
        elif header_split[column_index].upper() == "SIG":
            de_columns["SIG"] = column_index
        elif header_split[column_index].upper() == "DE_VALID":
            de_columns["DE_VALID"] = column_index


    return de_columns
