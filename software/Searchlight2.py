#!/usr/bin/env python2.7

import getopt
import sys
import timeit
import os
import shutil

from global_variables_setup.global_variables_setup import global_variables_setup
from input_variable_processing.input_variable_processing import input_variable_processing
from workflows.workflows import workflows
from shiny.shiny import shiny


# This section handles the input parameters:
if __name__ == '__main__':

    start_time = timeit.default_timer()
    version = "v2.0.0"

    print()
    print("#####################################")
    print("#####       Searchlight 2       #####")
    print("#####################################")
    print()
    print("Automated bulk RNA-seq data exploration and visualisation using dynamically generated R-scripts")
    print("John J. Cole & Carl S. Goodyear, et al.")
    print("University of Glasgow (Scotland) 2021")
    print()
    print(version)

    try:
        opts, args = getopt.getopt(sys.argv[1:], "", ["anno=", "out=", "ura=", "ora=", "ss=", "em=", "bg=", "de=", "mde=", "popex=", "config=", "gl=", "ignore_ne=", "ignore_de=", "ignore_mde="])
    except getopt.GetoptError as err:
        print(str(err))
        sys.exit(2)

    SL_path = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    annotations_parameter = None
    out_path_parameter = None
    ura_parameters = []
    ora_parameters = []
    ss_parameter = None
    norm_exp_parameter = None
    bg_parameter = None
    de_workflow_parameters = []
    mde_workflow_parameters = []
    popex_workflow_parameters = []
    gl_workflow_parameters = []
    config_file_parameter = None
    run_ne_wf = True
    run_de_wf = True
    run_mde_wf = True

    for o, a in opts:
        if o == "--config":
            config_file_path = a
        if o == "--anno":
            annotations_parameter = a
        if o == "--out":
            out_path_parameter = a
        if o == "--ura":
            ura_parameters.append(a)
        if o == "--ora":
            ora_parameters.append(a)
        if o == "--ss":
            ss_parameter = a
        if o == "--em":
            norm_exp_parameter = a
        if o == "--bg":
            bg_parameter = a
        if o == "--de":
            de_workflow_parameters.append(a)
        if o == "--mde":
            mde_workflow_parameters.append(a)
        if o == "--popex":
            popex_workflow_parameters.append(a)
        if o == "--gl":
            gl_workflow_parameters.append(a)
        if o == "--ignore_ne":
            run_ne_wf = False
        if o == "--ignore_de":
            run_de_wf = False
        if o == "--ignore_mde":
            run_mde_wf = False

    global_variables = global_variables_setup(annotations_parameter, ura_parameters, ora_parameters, ss_parameter, norm_exp_parameter, bg_parameter, de_workflow_parameters, mde_workflow_parameters, popex_workflow_parameters, config_file_parameter, out_path_parameter, SL_path, run_ne_wf, run_de_wf, run_mde_wf, version)
    global_variables = input_variable_processing(global_variables, annotations_parameter, ura_parameters, ora_parameters, ss_parameter, norm_exp_parameter, bg_parameter, de_workflow_parameters, mde_workflow_parameters, popex_workflow_parameters, out_path_parameter)
    workflows(global_variables)
    shiny(global_variables)


    print()
    print("Zipping results")
    print()
    shutil.make_archive(os.path.join(global_variables["out_path"], "results"), 'zip', global_variables["out_path"])


    stop_time = timeit.default_timer()
    print()
    print("Searchlight2 runtime: " + str(round((stop_time - start_time) / 60, 2)) + " minutes")
