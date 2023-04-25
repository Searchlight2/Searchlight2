

def mde_parsing(mde_workflow_parameters, global_variables):


    mde_parameters_parsed = []

    # parses each mde parameter
    for mde_parameter in mde_workflow_parameters:

        # default sub-parameters
        mde_name = None
        de_IDs = []
        sample_groups_list = []
        order_list = None
        mde_parameter_parsed = {}
        signatures_scc = 0.75


        # gets the sub-parameters
        sub_params_list = mde_parameter.split(",")
        for sub_param in sub_params_list:
            if sub_param.upper().startswith("name=".upper()):
                mde_name = sub_param.split("=")[1]
            if sub_param.upper().startswith("numerator=".upper()):
                de = sub_param.split("*")
                de_ID = de[0].split("=")[1].upper() + " vs " + de[1].split("=")[1].upper()
                de_IDs.append(de_ID)
                sample_groups_list.append(de[0].split("=")[1].upper())
                sample_groups_list.append(de[1].split("=")[1].upper())
            if sub_param.upper().startswith("order=".upper()):
                order_list = sub_param.upper().split("=")[1].split("+")
            if sub_param.upper().startswith("scc=".upper()):
                signatures_scc = float(sub_param.split("=")[1])


        # sets the order to the default (de order of groups) if unsupplied
        if order_list == None:
            order_list = []
            sample_groups_dict = {}
            for sample_group in sample_groups_list:
                if sample_group not in sample_groups_dict.keys():
                    order_list.append(sample_group)
                sample_groups_dict[sample_group] = True


        # stores the parsed parameter
        mde_parameter_parsed["mde_ID"] = mde_name
        mde_parameter_parsed["de_IDs"] = de_IDs
        mde_parameter_parsed["order_list"] = order_list
        mde_parameter_parsed["signatures_scc"] = signatures_scc
        mde_parameters_parsed.append(mde_parameter_parsed)

        print("parsed the mde parameter: " + mde_parameter)


    global_variables["mde_parameters"] = mde_parameters_parsed


    return global_variables