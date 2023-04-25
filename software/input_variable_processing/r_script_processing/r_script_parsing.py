
def r_script_parsing(r_script_parameter, global_variables):

    # default inputs
    out_path = None

    # gets the sub-parameters
    sub_params_list = r_script_parameter.split(",")

    for sub_param in sub_params_list:
        if sub_param.upper().startswith("path=".upper()):
            r_script_path = sub_param.split("=")[1]

    global_variables["Rscript_path"] = r_script_path

    print("parsed the Rscript parameter")

    return global_variables