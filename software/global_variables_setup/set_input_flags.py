# sets up flags for which input variables have been supplied
def set_input_flags(global_variables, annotations_parameter, ura_parameters, ora_parameters, ss_parameter, norm_exp_parameter, bg_parameter, de_workflow_parameters, mde_workflow_parameters, popex_workflow_parameters, config_file_parameter, out_path_parameter,run_ne_wf,run_de_wf,run_mde_wf):



    if out_path_parameter != None:
        global_variables["out_path_flag"] = True
    else:
        global_variables["out_path_flag"] = False

    if annotations_parameter != None:
        global_variables["annotations_flag"] = True
    else:
        global_variables["annotations_flag"] = False

    if len(ura_parameters) > 0:
        global_variables["ura_flag"] = True
    else:
        global_variables["ura_flag"] = False

    if len(ora_parameters) > 0:
        global_variables["ora_flag"] = True
    else:
        global_variables["ora_flag"] = False

    if ss_parameter != None:
        global_variables["ss_flag"] = True
    else:
        global_variables["ss_flag"] = False

    if norm_exp_parameter != None:
        global_variables["ne_flag"] = True
    else:
        global_variables["ne_flag"] = False

    if bg_parameter != None:
        global_variables["background_flag"] = True
    else:
        global_variables["background_flag"] = False

    if config_file_parameter != None:
        global_variables["config_file_flag"] = True
    else:
        global_variables["config_file_flag"] = False

    if len(de_workflow_parameters) > 0:
        global_variables["de_workflows_flag"] = True
    else:
        global_variables["de_workflows_flag"] = False

    if len(mde_workflow_parameters) > 0:
        global_variables["mde_workflows_flag"] = True
    else:
        global_variables["mde_workflows_flag"] = False

    if len(popex_workflow_parameters) > 0:
        global_variables["popex_workflows_flag"] = True
    else:
        global_variables["popex_workflows_flag"] = False

    if len(popex_workflow_parameters) > 0:
        global_variables["popex_workflows_flag"] = True
    else:
        global_variables["popex_workflows_flag"] = False

    global_variables["run_ne_wf_flag"] = run_ne_wf
    global_variables["run_de_wf_flag"] = run_de_wf
    global_variables["run_mde_wf_flag"] = run_mde_wf






    print "input variables logged"


    return global_variables
