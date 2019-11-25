
def get_all_samples(global_variables):
    samples_by_sample_groups = global_variables["samples_by_sample_groups"]
    order_list = global_variables["order_list"]
    all_samples = []

    for key, value in samples_by_sample_groups.iteritems():
        if key in order_list:
            for v in value:
                all_samples.append(v)

    return all_samples



