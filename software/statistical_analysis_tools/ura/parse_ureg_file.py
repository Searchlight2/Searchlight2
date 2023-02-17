import os

def parse_ureg_file(ureg_dict, background_dict, min_set_size, max_set_size, out_path, type):

    ureg_dict_parsed = {}
    gene_sets_dict_parsed = {}

    # iterates through the uregs:
    for ureg_name in ureg_dict:

        # tests for the genes being in the background
        if ureg_name in background_dict:
            ureg_targets_dict = ureg_dict[ureg_name]
            ureg_targets_dict_parsed = {}
            for target_name in ureg_targets_dict:
                if target_name in background_dict:
                    ureg_targets_dict_parsed[target_name] = ureg_targets_dict[target_name]

            # tests for the ureg set that isn't too big or small
            if len(ureg_targets_dict_parsed) >= min_set_size and len(ureg_targets_dict_parsed) <= max_set_size:

                # updates the new ureg dict
                ureg_dict_parsed[ureg_name] = ureg_targets_dict_parsed

                # updates the gene sets dict
                gene_sets_dict_parsed[ureg_name] = list(ureg_targets_dict_parsed.keys())


    # prints the outputs
    out_file_gmt = open(os.path.join(out_path, type, "valid_uregs.gmt"), "w")
    out_file_csv = open(os.path.join(out_path, type, "valid_uregs.csv"), "w")

    for gene_set in gene_sets_dict_parsed:
        out_file_gmt.write(gene_set + "\t" + type + "\t" + "\t".join(gene_sets_dict_parsed[gene_set]) + "\n")


    for ureg_name in ureg_dict_parsed:
        ureg_targets_dict_parsed = ureg_dict_parsed[ureg_name]
        for target_name in ureg_targets_dict_parsed:
            ureg_target_direction_list = ureg_targets_dict_parsed[target_name]

            if ureg_target_direction_list[0]:
                out_file_csv.write(ureg_name + "\t" + target_name + "\t" + "ACTIVATION" + "\n")
            if ureg_target_direction_list[1]:
                out_file_csv.write(ureg_name + "\t" + target_name + "\t" + "REPRESSION" + "\n")
            if ureg_target_direction_list[2]:
                out_file_csv.write(ureg_name + "\t" + target_name + "\t" + "UNKNOWN" + "\n")


    return ureg_dict_parsed,gene_sets_dict_parsed







