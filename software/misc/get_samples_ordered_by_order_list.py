
# gets a list of samples in the order list order:
def get_samples_ordered_by_order_list(order_list,samples_by_sample_groups):

    samples_ordered = []
    for sample_group in order_list:
        sample_group_samples = samples_by_sample_groups[sample_group]
        for sample in sample_group_samples:
            samples_ordered.append(sample)

    return samples_ordered