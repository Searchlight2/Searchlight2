from .ne.ne_workflow import ne_workflow
from .de.de_workflow import de_workflow
from .mde.mde_workflow import mde_workflow

from .biotypes.biotype_folders import biotype_folders

def workflows(global_variables):


    print("=====================================")
    print("=====         workflows         =====")
    print("=====================================")

    biotype_folders(global_variables)

    if global_variables["ne_flag"] and global_variables["ss_flag"] and global_variables["background_flag"] and global_variables["run_ne_wf_flag"] and len(list(global_variables["sample_groups"].keys())) > 0:
        ne_workflow(global_variables)

    if global_variables["de_workflows_flag"] and global_variables["ss_flag"] and global_variables["background_flag"] and global_variables["ne_flag"] and global_variables["run_de_wf_flag"]:
        de_workflow(global_variables)

    if global_variables["mde_workflows_flag"] and global_variables["ss_flag"] and global_variables["background_flag"] and global_variables["ne_flag"] and global_variables["de_workflows_flag"] and global_variables["run_mde_wf_flag"]:
        mde_workflow(global_variables)
