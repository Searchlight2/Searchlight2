import scipy.stats as stats
import math
from math import sqrt
import os
from misc.multi_sample_correction import msCorrect

#Controller:
def ura_analysis(ureg_dict,gene_sets_dict,background_dict,ipa_candidate_dict,hypergeometric_candidate_dict,zscore_threshold,p_threshold,fold_threshold,out_path,type,out_path_tag):

    # perform the tests
    hypergeometric_results_list = hypergeometric_processing(background_dict, hypergeometric_candidate_dict, gene_sets_dict)
    ura_results_dict = ura_processing(ureg_dict, ipa_candidate_dict)

    # stores the combined results:
    combined_ureg_results = []

    # create output files
    if out_path_tag == "NONE":
        out_file_all = open(os.path.join(out_path,type,"all_uregs_results.csv"), "w")
        out_file_sig_hyper = open(os.path.join(out_path,type,"enriched_uregs_results.csv"), "w")
        out_file_sig_zscore = open(os.path.join(out_path,type,"activated_uregs_results.csv"), "w")
        out_file_sig_both = open(os.path.join(out_path,type,"enriched_and_activated_uregs_results.csv"), "w")
    else:
        out_file_all = open(os.path.join(out_path,type,out_path_tag,"all_uregs_results.csv"), "w")
        out_file_sig_hyper = open(os.path.join(out_path,type,out_path_tag,"enriched_uregs_results.csv"), "w")
        out_file_sig_zscore = open(os.path.join(out_path,type,out_path_tag,"activated_uregs_results.csv"), "w")
        out_file_sig_both = open(os.path.join(out_path,type,out_path_tag,"enriched_and_activated_uregs_results.csv"), "w")

    header_list = ["upstream_regulator","activation_zscore","enrichment_p_value", "enrichment_p.BH_value", "log2_fold_enrichment", "genes_in_background","target_genes", "genes_activated", "genes_inhibited", "candidate_genes", "overlapping_genes", "bias_term","activated_gene_names","inhibited_gene_names","overlapping_gene_names"]

    out_file_all.write("\t".join(header_list) + "\n")
    out_file_sig_hyper.write("\t".join(header_list) + "\n")
    out_file_sig_zscore.write("\t".join(header_list) + "\n")
    out_file_sig_both.write("\t".join(header_list) + "\n")


    # print results to file
    for hypergeometric_result in hypergeometric_results_list:
        ureg = hypergeometric_result[0]
        background_size = hypergeometric_result[1]
        candidate_size = hypergeometric_result[2]
        ureg_targets_size = hypergeometric_result[3]
        overlap_size = hypergeometric_result[4]
        obs_vs_exp = hypergeometric_result[5]
        p_neg = hypergeometric_result[6]
        p_bh_neg = hypergeometric_result[7]
        p_pos = hypergeometric_result[8]
        p_bh_pos = hypergeometric_result[9]
        overlapping_genes = sorted(hypergeometric_result[10])

        ura_result = ura_results_dict[ureg]
        zscore = ura_result[0]
        bias_term = ura_result[1]
        n_activated = ura_result[2]
        n_inhibited = ura_result[3]
        genes_activated = sorted(ura_result[4])
        genes_inhibited = sorted(ura_result[5])
        target_genes = sorted(ura_result[6])

        out_list = [ureg,zscore,p_neg,p_bh_neg,obs_vs_exp,background_size,ureg_targets_size,n_activated,n_inhibited,candidate_size,overlap_size,bias_term,",".join(genes_activated),",".join(genes_inhibited),",".join(overlapping_genes)]

        out_file_all.write("\t".join(str(x) for x in out_list) + "\n")
        combined_ureg_results.append([ureg, zscore, p_neg, p_bh_neg, obs_vs_exp, ureg_targets_size, genes_activated, genes_inhibited, target_genes])

        if abs(float(zscore)) >= zscore_threshold:
            out_file_sig_zscore.write("\t".join(str(x) for x in out_list) + "\n")

        if obs_vs_exp != "NA":
            if abs(float(obs_vs_exp)) >= float(fold_threshold) and float(p_bh_neg) <= float(p_threshold):
                out_file_sig_hyper.write("\t".join(str(x) for x in out_list) + "\n")
            if abs(float(obs_vs_exp)) >= float(fold_threshold) and float(p_bh_neg) <= float(p_threshold) and abs(float(zscore)) >= zscore_threshold:
                out_file_sig_both.write("\t".join(str(x) for x in out_list) + "\n")


    return combined_ureg_results



