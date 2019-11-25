

def get_r_string_default_samples_colours_by_SS_column(samples_by_sample_groups,order_list,sample_groups_by_column):


    # iterates through the columns
    default_samples_colours_by_SS_column_r_string = []
    counter = 0
    for column_dict in sample_groups_by_column:
        column_list = []

        #iterates through the sample groups
        for sample_group in order_list:
            if sample_group in column_dict:
                counter += 1
                sample_group_samples = samples_by_sample_groups[sample_group]

                #iterates through the samples:
                for sample in sample_group_samples:
                    column_list.append("default_sample_group_colours[" + str(counter) + "]")

        default_samples_colours_by_SS_column_r_string.append("c(" + ",".join(column_list) + ")")

    default_samples_colours_by_SS_column_r_string = "list(" + ",".join(default_samples_colours_by_SS_column_r_string) + ")"

    return default_samples_colours_by_SS_column_r_string



