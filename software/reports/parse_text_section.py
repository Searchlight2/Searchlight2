# joins a list into "text format". I.e. items separated by "," except the final two which are separated by "and"
def join_with_and(list_to_join):

    if len(list_to_join) == 1:
        joined_list = str(list_to_join[0])
    else:
        joined_list = str(list_to_join[0])
        for i in range(1,len(list_to_join)-1):
            joined_list += ", " + str(list_to_join[i])
        joined_list += " and " + str(list_to_join[-1])

    return joined_list


def parse_text_section(text, pr_dictionary):


    if "<*SL2_version*>" in text:
        text = text.replace("<*SL2_version*>", pr_dictionary["version"])

    if "<*workflow_ID*>" in text:
        text = text.replace("<*workflow_ID*>", pr_dictionary["workflow_ID"])

    if "<*ne_file_path*>" in text:
        text = text.replace("<*ne_file_path*>", pr_dictionary["ne_file_path"])
    if "<*background_file_path*>" in text:
        text = text.replace("<*background_file_path*>", pr_dictionary["background_file_path"])
    if "<*expression_set_size*>" in text:
        text = text.replace("<*expression_set_size*>", str(pr_dictionary["expression_set_size"]))

    if "<*sample_groups*>" in text:
        text = text.replace("<*sample_groups*>", join_with_and(pr_dictionary["order_list"]).lower().replace("_"," "))

    if "<*de_padj*>" in text:
        text = text.replace("<*de_padj*>", str(pr_dictionary["de_p_threshold"]))
    if "<*de_log2fold*>" in text:
        text = text.replace("<*de_log2fold*>", str(pr_dictionary["de_fold_threshold"]))
    if "<*de_numerator*>" in text:
        text = text.replace("<*de_numerator*>", str(pr_dictionary["de_numerator_group"]).lower().replace("_"," "))
    if "<*de_denominator*>" in text:
        text = text.replace("<*de_denominator*>", str(pr_dictionary["de_denominator_group"]).lower().replace("_"," "))
    if "<*de_file_path*>" in text:
        text = text.replace("<*de_file_path*>", str(pr_dictionary["de_file_path"]))
    if "<*differential_expression_set_size*>" in text:
        text = text.replace("<*differential_expression_set_size*>", str(pr_dictionary["differential_expression_set_size"]))

    if "<*mde_comparisons*>" in text:
        text = text.replace("<*mde_comparisons*>", join_with_and(pr_dictionary["comparisons"]).lower().replace("_"," "))
    if "<*signatures_SCC*>" in text:
        text = text.replace("<*signatures_SCC*>", str(pr_dictionary["signatures_scc"]))

    if "<*hypergeom_gene_set_databases*>" in text:
        text = text.replace("<*hypergeom_gene_set_databases*>", join_with_and(pr_dictionary["hypergeom_gene_set_types"]).replace("_"," "))
    if "<*hypergeom_gene_set_min_set_size*>" in text:
        text = text.replace("<*hypergeom_gene_set_min_set_size*>", str(pr_dictionary["hypergeom_gene_set_min_set_sizes"][0]))
    if "<*hypergeom_gene_set_max_set_size*>" in text:
        text = text.replace("<*hypergeom_gene_set_max_set_size*>", str(pr_dictionary["hypergeom_gene_set_max_set_sizes"][0]))
    if "<*hypergeom_gene_set_padj*>" in text:
        text = text.replace("<*hypergeom_gene_set_padj*>", str(pr_dictionary["hypergeom_gene_set_p_thresholds"][0]))
    if "<*hypergeom_gene_set_log2fold*>" in text:
        text = text.replace("<*hypergeom_gene_set_log2fold*>", str(pr_dictionary["hypergeom_gene_set_fold_thresholds"][0]))
    if "<*hypergeom_gene_set_overlap*>" in text:
        text = text.replace("<*hypergeom_gene_set_overlap*>", str(pr_dictionary["hypergeom_gene_set_network_overlap_ratios"][0]))

    if "<*ura_databases*>" in text:
        text = text.replace("<*ura_databases*>", join_with_and(pr_dictionary["ura_types"]).replace("_"," "))
    if "<*ura_min_set_size*>" in text:
        text = text.replace("<*ura_min_set_size*>", str(pr_dictionary["ura_min_set_sizes"][0]))
    if "<*ura_max_set_size*>" in text:
        text = text.replace("<*ura_max_set_size*>", str(pr_dictionary["ura_max_set_sizes"][0]))
    if "<*ura_padj*>" in text:
        text = text.replace("<*ura_padj*>", str(pr_dictionary["ura_p_thresholds"][0]))
    if "<*ura_log2fold*>" in text:
        text = text.replace("<*ura_log2fold*>", str(pr_dictionary["ura_fold_thresholds"][0]))
    if "<*ura_zscore*>" in text:
        text = text.replace("<*ura_zscore*>", str(pr_dictionary["ura_zscore_thresholds"][0]))
    if "<*ura_overlap*>" in text:
        text = text.replace("<*ura_overlap*>", str(pr_dictionary["ura_overlap_ratios"][0]))


    return text







