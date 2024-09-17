def get_chromosome_list(in_file_path):

    chromosome_dict = {}

    # opens the file
    in_file = open(in_file_path).readlines()

    # detects the chromosome column
    header_line_split = in_file[0].rstrip().split("\t")
    index = 0
    for header in header_line_split:
        if header.upper() == "CHROMOSOME":
            chromosome_column = index
        index += 1

    # gets the chromosomes
    header = True
    for line in in_file:
        if header:
            header = False
        else:
            line_split = line.rstrip().split("\t")
            chromosome_dict[line_split[chromosome_column]] = True

    return sorted(chromosome_dict.keys())
