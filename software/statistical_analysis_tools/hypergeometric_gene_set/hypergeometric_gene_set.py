from sub_directories import sub_directories
from parse_gmt_file import parse_gmt_file
from hypergeometric_analysis import hypergeometric_analysis
from generate_network_data import generate_network_data

def hypergeometric_gene_set(candidate_list_path,background_list_path, global_variables, out_path, out_path_tag):


    parsed_gene_sets_parameters = global_variables["hypergeom_gs_parameters"]

    # Iterates through each gene set parameter:
    for gene_set_parameter_dict in parsed_gene_sets_parameters:

        type = gene_set_parameter_dict["type"]
        gene_sets_dict = gene_set_parameter_dict["gene_sets"]
        p_threshold = gene_set_parameter_dict["p_threshold"]
        fold_threshold = gene_set_parameter_dict["fold_threshold"]
        min_set_size = gene_set_parameter_dict["min_set_size"]
        max_set_size = gene_set_parameter_dict["max_set_size"]
        network_overlap_ratio = gene_set_parameter_dict["network_overlap_ratio"]
        network_overlap_size = gene_set_parameter_dict["network_overlap_size"]

        # makes the sub directories:
        sub_directories(out_path,type,out_path_tag)

        # loads the background into a dictionary:
        background_dict = {}
        background_file = open(background_list_path).readlines()
        for line in background_file:
            background_dict[line.rstrip()] = True

        # loads the candidates into a dictionary:
        candidate_dict = {}
        candidate_file = open(candidate_list_path).readlines()
        for line in candidate_file:
            candidate_dict[line.rstrip()] = True

        # Parses the gmt file
        gene_sets_parsed = parse_gmt_file(gene_sets_dict,background_dict,min_set_size,max_set_size,out_path,type,out_path_tag)

        # performs the analysis
        hypergeometric_analysis(background_dict,candidate_dict,gene_sets_parsed,p_threshold,fold_threshold,out_path,type,out_path_tag)

        # generates the network data
        generate_network_data(out_path,type,out_path_tag,network_overlap_ratio,network_overlap_size)
