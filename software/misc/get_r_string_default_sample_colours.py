

def get_r_string_default_sample_colours(order_list, samples_by_sample_groups):

    default_samples_colours_r_string = []
    for counter in range(0,len(order_list)):
        sample_group_samples = samples_by_sample_groups[order_list[counter]]
        for sample in sample_group_samples:
            default_samples_colours_r_string.append("default_sample_group_colours[" + str(counter+1) + "]")

    default_samples_colours_r_string = "c(" + ",".join(default_samples_colours_r_string) + ")"

    return default_samples_colours_r_string

