
from .set_input_flags import set_input_flags
from .load_config_file import load_config_file


def global_variables_setup(annotations_parameter, ura_parameters, ora_parameters, ss_parameter, norm_exp_parameter, bg_parameter, de_workflow_parameters, mde_workflow_parameters, popex_workflow_parameters, config_file_parameter, out_path_parameter, SL_path,run_ne_wf,run_de_wf,run_mde_wf, version):

    print()
    print("=====================================")
    print("=====  global variables set-up  =====")
    print("=====================================")
    print()

    global_variables = {}
    global_variables["SL_path"] = SL_path
    global_variables["version"] = version

    global_variables = set_input_flags(global_variables, annotations_parameter, ura_parameters, ora_parameters, ss_parameter, norm_exp_parameter, bg_parameter, de_workflow_parameters, mde_workflow_parameters, popex_workflow_parameters, config_file_parameter, out_path_parameter,run_ne_wf,run_de_wf,run_mde_wf)
    global_variables = load_config_file(global_variables, config_file_parameter)

    return global_variables
