def is_sample(test_sample, sample_list):

    for sample in sample_list:

        if sample.upper() == test_sample.upper():
            return True

    return False
