
def get_r_string_samples_by_sample_group(order_list,samples_by_sample_groups):

    samples_by_sample_group_r_string = []
    for sample_group in order_list:
        sample_group_samples = samples_by_sample_groups[sample_group]
        samples_by_sample_group_r_string.append("c(\"" + "\",\"".join(sample_group_samples) + "\")")

    samples_by_sample_group_r_string = "list(" + ",".join(samples_by_sample_group_r_string) + ")"

    return samples_by_sample_group_r_string