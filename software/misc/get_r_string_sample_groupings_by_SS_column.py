
def get_r_string_sample_groupings_by_SS_column(order_list,sample_groups_by_column,samples_by_sample_groups):


    # iterates through the columns
    sample_groupings_by_SS_column_r_string = []
    for column_dict in sample_groups_by_column:
        column_list = []

        # iterates through the sample groups
        for sample_group in order_list:
            if sample_group in column_dict:
                sample_group_samples = samples_by_sample_groups[sample_group]

                # iterates through the samples:
                for sample in sample_group_samples:
                    column_list.append(sample_group)

        sample_groupings_by_SS_column_r_string.append("c(\"" + "\",\"".join(column_list) + "\")")

    sample_groupings_by_SS_column_r_string = "list(" + ",".join(sample_groupings_by_SS_column_r_string) + ")"

    return sample_groupings_by_SS_column_r_string


