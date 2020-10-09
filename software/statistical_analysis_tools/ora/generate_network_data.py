import os


#   Generates the network nodes and edges
def generate_network_data(out_path,type,out_path_tag,network_overlap_ratio,network_overlap_size):

    fold_column = 5
    p_neg_column = 6
    p_pos_column = 8
    genes_column = 10

    #   Make the nodes dictionary and files.
    neg_nodes_dict, pos_nodes_dict = get_nodes(out_path,type,out_path_tag,fold_column, p_pos_column, p_neg_column, genes_column)

    #   Create the edge file for the nodes.
    get_edges(neg_nodes_dict, os.path.join(out_path, type, out_path_tag, "network_data","enriched_gene_sets_edges.csv"), float(network_overlap_ratio), network_overlap_size)
    get_edges(pos_nodes_dict, os.path.join(out_path, type, out_path_tag, "network_data","underenriched_gene_sets_edges.csv"), float(network_overlap_ratio), network_overlap_size)


#   Make the nodes dictionary and file
def get_nodes(out_path,type,out_path_tag,fold_column, p_pos_column, p_neg_column, genes_column):



    #   load the hypergeometric result file
    in_file_neg = open(os.path.join(out_path,type,out_path_tag,"enriched_gene_sets_results.csv")).readlines()
    in_file_pos = open(os.path.join(out_path,type,out_path_tag,"underenriched_gene_sets_results.csv")).readlines()

    #  open the outfile:
    out_file_neg = open(os.path.join(out_path, type, out_path_tag, "network_data","enriched_gene_sets_nodes.csv"), 'w')
    out_file_pos = open(os.path.join(out_path, type, out_path_tag, "network_data","underenriched_gene_sets_nodes.csv"), 'w')

    # write headers
    out_file_neg.write("node\tlog2fold\tenrichment_p_value\tnode_size\n")
    out_file_pos.write("node\tlog2fold\tunderenrichment_p_value\tnode_size\n")

    # get a dictionary of all the nodes (gene sets).
    neg_nodes_dict = {}
    pos_nodes_dict = {}

    #  iterate through the neg file and get the nodes:
    first_line = True
    for line in in_file_neg:

        if first_line:
            first_line = False
        else:
            line_split = line.rstrip('\n').split('\t')
            genes = line_split[genes_column].split(',')
            neg_nodes_dict[line_split[0]] = genes
            out_file_neg.write(line_split[0] + "\t" + line_split[fold_column] + "\t" + line_split[p_neg_column] + "\t" + str(len(genes)) + "\n")

    #  iterate through the pos file and get the nodes:
    first_line = True
    for line in in_file_pos:

        if first_line:
            first_line = False
        else:
            line_split = line.rstrip('\n').split('\t')
            genes = line_split[genes_column].split(',')
            pos_nodes_dict[line_split[0]] = genes
            out_file_pos.write(line_split[0] + "\t" + line_split[fold_column] + "\t" + line_split[p_pos_column] + "\t" + str(len(genes)) + "\n")

    return neg_nodes_dict,pos_nodes_dict


#   Make edge files
def get_edges(nodes, outPathEdges, overlap_coefficient_cutOff, min_overlap_size):
    #   Create the edge list file
    fhand = open(outPathEdges, 'w+')
    fhand.write("Source\tTarget\toverlap_ratio\toverlap_size\n")

    #   Get pairs of overlapping nodes. This will be the edges.
    #   Loop through the nodes and compare overlap.
    #   If overlap is less than overlap ignore, if over add nodes to dictionary.

    #   Make a list of all the keys
    node_keys = list(nodes)
    edges = 0

    #   Loop through the node keys and compare the gene lists between each pathway.
    for i, n1 in enumerate(node_keys):
        g1 = nodes[n1]
        overlap_coefficient = 0.0

        #   Compare the gene list with each
        for i_x in range(i + 1, len(node_keys)):
            g2 = nodes[node_keys[i_x]]

            #   Use Szymkiewicz-Simpson coefficient for overlap.
            if g1[0] != '' and g2[0] != '':
                overlap_size = float(len(set(g1) & set(g2)))
                overlap_coefficient = overlap_size / float(min(len(g1), len(g2)))

            if overlap_coefficient >= overlap_coefficient_cutOff and overlap_size >= min_overlap_size:
                edge_txt = "%s\t%s\t%f\t%i\n"%(n1, node_keys[i_x], overlap_coefficient, overlap_size)
                fhand.write(edge_txt)

