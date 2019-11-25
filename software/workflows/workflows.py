from normexp.normexp_workflow import normexp_workflow
from pde.pde_workflow import pde_workflow
from mpde.mpde_workflow import mpde_workflow

from biotypes.biotype_folders import biotype_folders

def workflows(global_variables):


    print "====================================="
    print "=====         workflows         ====="
    print "====================================="

    biotype_folders(global_variables)

    if global_variables["normexp_flag"] and global_variables["ss_flag"] and global_variables["background_flag"] and global_variables["run_normexp_wf_flag"] and len(global_variables["sample_groups"].keys()) > 0:
        normexp_workflow(global_variables)

    if global_variables["pde_workflows_flag"] and global_variables["ss_flag"] and global_variables["background_flag"] and global_variables["normexp_flag"] and global_variables["run_pde_wf_flag"]:
        pde_workflow(global_variables)

    if global_variables["mpde_workflows_flag"] and global_variables["ss_flag"] and global_variables["background_flag"] and global_variables["normexp_flag"] and global_variables["pde_workflows_flag"] and global_variables["run_mpde_wf_flag"]:
        mpde_workflow(global_variables)
