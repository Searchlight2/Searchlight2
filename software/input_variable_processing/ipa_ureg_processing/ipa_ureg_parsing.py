
def ipa_ureg_parsing(ipa_ureg_parameters, global_variables):
    parsed_ureg_parameters = []
    for ureg_parameter in ipa_ureg_parameters:

        # default sub-parameters
        ureg_file_path = None
        type = None
        zscore_threshold = 2.0
        p_threshold = 0.05
        fold_threshold = 0.0
        min_set_size = 5.0
        max_set_size = 250.0
        network_overlap_ratio = 0.25
        network_overlap_size = 5.0

        # gets the sub-parameters
        sub_params_list = ureg_parameter.split(",")
        for sub_param in sub_params_list:
            if sub_param.upper().startswith("file=".upper()):
                ureg_file_path = sub_param.split("=")[1]
            if sub_param.upper().startswith("type=".upper()):
                type = sub_param.split("=")[1].upper()
            if sub_param.upper().startswith("zscore=".upper()):
                zscore_threshold = float(sub_param.split("=")[1])
            if sub_param.upper().startswith("p.adj=".upper()):
                p_threshold = float(sub_param.split("=")[1])
            if sub_param.upper().startswith("log2fold=".upper()):
                fold_threshold = float(sub_param.split("=")[1])
            if sub_param.upper().startswith("min_set_size=".upper()):
                min_set_size = float(sub_param.split("=")[1])
            if sub_param.upper().startswith("max_set_size=".upper()):
                max_set_size = float(sub_param.split("=")[1])
            if sub_param.upper().startswith("network_overlap_ratio=".upper()):
                network_overlap_ratio = float(sub_param.split("=")[1])
            if sub_param.upper().startswith("network_overlap_size=".upper()):
                network_overlap_size = float(sub_param.split("=")[1])

        # parses the ureg file:
        ureg_dict = {}
        ureg_file = open(ureg_file_path).readlines()

        for line in ureg_file:
            line_split = line.rstrip().split("\t")
            ureg_name = line_split[0].upper()
            target_name = line_split[1].upper()
            direction = line_split[2].upper()

            if ureg_name in ureg_dict:
                ureg_targets_dict = ureg_dict[ureg_name]
                if target_name in ureg_targets_dict:
                    ureg_target_direction_list = ureg_targets_dict[target_name]
                else:
                    ureg_target_direction_list = [False,False,False]
            else:
                ureg_targets_dict = {}
                ureg_target_direction_list = [False, False, False]

            if direction.upper() == "ACTIVATION":
                ureg_target_direction_list[0] = True
            elif direction.upper() == "REPRESSION":
                ureg_target_direction_list[1] = True
            elif direction.upper() == "UNKNOWN":
                ureg_target_direction_list[2] = True

            ureg_targets_dict[target_name] = ureg_target_direction_list
            ureg_dict[ureg_name] = ureg_targets_dict


        # updates the information
        ureg_parameter_dict = {}
        ureg_parameter_dict["type"] = type
        ureg_parameter_dict["ureg"] = ureg_dict
        ureg_parameter_dict["zscore_threshold"] = zscore_threshold
        ureg_parameter_dict["p_threshold"] = p_threshold
        ureg_parameter_dict["fold_threshold"] = fold_threshold
        ureg_parameter_dict["min_set_size"] = min_set_size
        ureg_parameter_dict["max_set_size"] = max_set_size
        ureg_parameter_dict["network_overlap_ratio"] = network_overlap_ratio
        ureg_parameter_dict["network_overlap_size"] = network_overlap_size

        parsed_ureg_parameters.append(ureg_parameter_dict)
        print "parsed the ipa ureg parameter: " + ureg_parameter

    global_variables["ipa_ureg_parameters"] = parsed_ureg_parameters

    return global_variables