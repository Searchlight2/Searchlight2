# gets a list of samples in the order list order:
def get_r_string_sample_groupings(order_list,samples_by_sample_groups):

    sample_groupings_r_string = []
    for sample_group in order_list:
        sample_group_samples = samples_by_sample_groups[sample_group]
        for index in sample_group_samples:
            sample_groupings_r_string.append(sample_group)

    sample_groupings_r_string = "c(\"" + "\",\"".join(sample_groupings_r_string) + "\")"

    return sample_groupings_r_string