def hypergeometric_processing(background_dict, hypergeometric_candidate_dict, gene_sets_parsed):

    p_pos_list = []
    p_neg_list = []
    result_list = []

    background_size = len(background_dict.keys())
    candidate_size = len(hypergeometric_candidate_dict.keys())

    # iterates through the gene sets
    for gene_set in gene_sets_parsed:

        genes_in_gene_set = gene_sets_parsed[gene_set]
        gene_set_size = len(genes_in_gene_set)

        # gets the overlap
        overlapping_genes = []
        for gene in genes_in_gene_set:
            if gene.upper() in hypergeometric_candidate_dict:
                overlapping_genes.append(gene.upper())

        overlap_size = len(overlapping_genes)

        # does the hypergeometric test:
        obs_vs_exp, p_Pos, p_Neg = hypergeometric(background_size, candidate_size, gene_set_size,overlap_size)
        p_pos_list.append(p_Pos)
        p_neg_list.append(p_Neg)
        result_list.append([gene_set, str(background_size), str(candidate_size), str(gene_set_size), str(overlap_size),str(obs_vs_exp), str(p_Neg), str(p_Pos), overlapping_genes])

    # multisample corrects:
    p_pos_list_BH = msCorrect(p_pos_list, correction_type="Benjamini-Hochberg")
    p_neg_list_BH = msCorrect(p_neg_list, correction_type="Benjamini-Hochberg")

    line_counter = 0
    for result in result_list:

        result.insert(7, str(p_neg_list_BH[line_counter]))
        result.insert(9, str(p_pos_list_BH[line_counter]))
        line_counter += 1

    return result_list


# Method to get the hypergeometric overlap p-value and fold:
def hypergeometric(background_size, candidate_size, gene_set_size, overlap_size):

    p_Pos = stats.hypergeom.cdf(overlap_size, background_size, candidate_size, gene_set_size)
    p_Neg = stats.hypergeom.sf(overlap_size - 1, background_size, candidate_size, gene_set_size)

    if candidate_size > 0 and gene_set_size > 0 and overlap_size > 0:
        exp = (float(gene_set_size) / float(background_size)) * float(candidate_size)
        obs_vs_exp = math.log(float(overlap_size), 2) - math.log(float(exp), 2)

    else:
        obs_vs_exp = "NA"

    return obs_vs_exp, p_Pos, p_Neg



#Gets the upstream regulator enrichment stats:
def ura_processing(ureg_dict, ipa_candidate_dict):

    ureg_results_dict = {}


    # gets the data bias
    n_up = 0
    n_down = 0
    for gene in ipa_candidate_dict:
        log2fold = ipa_candidate_dict[gene][0]
        if log2fold > 0:
            n_up +=1
        elif log2fold < 0:
            n_down +=1
    u_data = float(n_up - n_down) / float(n_up + n_down)


    #iterates through the uregs and gets the weighted z-score:
    for ureg_name in ureg_dict:
        ureg_targets_dict = ureg_dict[ureg_name]

        n_activated = 0
        n_inhibited = 0
        genes_activated = []
        genes_inhibited = []
        x = 0
        alpha_x = 0

        for target_name in ureg_targets_dict:
            ureg_target_direction_list = ureg_targets_dict[target_name]
            target_direction = ipa_candidate_dict[target_name][0]
            target_weight = 1.00 - float(ipa_candidate_dict[target_name][1])
            target_weight_squared = target_weight * target_weight

            # gets the activation and inhibition counts / weighted counts
            if ureg_target_direction_list[0] and not ureg_target_direction_list[1]:
                if target_direction > 0:
                    n_activated += 1
                    genes_activated.append(target_name)
                    x += target_weight
                    alpha_x += target_weight_squared

                elif target_direction < 0:
                    n_inhibited += 1
                    genes_inhibited.append(target_name)
                    x -= target_weight
                    alpha_x += target_weight_squared

            if ureg_target_direction_list[1] and not ureg_target_direction_list[0]:
                if target_direction < 0:
                    n_activated += 1
                    genes_activated.append(target_name)
                    x += target_weight
                    alpha_x += target_weight_squared

                elif target_direction > 0:
                    n_inhibited += 1
                    genes_inhibited.append(target_name)
                    x -= target_weight
                    alpha_x += target_weight_squared

        # gets the z-score
        if n_up + n_down > 0 and n_activated + n_inhibited > 0:
            alpha_x = float(sqrt(alpha_x))
            u_tr = float(n_activated - n_inhibited) / float(n_activated + n_inhibited)
            bias_term = float(u_data) * float(u_tr)
            zscore = (x - alpha_x) / alpha_x

            ureg_results_dict[ureg_name] = [zscore+1,bias_term,n_activated,n_inhibited,genes_activated,genes_inhibited, ureg_targets_dict.keys()]

        else:
            ureg_results_dict[ureg_name] = [0.0, 0.0, 0.0, 0.0, [], [],[]]


    return ureg_results_dict