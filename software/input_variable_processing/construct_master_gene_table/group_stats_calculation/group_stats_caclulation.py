import numpy

def group_stats_calculation(global_variables, master_gene_table):


    samples_by_sample_groups = global_variables["samples_by_sample_groups"]

    for gene_ID in master_gene_table:
        gene_dictionary = master_gene_table[gene_ID]

        if gene_dictionary["ne_flag"]:

            for sample_group in samples_by_sample_groups:
                ne_list = []
                sample_group_samples = samples_by_sample_groups[sample_group]

                for sample in sample_group_samples:
                    ne_list.append(gene_dictionary[sample])

                ne_list = numpy.array(ne_list)
                mean = numpy.mean(ne_list)
                median = numpy.median(ne_list)
                stdev = numpy.std(ne_list)

                gene_dictionary["mean_" + sample_group] = mean
                gene_dictionary["median_" + sample_group] = median
                gene_dictionary["stdev_" + sample_group] = stdev

        master_gene_table[gene_ID] = gene_dictionary


    print("sample group summary stats calculated")



    return master_gene_table

