import numpy
import os
import math
import scipy

from misc.get_sample_columns_from_file import get_sample_columns_from_file
from misc.get_coordinate_columns_from_file import get_coordinate_columns_from_file
from misc.get_de_columns_from_file import get_de_columns_from_file
from misc.new_directory import new_directory


def spatial_enrichment(global_variables,in_path, sample_groups, out_path, type):

    # strores the results
    gene_data_dictionary = {}
    summary_dictionary = {}

    # makes the out folder:
    new_directory(out_path)

    # opens the files
    in_file = open(in_path).readlines()
    genes_out_file = open(os.path.join(out_path,"spatial_enrichment_gene_data.csv"),"w")
    summary_out_file = open(os.path.join(out_path,"spatial_enrichment_summary.csv"),"w")

    # writes the headers:
    if type == "ne":
        genes_out_file.write("\t".join(["gene_id","mean_expression","chromosome","midpoint_coordinate"]) + "\n")
        summary_out_file.write("\t".join(["chromosome", "total_genes", "expressed_genes","expressed_genes_bias_log2fold","expressed_genes_bias_p"]) + "\n")
    if type == "de":
        genes_out_file.write("\t".join(["gene_id","mean_expression","chromosome","midpoint_coordinate","log2fold","p","significant","de_valid"]) + "\n")
        summary_out_file.write("\t".join(["chromosome", "total_genes", "expressed_genes", "de_valid_genes","positive_fold_genes","negative_fold_genes","significant_genes","upregulated_genes","downregulated_genes","expressed_genes_bias_log2fold","expressed_genes_bias_p","significant_genes_bias_log2fold","significant_genes_bias_p","direction_bias_swing","direction_bias_p"]) + "\n")

    # gets a dictionary of the samples
    samples_by_sample_groups = global_variables["samples_by_sample_groups"]
    samples_dict = {}
    for sample_group in sample_groups:
        sample_group_samples = samples_by_sample_groups[sample_group]
        for sample in sample_group_samples:
            samples_dict[sample] = True

    # gets the expression threshold
    expressed_threshold = global_variables["ne_threshold"]

    # gets the column information for the infile
    sample_columns = get_sample_columns_from_file(samples_dict, in_file)
    coordinate_columns = get_coordinate_columns_from_file(in_file)

    if type == "de":
        de_columns = get_de_columns_from_file(in_file)

    # gets the gene and summary information
    header = True
    for line in in_file:
        if header:
            header = False
        else:
            line_split = line.rstrip().split("\t")

            # gets the mean expression
            mean_expression = get_mean_expression(line_split, sample_columns)

            # gets the coordinates
            chromosome = line_split[coordinate_columns["CHROMOSOME"]]
            start = int(line_split[coordinate_columns["START"]])
            stop = int(line_split[coordinate_columns["STOP"]])
            mid_point = (stop-start)/2

            # updates the results with the ne information
            gene_data = [str(mean_expression),chromosome,str(mid_point)]

            if chromosome in summary_dictionary:
                chromosome_summary = summary_dictionary[chromosome]
            else:
                chromosome_summary = [0,0,0,0,0,0,0,0]

            chromosome_summary[0] = chromosome_summary[0] + 1

            # tests for an expressed gene
            if mean_expression >= expressed_threshold:
                chromosome_summary[1] = chromosome_summary[1] + 1

            # updates the results with the de information
            if type == "de":
                gene_data.append(line_split[de_columns["LOG2FOLD"]])
                gene_data.append(line_split[de_columns["P"]])
                gene_data.append(line_split[de_columns["SIG"]])
                gene_data.append(line_split[de_columns["DE_VALID"]])

                if line_split[de_columns["DE_VALID"]] == "True":
                    chromosome_summary[2] = chromosome_summary[2]+1
                    if float(line_split[de_columns["LOG2FOLD"]]) > 0:
                        chromosome_summary[3] = chromosome_summary[3] + 1
                    elif float(line_split[de_columns["LOG2FOLD"]]) < 0:
                        chromosome_summary[4] = chromosome_summary[4] + 1
                    if line_split[de_columns["SIG"]] == "True":
                        chromosome_summary[5] = chromosome_summary[5] + 1
                        if float(line_split[de_columns["LOG2FOLD"]]) > 0:
                            chromosome_summary[6] = chromosome_summary[6] + 1
                        elif float(line_split[de_columns["LOG2FOLD"]]) < 0:
                            chromosome_summary[7] = chromosome_summary[7] + 1

            # updates the results
            gene_data_dictionary[line_split[0]] = gene_data
            summary_dictionary[chromosome] = chromosome_summary


    # performs the stats
    total_genes = 0
    total_expressed_genes = 0
    total_de_valid_genes = 0
    total_significant = 0
    total_upregulated_genes = 0
    total_downregulated_genes = 0

    # counts and summaries
    for chromosome in summary_dictionary:
        chromosome_summary = summary_dictionary[chromosome]

        total_genes += chromosome_summary[0]
        total_expressed_genes += chromosome_summary[1]
        total_de_valid_genes += chromosome_summary[2]
        total_significant += chromosome_summary[5]
        total_upregulated_genes += chromosome_summary[6]
        total_downregulated_genes += chromosome_summary[7]

    if total_significant > 0:
        ratio_upregulated = float(total_upregulated_genes) / (float(total_significant))
        ratio_downregulated = float(total_downregulated_genes) / (float(total_significant))
    else:
        ratio_upregulated = 0.0
        ratio_downregulated = 0.0

    # stats
    for chromosome in summary_dictionary:
        chromosome_summary = summary_dictionary[chromosome]

        # expressed genes bias
        try:
            expressed_genes_log2fold = math.log(float(chromosome_summary[1])+0.001,2) - math.log(((float(chromosome_summary[0])/float(total_genes))*float(total_expressed_genes))+0.001,2)
            chromosome_summary.append(round(expressed_genes_log2fold,2))
            odds, expressed_genes_p_value = scipy.stats.fisher_exact([[float(total_genes),float(chromosome_summary[0])],[float(total_expressed_genes),float(chromosome_summary[1])]],alternative='two-sided')
            chromosome_summary.append(expressed_genes_p_value)
        except:
            chromosome_summary.append("NA")
            chromosome_summary.append("NA")

        # sig genes bias
        try:
            significant_genes_log2fold = math.log(float(chromosome_summary[5])+0.001,2) - math.log((float(chromosome_summary[2])/float(total_de_valid_genes))*float(total_significant)+0.001,2)
            chromosome_summary.append(round(significant_genes_log2fold,2))
            odds, sig_genes_bias_p_value = scipy.stats.fisher_exact([[float(total_de_valid_genes),float(chromosome_summary[2])],[float(total_significant),float(chromosome_summary[5])]],alternative='two-sided')
            chromosome_summary.append(sig_genes_bias_p_value)
        except:
            chromosome_summary.append("NA")
            chromosome_summary.append("NA")

        # direction bias
        try:
            expected_upregulated = ratio_upregulated * float(chromosome_summary[5])
            expected_downregulated = ratio_downregulated * float(chromosome_summary[5])
            swing_difference = float(chromosome_summary[6]) - expected_upregulated
            swing = str(round(swing_difference/float(chromosome_summary[5])*100,2)) + "%"
            chromosome_summary.append(swing)

            odds,direction_bias_p_value = scipy.stats.fisher_exact([[expected_upregulated,float(chromosome_summary[6])],[expected_downregulated,float(chromosome_summary[7])]], alternative='two-sided')
            chromosome_summary.append(direction_bias_p_value)
        except:
            chromosome_summary.append("NA")
            chromosome_summary.append("NA")

        summary_dictionary[chromosome] = chromosome_summary


    #outputs the gene data results:
    for gene in gene_data_dictionary:
        genes_out_file.write(gene + "\t" + "\t".join(gene_data_dictionary[gene]) + "\n")

    #outputs the summary:
    for chromosome in summary_dictionary:
        summary_out_file.write(chromosome + "\t" + "\t".join(map(str,summary_dictionary[chromosome])) + "\n")




# gets the mean gene expression for a list of samples
def get_mean_expression(line_split,sample_columns):
    per_sample_expression = []
    for sample_column_index in sample_columns:
        per_sample_expression.append(float(line_split[sample_column_index]))
    mean_expression = numpy.mean(per_sample_expression)

    return mean_expression