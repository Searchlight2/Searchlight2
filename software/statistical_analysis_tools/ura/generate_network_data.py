import os


#   Generates the network nodes and edges
def generate_network_data(out_path,type,out_path_tag,network_overlap_ratio,network_overlap_size, ureg_results,zscore_threshold,p_threshold,fold_threshold):

    # does the work
    activated_nodes_dict,enriched_nodes_dict,enriched_and_activated_nodes_dict = make_nodes(out_path,type,out_path_tag, ureg_results, zscore_threshold,p_threshold,fold_threshold)
    make_edges(out_path, type, out_path_tag, "activated_uregs_edges.csv", activated_nodes_dict, network_overlap_ratio,network_overlap_size)
    make_edges(out_path, type, out_path_tag, "enriched_uregs_edges.csv", enriched_nodes_dict, network_overlap_ratio,network_overlap_size)
    make_edges(out_path, type, out_path_tag, "enriched_and_activated_uregs_edges.csv", enriched_and_activated_nodes_dict, network_overlap_ratio,network_overlap_size)


#   Make the nodes dictionary and file
def make_nodes(out_path,type,out_path_tag, ureg_results, zscore_threshold,p_threshold,fold_threshold):

    # opens the files
    if out_path_tag == "NONE":
        out_file_activated = open(os.path.join(out_path, type, "network_data", "activated_uregs_nodes.csv"), "w")
        out_file_enriched = open(os.path.join(out_path, type, "network_data", "enriched_uregs_nodes.csv"), "w")
        out_file_enriched_and_activated = open(os.path.join(out_path, type, "network_data", "enriched_and_activated_uregs_nodes.csv"), "w")
    else:
        out_file_activated = open(os.path.join(out_path, type, out_path_tag, "network_data", "activated_uregs_nodes.csv"), "w")
        out_file_enriched = open(os.path.join(out_path, type, out_path_tag, "network_data", "enriched_uregs_nodes.csv"), "w")
        out_file_enriched_and_activated = open(os.path.join(out_path, type, out_path_tag, "network_data", "enriched_and_activated_uregs_nodes.csv"), "w")

    header = ["node","enrichment_p_value","activation_zscore","node_size"]
    out_file_activated.write("\t".join(header) + "\n")
    out_file_enriched.write("\t".join(header) + "\n")
    out_file_enriched_and_activated.write("\t".join(header) + "\n")


    # dictionaries of nodes
    activated_nodes_dict = {}
    enriched_nodes_dict = {}
    enriched_and_activated_nodes_dict = {}


    #  iterate through the results:
    for result in ureg_results:

        node_name = result[0]
        zscore = float(result[1])
        hypergeometric_p = float(result[2])
        hypergeometric_p_bh = float(result[3])
        obs_vs_exp =  result[4]
        ureg_targets_size = float(result[5])
        activated_genes = result[6]
        inhibited_genes = result[7]
        target_genes = result[8]

        # generates node data
        if abs(float(zscore)) >= zscore_threshold:
            out_file_activated.write("\t".join([node_name,str(hypergeometric_p),str(zscore),str(ureg_targets_size)]) + "\n")
            activated_nodes_dict[node_name] = [target_genes, activated_genes, inhibited_genes, zscore]

        if obs_vs_exp != "NA":
            if abs(float(obs_vs_exp)) >= float(fold_threshold) and float(hypergeometric_p_bh) <= float(p_threshold):
                out_file_enriched.write("\t".join([node_name,str(hypergeometric_p),str(zscore),str(ureg_targets_size)]) + "\n")
                enriched_nodes_dict[node_name] = [target_genes, activated_genes, inhibited_genes, zscore]

            if abs(float(obs_vs_exp)) >= float(fold_threshold) and float(hypergeometric_p_bh) <= float(p_threshold) and abs(float(zscore)) >= zscore_threshold:
                out_file_enriched_and_activated.write("\t".join([node_name,str(hypergeometric_p),str(zscore),str(ureg_targets_size)]) + "\n")
                enriched_and_activated_nodes_dict[node_name] = [target_genes, activated_genes, inhibited_genes, zscore]

    return activated_nodes_dict,enriched_nodes_dict,enriched_and_activated_nodes_dict


