

def mpde_parsing(mpde_workflow_parameters, global_variables):


    mpde_parameters_parsed = []

    # parses each mpde parameter
    for mpde_parameter in mpde_workflow_parameters:

        # default sub-parameters
        mpde_name = None
        pde_IDs = []
        sample_groups_list = []
        order_list = None
        mpde_parameter_parsed = {}
        signatures_scc = 0.75


        # gets the sub-parameters
        sub_params_list = mpde_parameter.split(",")
        for sub_param in sub_params_list:
            if sub_param.upper().startswith("name=".upper()):
                mpde_name = sub_param.split("=")[1]
            if sub_param.upper().startswith("numerator=".upper()):
                pde = sub_param.split("*")
                pde_ID = pde[0].split("=")[1].upper() + " vs " + pde[1].split("=")[1].upper()
                pde_IDs.append(pde_ID)
                sample_groups_list.append(pde[0].split("=")[1].upper())
                sample_groups_list.append(pde[1].split("=")[1].upper())
            if sub_param.upper().startswith("order=".upper()):
                order_list = sub_param.upper().split("=")[1].split("+")
            if sub_param.upper().startswith("scc=".upper()):
                signatures_scc = float(sub_param.split("=")[1])


        # sets the order to the default (PDE order of groups) if unsupplied
        if order_list == None:
            order_list = []
            sample_groups_dict = {}
            for sample_group in sample_groups_list:
                if sample_group not in sample_groups_dict.keys():
                    order_list.append(sample_group)
                sample_groups_dict[sample_group] = True


        # stores the parsed parameter
        mpde_parameter_parsed["mpde_ID"] = mpde_name
        mpde_parameter_parsed["pde_IDs"] = pde_IDs
        mpde_parameter_parsed["order_list"] = order_list
        mpde_parameter_parsed["signatures_scc"] = signatures_scc
        mpde_parameters_parsed.append(mpde_parameter_parsed)

        print "parsed the mpde parameter: " + mpde_parameter


    global_variables["mpde_parameters"] = mpde_parameters_parsed


    return global_variables