import os
from statistical_analysis_tools.ora.ora import ora


def ora_helper(out_path,global_variables):

    background_path = os.path.join(out_path, "data", "gene_symbols", "gene_symbols.txt")
    gene_sets_out_path = os.path.join(out_path, "data", "statistical_analysis", "over_representation_analysis")

    candidate_list_path = os.path.join(out_path, "data", "gene_symbols", "gene_symbols_significant.txt")
    ora(candidate_list_path, background_path, global_variables, gene_sets_out_path, "all_significant_genes")

    candidate_list_path = os.path.join(out_path, "data", "gene_symbols", "gene_symbols_significant_upregulated.txt")
    ora(candidate_list_path, background_path, global_variables, gene_sets_out_path, "upregulated_genes")

    candidate_list_path = os.path.join(out_path, "data", "gene_symbols", "gene_symbols_significant_downregulated.txt")
    ora(candidate_list_path, background_path, global_variables, gene_sets_out_path,"downregulated_genes")
