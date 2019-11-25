# Parses the sample sheet into a useful form:
def ss_parsing(ss_parameter, global_variables):

    # gets the sub-parameters
    sub_params_list = ss_parameter.split(",")

    for sub_param in sub_params_list:
        if sub_param.upper().startswith("file=".upper()):

            ss_file_path = sub_param.split("=")[1]
            ss_file = open(ss_file_path).readlines()

            sample_list = []
            sample_groups = {}
            sample_groups_default_order = []
            sample_groups_by_sample = {}
            samples_by_sample_groups = {}
            sample_groups_by_column = []
            sample_sheet_column_names = []


            # Reads the sample sheet:
            line_counter = 1
            for line in ss_file:
                line_split = line.rstrip().split("\t")

                # Processes a sample entry (skipping the header)
                if line_counter != 1:
                    sample = line_split[0].upper()

                    # Updates the samples
                    sample_list.append(sample)

                    # Iterates through the sample groupings for a sample
                    col_counter = 0
                    for sample_group in line_split[1:]:

                        sample_group = sample_group.upper()

                        # Updates the sample groups
                        sample_groups[sample_group] = True

                        # Update the sample groups by sample dictionary:
                        if sample in sample_groups_by_sample:
                            sample_groups_for_sample = sample_groups_by_sample[sample]
                        else:
                            sample_groups_for_sample = []

                        sample_groups_for_sample.append(sample_group)
                        sample_groups_by_sample[sample] = sample_groups_for_sample

                        # Updates the samples by sample groups dictionary:
                        if sample_group in samples_by_sample_groups:
                            sample_for_sample_groups = samples_by_sample_groups[sample_group]
                        else:
                            sample_for_sample_groups = []

                        sample_for_sample_groups.append(sample)
                        samples_by_sample_groups[sample_group] = sample_for_sample_groups

                        # Updates the sample group by column list:
                        sample_groups_column_dict = sample_groups_by_column[col_counter]
                        sample_groups_column_dict[sample_group] = True
                        sample_groups_by_column[col_counter] = sample_groups_column_dict

                        col_counter += 1

                else:
                    # Sets up the sample_groups_by_column list
                    for column in line_split[1:]:
                        sample_groups_column_dict = {}
                        sample_groups_by_column.append(sample_groups_column_dict)
                        sample_sheet_column_names.append(column)

                line_counter += 1


            # Updates the default sample group order (by column and then row):
            for column_index in range(1,len(ss_file[0].rstrip().split("\t"))):
                added_sample_groups_dict = {}
                counter = 1
                for line in ss_file:
                    if counter != 1:
                        line_split = line.rstrip().split("\t")
                        sample_group = line_split[column_index].upper()

                        if sample_group not in added_sample_groups_dict:
                            sample_groups_default_order.append(sample_group)
                            added_sample_groups_dict[sample_group] = True



                    counter += 1


    global_variables["sample_list"] = sample_list
    global_variables["sample_groups"] = sample_groups
    global_variables["sample_groups_default_order"] = sample_groups_default_order
    global_variables["sample_groups_by_sample"] = sample_groups_by_sample
    global_variables["samples_by_sample_groups"] = samples_by_sample_groups
    global_variables["sample_groups_by_column"] = sample_groups_by_column
    global_variables["sample_sheet_column_names"] = sample_sheet_column_names


    print "parsed the ss parameter"

    return global_variables




