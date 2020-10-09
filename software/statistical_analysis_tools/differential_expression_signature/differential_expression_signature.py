from statistical_analysis_tools.differential_expression_signature.get_expression_data import get_expression_data
from statistical_analysis_tools.differential_expression_signature.get_genes_by_signature import get_genes_by_signature
from statistical_analysis_tools.differential_expression_signature.merge_signatures import merge_signatures
from statistical_analysis_tools.differential_expression_signature.write_data import write_data
from statistical_analysis_tools.differential_expression_signature.write_summary import write_summary
from misc.get_samples_ordered_by_order_list import get_samples_ordered_by_order_list


def differential_expression_signature(global_variables, infile, out_path, de_IDs, mde_dict):

    # open data file
    data = open(infile).readlines()

    # gets a dictionary of genes by signature
    genes_by_signature,signatures_by_gene = get_genes_by_signature(data, de_IDs)

    # adds the zscores to the genes by signatures
    sample_list = get_samples_ordered_by_order_list(mde_dict["order_list"], global_variables["samples_by_sample_groups"])
    genes_by_signature = get_expression_data(data,sample_list,genes_by_signature,signatures_by_gene)

    # iteratively merges signatures
    genes_by_merged_signature, meta_genes = merge_signatures(genes_by_signature, mde_dict, sample_list)

    # gets the number of signatures (for the report)
    mde_dict["de_signatures"] = range(1,len(genes_by_merged_signature)+1)

    # write data out
    write_data(out_path, genes_by_merged_signature)
    write_summary(out_path, genes_by_merged_signature, meta_genes, global_variables, mde_dict)

    # returns the updated mde disct
    return mde_dict

