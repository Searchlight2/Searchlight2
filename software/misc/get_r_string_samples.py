

def get_r_string_samples(samples_ordered):
    samples_r_string = "c(\""
    samples_r_string += "\",\"".join(samples_ordered)
    samples_r_string += "\")"

    return samples_r_string
