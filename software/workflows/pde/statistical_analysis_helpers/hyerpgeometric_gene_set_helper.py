import os
from statistical_analysis_tools.hypergeometric_gene_set.hypergeometric_gene_set import hypergeometric_gene_set


def hypergeometric_gene_set_helper(out_path,global_variables):

    background_path = os.path.join(out_path, "data", "gene_symbols", "gene_symbols.txt")
    gene_sets_out_path = os.path.join(out_path, "data", "statistical_analysis", "hypergeometric_gene_set")

    candidate_list_path = os.path.join(out_path, "data", "gene_symbols", "gene_symbols_significant.txt")
    hypergeometric_gene_set(candidate_list_path, background_path, global_variables, gene_sets_out_path, "all_significant_genes")

    candidate_list_path = os.path.join(out_path, "data", "gene_symbols", "gene_symbols_significant_upregulated.txt")
    hypergeometric_gene_set(candidate_list_path, background_path, global_variables, gene_sets_out_path, "upregulated_genes")

    candidate_list_path = os.path.join(out_path, "data", "gene_symbols", "gene_symbols_significant_downregulated.txt")
    hypergeometric_gene_set(candidate_list_path, background_path, global_variables, gene_sets_out_path,"downregulated_genes")
