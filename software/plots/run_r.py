from subprocess import call
import os

def run_r(pr_dictionary):
    with open(os.devnull, "w") as f: call(["Rscript",os.path.join(pr_dictionary["workflow_outpath"],"plots","workflow.r")], stderr=f, stdout=f)