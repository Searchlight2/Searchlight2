
def out_parsing(out_path_parameter, global_variables):

    # default inputs
    out_path = None

    # gets the sub-parameters
    sub_params_list = out_path_parameter.split(",")

    for sub_param in sub_params_list:
        if sub_param.upper().startswith("path=".upper()):
            out_path = sub_param.split("=")[1]

    global_variables["out_path"] = out_path

    print("parsed the out parameter")

    return global_variables