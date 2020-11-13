import os
from misc.multi_sample_correction import msCorrect
from misc.ora_test import hypergeometric_test

def hypergeometric_analysis(background_dict,candidate_dict,gene_sets_parsed,p_threshold,fold_threshold,out_path,type,out_path_tag):

    p_pos_list = []
    p_neg_list = []
    result_list = []

    background_size = len(background_dict.keys())
    candidate_size = len(candidate_dict.keys())

    # iterates through the gene sets
    for gene_set in gene_sets_parsed:

        genes_in_gene_set = gene_sets_parsed[gene_set]
        gene_set_size = len(genes_in_gene_set)

        # gets the overlap
        overlapping_genes = []
        for gene in genes_in_gene_set:
            if gene.upper() in candidate_dict:
                overlapping_genes.append(gene.upper())

        overlap_size =  len(overlapping_genes)

        # does the hypergeometric test:
        obs_vs_exp, p_Pos, p_Neg = hypergeometric_test(background_size, candidate_size, gene_set_size, overlap_size)
        p_pos_list.append(p_Pos)
        p_neg_list.append(p_Neg)
        result_list.append([gene_set, str(background_size), str(candidate_size), str(gene_set_size), str(overlap_size), str(obs_vs_exp), str(p_Neg), str(p_Pos), ",".join(sorted(overlapping_genes))])


    # multisample corrects:
    p_pos_list_BH = msCorrect(p_pos_list, correction_type="Benjamini-Hochberg")
    p_neg_list_BH = msCorrect(p_neg_list, correction_type="Benjamini-Hochberg")


    # prints the results
    out_file_all = open(os.path.join(out_path,type,out_path_tag,"all_gene_sets_results.csv"), "w")
    out_file_neg = open(os.path.join(out_path,type,out_path_tag,"enriched_gene_sets_results.csv"), "w")
    out_file_pos = open(os.path.join(out_path,type,out_path_tag,"underenriched_gene_sets_results.csv"), "w")

    out_file_all.write("\t".join(["gene_set", "genes_in_background", "candidate_genes","gene_set_genes", "overlapping_genes", "log2_fold_enrichment","enrichment_p_value", "enrichment_p.BH_value", "underenrichment_p_value", "underenrichment_p.BH_value","overlapping_gene_names"]) + "\n")
    out_file_pos.write("\t".join(["gene_set", "genes_in_background", "candidate_genes","gene_set_genes", "overlapping_genes", "log2_fold_enrichment","enrichment_p_value", "enrichment_p.BH_value", "underenrichment_p_value", "underenrichment_p.BH_value","overlapping_gene_names"]) + "\n")
    out_file_neg.write("\t".join(["gene_set", "genes_in_background", "candidate_genes","gene_set_genes", "overlapping_genes", "log2_fold_enrichment","enrichment_p_value", "enrichment_p.BH_value", "underenrichment_p_value", "underenrichment_p.BH_value","overlapping_gene_names"]) + "\n")


    line_counter = 0
    for result in result_list:

        result.insert(7, str(p_neg_list_BH[line_counter]))
        result.insert(9, str(p_pos_list_BH[line_counter]))
        out_file_all.write("\t".join(result) + "\n")

        if result[5] != "NA":
            if abs(float(result[5])) >= float(fold_threshold) and float(result[7]) <= float(p_threshold):
                out_file_neg.write("\t".join(result) + "\n")

        if result[5] != "NA":
            if abs(float(result[5])) >= float(fold_threshold) and float(result[9]) <= float(p_threshold):
                out_file_pos.write("\t".join(result) + "\n")



        line_counter += 1


