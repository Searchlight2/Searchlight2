import os
from statistical_analysis_tools.differential_expression_signature.differential_expression_signature import differential_expression_signature
from statistical_analysis_tools.ora.ora import ora

def differential_expression_signature_helper(global_variables, out_path, de_IDs, mde_dict):

    # runs the signature analysis
    signature_candidate_list_path = os.path.join(out_path, "data", "genes_significant_in_any_des_annotated.csv")
    differential_expression_signature_out_path = os.path.join(out_path, "data", "statistical_analysis", "differential_expression_signature")
    mde_dict = differential_expression_signature(global_variables, signature_candidate_list_path, differential_expression_signature_out_path, de_IDs, mde_dict)


    # runs the gene-set analysis for each signature
    if global_variables["ora_flag"] == True:
        background_path = os.path.join(out_path, "data", "gene_symbols", "all_gene_symbols.txt")

        for signature_number in mde_dict["de_signatures"]:
            signature_name = "signature_" + str(signature_number)
            candidate_list_path = os.path.join(out_path, "data", "statistical_analysis", "differential_expression_signature", "gene_symbols", signature_name+"_symbols.txt")
            gene_sets_out_path = os.path.join(differential_expression_signature_out_path, "over_representation_analysis")
            ora(candidate_list_path, background_path, global_variables, gene_sets_out_path, signature_name)

    return mde_dict