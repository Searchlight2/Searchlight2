# sets up flags for which input variables have been supplied
def set_input_flags(global_variables, annotations_parameter, ipa_ureg_parameters, hypergeom_gs_parameters, ss_parameter, norm_exp_parameter, bg_parameter, pde_workflow_parameters, mpde_workflow_parameters, popex_workflow_parameters, config_file_parameter, out_path_parameter,run_normexp_wf,run_pde_wf,run_mpde_wf):



    if out_path_parameter != None:
        global_variables["out_path_flag"] = True
    else:
        global_variables["out_path_flag"] = False

    if annotations_parameter != None:
        global_variables["annotations_flag"] = True
    else:
        global_variables["annotations_flag"] = False

    if len(ipa_ureg_parameters) > 0:
        global_variables["ipa_ureg_flag"] = True
    else:
        global_variables["ipa_ureg_flag"] = False

    if len(hypergeom_gs_parameters) > 0:
        global_variables["hypergeom_gs_flag"] = True
    else:
        global_variables["hypergeom_gs_flag"] = False

    if ss_parameter != None:
        global_variables["ss_flag"] = True
    else:
        global_variables["ss_flag"] = False

    if norm_exp_parameter != None:
        global_variables["normexp_flag"] = True
    else:
        global_variables["normexp_flag"] = False

    if bg_parameter != None:
        global_variables["background_flag"] = True
    else:
        global_variables["background_flag"] = False

    if config_file_parameter != None:
        global_variables["config_file_flag"] = True
    else:
        global_variables["config_file_flag"] = False

    if len(pde_workflow_parameters) > 0:
        global_variables["pde_workflows_flag"] = True
    else:
        global_variables["pde_workflows_flag"] = False

    if len(mpde_workflow_parameters) > 0:
        global_variables["mpde_workflows_flag"] = True
    else:
        global_variables["mpde_workflows_flag"] = False

    if len(popex_workflow_parameters) > 0:
        global_variables["popex_workflows_flag"] = True
    else:
        global_variables["popex_workflows_flag"] = False

    if len(popex_workflow_parameters) > 0:
        global_variables["popex_workflows_flag"] = True
    else:
        global_variables["popex_workflows_flag"] = False

    global_variables["run_normexp_wf_flag"] = run_normexp_wf
    global_variables["run_pde_wf_flag"] = run_pde_wf
    global_variables["run_mpde_wf_flag"] = run_mpde_wf






    print "input variables logged"


    return global_variables
