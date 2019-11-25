
from set_input_flags import set_input_flags
from load_config_file import load_config_file


def global_variables_setup(annotations_parameter, ipa_ureg_parameters, hypergeom_gs_parameters, ss_parameter, norm_exp_parameter, bg_parameter, pde_workflow_parameters, mpde_workflow_parameters, popex_workflow_parameters, config_file_parameter, out_path_parameter, SL_path,run_normexp_wf,run_pde_wf,run_mpde_wf, version):

    print
    print "====================================="
    print "=====  global variables set-up  ====="
    print "====================================="
    print

    global_variables = {}
    global_variables["SL_path"] = SL_path
    global_variables["version"] = version

    global_variables = set_input_flags(global_variables, annotations_parameter, ipa_ureg_parameters, hypergeom_gs_parameters, ss_parameter, norm_exp_parameter, bg_parameter, pde_workflow_parameters, mpde_workflow_parameters, popex_workflow_parameters, config_file_parameter, out_path_parameter,run_normexp_wf,run_pde_wf,run_mpde_wf)
    global_variables = load_config_file(global_variables, config_file_parameter)

    return global_variables
