from statistical_analysis_tools.ura.sub_directories import sub_directories
from statistical_analysis_tools.ura.parse_ureg_file import parse_ureg_file
from statistical_analysis_tools.ura.ura_analysis import ura_analysis
from statistical_analysis_tools.ura.generate_network_data import generate_network_data


def ura(ipa_candidate_list_path,hypergeometric_candidate_list_path,background_list_path, global_variables, out_path,out_path_tag):

    parsed_ureg_parameters = global_variables["ura_parameters"]


    # Iterates through each gene set parameter:
    for ureg_parameter_dict in parsed_ureg_parameters:

        type = ureg_parameter_dict["type"]
        ureg_dict = ureg_parameter_dict["ureg"]
        zscore_threshold = ureg_parameter_dict["zscore_threshold"]
        p_threshold = ureg_parameter_dict["p_threshold"]
        fold_threshold = ureg_parameter_dict["fold_threshold"]
        min_set_size = ureg_parameter_dict["min_set_size"]
        max_set_size = ureg_parameter_dict["max_set_size"]
        network_overlap_ratio = ureg_parameter_dict["network_overlap_ratio"]
        network_overlap_size = ureg_parameter_dict["network_overlap_size"]

        # makes the sub directories:
        sub_directories(out_path, type, out_path_tag)

        # loads the background into a dictionary:
        background_dict = {}
        background_file = open(background_list_path).readlines()
        for line in background_file:
            background_dict[line.rstrip()] = True

        # loads the candidates into a dictionary (storing fold,p and p.adj - if they are valid):
        ipa_candidate_dict = {}
        candidate_file = open(ipa_candidate_list_path).readlines()
        for line in candidate_file:
            line_split = line.rstrip().split("\t")
            if line_split[10] == "True":
                ipa_candidate_dict[line_split[1].upper()] = [float(line_split[6]),float(line_split[7]),float(line_split[8])]
            else:
                ipa_candidate_dict[line_split[1].upper()] = [0.0, 1.0, 1.0]

        hypergeometric_candidate_dict = {}
        candidate_file = open(hypergeometric_candidate_list_path).readlines()
        for line in candidate_file:
            hypergeometric_candidate_dict[line.rstrip().upper()] = True

        # Parses the ureg file
        ureg_dict_parsed, gene_sets_dict_parsed = parse_ureg_file(ureg_dict, background_dict, min_set_size, max_set_size, out_path, type)

        # performs the analysis
        ureg_results = ura_analysis(ureg_dict_parsed,gene_sets_dict_parsed,background_dict,ipa_candidate_dict,hypergeometric_candidate_dict,zscore_threshold,p_threshold,fold_threshold,out_path,type,out_path_tag)

        # generates the network data
        generate_network_data(out_path,type,out_path_tag,network_overlap_ratio,network_overlap_size,ureg_results,zscore_threshold,p_threshold,fold_threshold)