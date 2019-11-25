
def get_r_string_default_sample_group_colours_by_SS_column(samples_by_sample_groups,order_list,sample_groups_by_column):

    # iterates through the columns
    default_sample_group_colours_by_SS_column_r_string = []
    counter = 1
    for column_dict in sample_groups_by_column:
        default_sample_group_colours_by_SS_column_r_string.append("default_sample_group_colours[" + str(counter) + ":" + str(counter+len(column_dict.keys())-1) + "]")
        counter += len(column_dict.keys())

    default_samples_colours_by_SS_column_r_string = "list(" + ",".join(default_sample_group_colours_by_SS_column_r_string) + ")"

    return default_samples_colours_by_SS_column_r_string