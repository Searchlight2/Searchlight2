
# gets the column indexes for a list of samples, given an infile.
def get_sample_columns_from_file(samples_dict, infile):

    sample_columns = []

    header_split = infile[0].rstrip().split("\t")

    for column_index in range(0,len(header_split)):
        if header_split[column_index] in samples_dict:
            sample_columns.append(column_index)

    return sample_columns



