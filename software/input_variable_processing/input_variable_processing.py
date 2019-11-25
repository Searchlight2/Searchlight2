# Core parameter imports
from check_workflow_prerequisites.check_workflow_prerequisites import check_workflow_prerequisites

from out_processing.out_validation import out_validation
from out_processing.out_parsing import out_parsing

from ss_processing.ss_validation import ss_validation
from ss_processing.ss_parsing import ss_parsing

# Optional parameters imports
from normexp_processing.normexp_validation import normexp_validation
from normexp_processing.normexp_parsing import normexp_parsing
from background_processing.background_validation import background_validation
from background_processing.background_parsing import background_parsing
from annotations_processing.annotations_validation import annotations_validation
from annotations_processing.annotations_parsing import annotations_parsing
from hypergeom_gs_processing.hypergeom_gs_validation import hypergeom_gs_validation
from hypergeom_gs_processing.hypergeom_gs_parsing import hypergeom_gs_parsing
from ipa_ureg_processing.ipa_ureg_validation import ipa_ureg_validation
from ipa_ureg_processing.ipa_ureg_parsing import ipa_ureg_parsing


# Workflow imports
from pde_processing.pde_validation import pde_validation
from pde_processing.pde_parsing import pde_parsing
from mpde_processing.mpde_validation import mpde_validation
from mpde_processing.mpde_parsing import mpde_parsing

# Master table imports
from construct_master_gene_table.construct_master_gene_table import construct_master_gene_table

# Processing report inputs
from processing_report.processing_report import processing_report



# Parses the various input variables into a usable form, and checks that they are in the correct format
def input_variable_processing(global_variables, annotations_parameter,ipa_ureg_parameters,hypergeom_gs_parameters,ss_parameter,norm_exp_parameter,bg_parameter,pde_workflow_parameters, mpde_workflow_parameters, popex_workflow_parameters, out_path_parameter):

    print
    print "====================================="
    print "===== input variable processing ====="
    print "====================================="
    print


    # Parses the outpath
    if global_variables["out_path_flag"] == True:
        out_validation(out_path_parameter, global_variables)
        global_variables = out_parsing(out_path_parameter, global_variables)

    # Parses SS
    if global_variables["ss_flag"] == True:
        ss_validation(ss_parameter)
        global_variables = ss_parsing(ss_parameter, global_variables)

    # Parses normexp
    if global_variables["normexp_flag"] == True:
        normexp_validation(norm_exp_parameter, global_variables["sample_list"])
        global_variables = normexp_parsing(norm_exp_parameter, global_variables)

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

    print

    # Parses pde workflows
    if global_variables["pde_workflows_flag"] == True:
        pde_validation(pde_workflow_parameters,global_variables["sample_groups"])
        global_variables = pde_parsing(pde_workflow_parameters, global_variables)

    # Parses mpde workflows
    if global_variables["mpde_workflows_flag"] == True:
        mpde_validation(mpde_workflow_parameters, global_variables["sample_groups"], global_variables["pde_parameters"])
        global_variables = mpde_parsing(mpde_workflow_parameters, global_variables)

    print

    # Parses the gene sets
    if global_variables["hypergeom_gs_flag"] == True:
        hypergeom_gs_validation(hypergeom_gs_parameters)
        global_variables = hypergeom_gs_parsing(hypergeom_gs_parameters,global_variables)

    # Parses the ureg files
    if global_variables["ipa_ureg_flag"] == True:
        ipa_ureg_validation(ipa_ureg_parameters)
        global_variables = ipa_ureg_parsing(ipa_ureg_parameters, global_variables)

    print


    # Constructs the master gene table
    if global_variables["ss_flag"] and global_variables["background_flag"]:
        global_variables = construct_master_gene_table(global_variables)

    # Constructs the processing report
    processing_report(global_variables)

    return global_variables
