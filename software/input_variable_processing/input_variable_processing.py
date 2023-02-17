# Core parameter imports
from .check_workflow_prerequisites.check_workflow_prerequisites import check_workflow_prerequisites

from .out_processing.out_validation import out_validation
from .out_processing.out_parsing import out_parsing

from .ss_processing.ss_validation import ss_validation
from .ss_processing.ss_parsing import ss_parsing

# Optional parameters imports
from .ne_processing.ne_validation import ne_validation
from .ne_processing.ne_parsing import ne_parsing
from .background_processing.background_validation import background_validation
from .background_processing.background_parsing import background_parsing
from .annotations_processing.annotations_validation import annotations_validation
from .annotations_processing.annotations_parsing import annotations_parsing
from .ora_processing.ora_validation import ora_validation
from .ora_processing.ora_parsing import ora_parsing
from .ura_processing.ura_validation import ura_validation
from .ura_processing.ura_parsing import ura_parsing


# Workflow imports
from .de_processing.de_validation import de_validation
from .de_processing.de_parsing import de_parsing
from .mde_processing.mde_validation import mde_validation
from .mde_processing.mde_parsing import mde_parsing

# Master table imports
from .construct_master_gene_table.construct_master_gene_table import construct_master_gene_table

# Processing report inputs
from .processing_report.processing_report import processing_report



# Parses the various input variables into a usable form, and checks that they are in the correct format
def input_variable_processing(global_variables, annotations_parameter,ura_parameters,ora_parameters,ss_parameter,norm_exp_parameter,bg_parameter,de_workflow_parameters, mde_workflow_parameters, popex_workflow_parameters, out_path_parameter):

    print()
    print("=====================================")
    print("===== input variable processing =====")
    print("=====================================")
    print()


    # Parses the outpath
    if global_variables["out_path_flag"] == True:
        out_validation(out_path_parameter, global_variables)
        global_variables = out_parsing(out_path_parameter, global_variables)

    # Parses SS
    if global_variables["ss_flag"] == True:
        ss_validation(ss_parameter)
        global_variables = ss_parsing(ss_parameter, global_variables)

    # Parses ne
    if global_variables["ne_flag"] == True:
        ne_validation(norm_exp_parameter, global_variables["sample_list"])
        global_variables = ne_parsing(norm_exp_parameter, global_variables)

    # Parses background
    if global_variables["background_flag"] == True:
        global_variables = background_validation(bg_parameter, global_variables)
        global_variables = background_parsing(bg_parameter, global_variables)

    # Parses annotations
    if global_variables["annotations_flag"] == True:
        annotations_validation(annotations_parameter)
        global_variables = annotations_parsing(annotations_parameter, global_variables)

    # Checks that the correct prerequisites to run searchlight have been supplied:
    check_workflow_prerequisites(global_variables)

    print()

    # Parses de workflows
    if global_variables["de_workflows_flag"] == True:
        de_validation(de_workflow_parameters,global_variables["sample_groups"])
        global_variables = de_parsing(de_workflow_parameters, global_variables)

    # Parses mde workflows
    if global_variables["mde_workflows_flag"] == True:
        mde_validation(mde_workflow_parameters, global_variables["sample_groups"], global_variables["de_parameters"])
        global_variables = mde_parsing(mde_workflow_parameters, global_variables)

    print()

    # Parses the gene sets
    if global_variables["ora_flag"] == True:
        ora_validation(ora_parameters)
        global_variables = ora_parsing(ora_parameters,global_variables)

    # Parses the ureg files
    if global_variables["ura_flag"] == True:
        ura_validation(ura_parameters)
        global_variables = ura_parsing(ura_parameters, global_variables)

    print()


    # Constructs the master gene table
    if global_variables["ss_flag"] and global_variables["background_flag"]:
        global_variables = construct_master_gene_table(global_variables)

    # Constructs the processing report
    processing_report(global_variables)

    return global_variables
