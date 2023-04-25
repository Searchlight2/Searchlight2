from subprocess import call
import os
import platform

def run_r(pr_dictionary, global_variables):

    # get the r  path
    r_path = os.path.join(pr_dictionary["workflow_outpath"], "plots", "workflow.r")

    # Run R - if a windows platform
    if platform.system() == "Windows":

        with open(os.devnull, "w") as f:
            call([global_variables["Rscript_path"], r_path], stderr=f, stdout=f)

    # Run R - if unix or linux
    else:
        with open(os.devnull, "w") as f:
            call([global_variables["Rscript_path"],r_path], stderr=f, stdout=f)