#   Make edge files
def make_edges(out_path,type,out_path_tag, out_file_name,nodes_dict,network_overlap_ratio,network_overlap_size):


    # opens the out file
    if out_path_tag == "NONE":
        out_file = open(os.path.join(out_path, type, "network_data", out_file_name), "w")
    else:
        out_file = open(os.path.join(out_path, type, out_path_tag, "network_data", out_file_name), "w")

    header = ["source","target","overlap_ratio","overlap_size","concordant_activators_ratio", "concordant_activators_difference"]
    out_file.write("\t".join(header) + "\n")

    #   Get pairs of overlapping nodes. This will be the edges.
    #   Loop through the nodes and compare overlap.
    #   If overlap is less than overlap ignore, if over add nodes to dictionary.

    #   Make a list of all the keys
    node_keys = list(nodes_dict)

    #   Loop through the node keys and compare the gene lists between each pathway.
    for i, n1 in enumerate(node_keys):
        g1 = nodes_dict[n1][0]
        a1 = nodes_dict[n1][1]
        i1 = nodes_dict[n1][2]


        #   Compare the gene list with each
        for i_x in range(i + 1, len(node_keys)):
            g2 = nodes_dict[node_keys[i_x]][0]
            a2 = nodes_dict[node_keys[i_x]][1]
            i2 = nodes_dict[node_keys[i_x]][2]


            #   Use Szymkiewicz-Simpson coefficient for overlap.
            if g1 != [] and g2 != []:
                overlap_size = float(len(set(g1) & set(g2)))
                overlap_coefficient = overlap_size / float(min(len(g1), len(g2)))


                #   Determine number of concordant and discordant activators
                concordant_activators_overlap = 0
                if (a1 != [] and a2 != []):
                    concordant_activators_overlap = float(len(set(a1) & set(a2)))
                if (i1 != [] and i2 != []):
                    concordant_activators_overlap += float(len(set(i1) & set(i2)))

                discordant_activators_overlap = 0
                if (a1 != [] and i2 != []):
                    discordant_activators_overlap = float(len(set(a1) & set(i2)))
                if (a2 != [] and i1 != []):
                    discordant_activators_overlap += float(len(set(a2) & set(i1)))

                activators_concordancy_difference = concordant_activators_overlap - discordant_activators_overlap
                activatorsOverlapTotal = discordant_activators_overlap + concordant_activators_overlap
                activators_concordancy_overlap_ratio = 0
                if activatorsOverlapTotal > 0:
                    activators_concordancy_overlap_ratio = activators_concordancy_difference/activatorsOverlapTotal


                #   Determine the synergy / clash between the regulation patterns of the two nodes, at the overlapping genes:
                zscore1 = float(nodes_dict[n1][3])
                zscore2 = float(nodes_dict[node_keys[i_x]][3])

                if zscore1 == 0 or zscore2 == 0:
                    activators_concordancy_overlap_ratio = 0
                    activators_concordancy_difference = 0

                elif activators_concordancy_overlap_ratio > 0:
                    if zscore1 > 0 and zscore2 > 0:
                        activators_concordancy_overlap_ratio = abs(activators_concordancy_overlap_ratio)
                        activators_concordancy_difference = abs(activators_concordancy_difference)
                    if zscore1 > 0 and zscore2 < 0:
                        activators_concordancy_overlap_ratio = -abs(activators_concordancy_overlap_ratio)
                        activators_concordancy_difference = -abs(activators_concordancy_difference)
                    if zscore1 < 0 and zscore2 > 0:
                        activators_concordancy_overlap_ratio = -abs(activators_concordancy_overlap_ratio)
                        activators_concordancy_difference = -abs(activators_concordancy_difference)
                    if zscore1 < 0 and zscore2 < 0:
                        activators_concordancy_overlap_ratio = abs(activators_concordancy_overlap_ratio)
                        activators_concordancy_difference = abs(activators_concordancy_difference)

                elif activators_concordancy_overlap_ratio < 0:
                    if zscore1 > 0 and zscore2 > 0:
                        activators_concordancy_overlap_ratio = -abs(activators_concordancy_overlap_ratio)
                        activators_concordancy_difference = -abs(activators_concordancy_difference)
                    if zscore1 > 0 and zscore2 < 0:
                        activators_concordancy_overlap_ratio = abs(activators_concordancy_overlap_ratio)
                        activators_concordancy_difference = abs(activators_concordancy_difference)
                    if zscore1 < 0 and zscore2 > 0:
                        activators_concordancy_overlap_ratio = abs(activators_concordancy_overlap_ratio)
                        activators_concordancy_difference = abs(activators_concordancy_difference)
                    if zscore1 < 0 and zscore2 < 0:
                        activators_concordancy_overlap_ratio = -abs(activators_concordancy_overlap_ratio)
                        activators_concordancy_difference = -abs(activators_concordancy_difference)

                #  print the results
                if overlap_coefficient >= network_overlap_ratio and overlap_size >= network_overlap_size:
                    out_file.write("\t".join([n1, node_keys[i_x], str(overlap_coefficient), str(overlap_size), str(activators_concordancy_overlap_ratio), str(activators_concordancy_difference)]) + "\n")


