import os
from misc.get_samples_ordered_by_order_list import get_samples_ordered_by_order_list


def write_summary(out_path, genes_by_merged_signature, meta_genes, global_variables, mde_dict):

    # append total genes and z scores to data
    summary_data = {}
    counter = 1
    for key in meta_genes:
        meta_gene_values = meta_genes[key]
        total_genes = str(len(genes_by_merged_signature[key]))
        summary_data[counter] = total_genes + "\t" + "\t".join(str(x) for x in meta_gene_values) + "\n"
        counter += 1

    # sort the summary data by total genes
    summary_data_sorted_on_number_of_genes = sorted(summary_data, key=lambda key: int(summary_data[key].split("\t")[0]), reverse=True)
    summary_data_sorted = {}
    for i in range(0, len(summary_data_sorted_on_number_of_genes)):
        sig_id = "signature_" + str(i+1) + "\t"
        summary_data_sorted[i+1] = sig_id + summary_data[summary_data_sorted_on_number_of_genes[i]]

    # create header
    sample_names = get_samples_ordered_by_order_list(mde_dict["order_list"], global_variables["samples_by_sample_groups"])
    summary_data_sorted[0] = "signature\tsignature_size\t" + "\t".join(sample_names) + "\n"

    # writes the summary
    with open(os.path.join(out_path, "Signature_summary.csv"), "w+") as f:
        for k, v in summary_data_sorted.items():
            f.write(v)
