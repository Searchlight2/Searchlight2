import os
from statistical_analysis_tools.differential_expression_signature.differential_expression_signature import differential_expression_signature
from statistical_analysis_tools.hypergeometric_gene_set.hypergeometric_gene_set import hypergeometric_gene_set

def differential_expression_signature_helper(global_variables, out_path, pde_IDs, mpde_dict):

    # runs the signature analysis
    signature_candidate_list_path = os.path.join(out_path, "data", "genes_significant_in_any_PDEs_annotated.csv")
    differential_expression_signature_out_path = os.path.join(out_path, "data", "statistical_analysis", "differential_expression_signature")
    mpde_dict = differential_expression_signature(global_variables, signature_candidate_list_path, differential_expression_signature_out_path, pde_IDs, mpde_dict)


    # runs the gene-set analysis for each signature
    if global_variables["hypergeom_gs_flag"] == True:
        background_path = os.path.join(out_path, "data", "gene_symbols", "all_gene_symbols.txt")

        for signature_number in mpde_dict["de_signatures"]:
            signature_name = "signature_" + str(signature_number)
            candidate_list_path = os.path.join(out_path, "data", "statistical_analysis", "differential_expression_signature", "gene_symbols", signature_name+"_symbols.txt")
            gene_sets_out_path = os.path.join(differential_expression_signature_out_path, "hypergeometric_gene_set")
            hypergeometric_gene_set(candidate_list_path, background_path, global_variables, gene_sets_out_path, signature_name)

    return mpde_dict