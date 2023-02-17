from statistical_analysis_tools.differential_expression_signature.get_meta_gene import get_meta_gene
from statistical_analysis_tools.differential_expression_signature.spearman_correlation import spearman_correlation

def merge_signatures(genes_by_signature, mde_dict, sample_list):

    # user defined threshold for merging
    scc_threshold = mde_dict["signatures_scc"]

    # for each signature, gets the mean z-score per sample
    meta_genes = get_meta_gene(genes_by_signature, sample_list)

    # gets the highest SCC
    highest_scc, signature1, signature2 = spearman_correlation(meta_genes)

    # test for SCC > threshold (then merge)
    while highest_scc > scc_threshold:

        # gets and adds the new signature
        signature1_genes = genes_by_signature[signature1]
        signature2_genes = genes_by_signature[signature2]
        merged_signature_genes = {}

        for gene in list(signature1_genes.keys()):
            merged_signature_genes[gene] = signature1_genes[gene]
        for gene in list(signature2_genes.keys()):
            merged_signature_genes[gene] = signature2_genes[gene]

        merged_signature_id =  "(" + signature1 + "\t" + signature2 + ")"
        genes_by_signature[merged_signature_id] = merged_signature_genes

        # delete the old signatures from genes by signatures
        del genes_by_signature[signature1]
        del genes_by_signature[signature2]

        #get the new meta genes and highest scc
        meta_genes = get_meta_gene(genes_by_signature, sample_list)
        highest_scc, signature1, signature2 = spearman_correlation(meta_genes)


    return genes_by_signature, meta_genes

