#!/usr/bin/env python2.7

import getopt
import sys
import timeit
import os

from global_variables_setup.global_variables_setup import global_variables_setup
from input_variable_processing.input_variable_processing import input_variable_processing
from workflows.workflows import workflows
from shiny.shiny import shiny


# This section handles the input parameters:
if __name__ == '__main__':

    start_time = timeit.default_timer()
    version = "v2.0.3"

    print
    print "#####################################"
    print "#####       Searchlight 2       #####"
    print "#####################################"
    print
    print "Rapid and comprehensive RNA-seq data exploration and visualisation for unlimited differential datasets"
    print "John J. Cole, Bekir Faydaci, Anargyros Megalios, Robin Shaw, Neil Robertson & Carl S. Goodyear"
    print "University of Glasgow"
    print
    print version

    try:
        opts, args = getopt.getopt(sys.argv[1:], "", ["anno=", "out=", "ureg=", "hgsea=", "ss=", "normexp=", "bg=", "pde=", "mpde=", "popex=", "config=", "gl=", "ignore_normexp=", "ignore_pde=", "ignore_mpde="])
    except getopt.GetoptError, err:
        print str(err)
        sys.exit(2)

    SL_path = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    annotations_parameter = None
    out_path_parameter = None
    ipa_ureg_parameters = []
    hypergeom_gs_parameters = []
    ss_parameter = None
    norm_exp_parameter = None
    bg_parameter = None
    pde_workflow_parameters = []
    mpde_workflow_parameters = []
    popex_workflow_parameters = []
    gl_workflow_parameters = []
    config_file_parameter = None
    run_normexp_wf = True
    run_pde_wf = True
    run_mpde_wf = True

    for o, a in opts:
        if o == "--config":
            config_file_path = a
        if o == "--anno":
            annotations_parameter = a
        if o == "--out":
            out_path_parameter = a
        if o == "--ureg":
            ipa_ureg_parameters.append(a)
        if o == "--hgsea":
            hypergeom_gs_parameters.append(a)
        if o == "--ss":
            ss_parameter = a
        if o == "--normexp":
            norm_exp_parameter = a
        if o == "--bg":
            bg_parameter = a
        if o == "--pde":
            pde_workflow_parameters.append(a)
        if o == "--mpde":
            mpde_workflow_parameters.append(a)
        if o == "--popex":
            popex_workflow_parameters.append(a)
        if o == "--gl":
            gl_workflow_parameters.append(a)
        if o == "--ignore_normexp":
            run_normexp_wf = False
        if o == "--ignore_pde":
            run_pde_wf = False
        if o == "--ignore_mpde":
            run_mpde_wf = False

    global_variables = global_variables_setup(annotations_parameter, ipa_ureg_parameters, hypergeom_gs_parameters, ss_parameter, norm_exp_parameter, bg_parameter, pde_workflow_parameters, mpde_workflow_parameters, popex_workflow_parameters, config_file_parameter, out_path_parameter, SL_path, run_normexp_wf, run_pde_wf, run_mpde_wf, version)
    global_variables = input_variable_processing(global_variables, annotations_parameter, ipa_ureg_parameters, hypergeom_gs_parameters, ss_parameter, norm_exp_parameter, bg_parameter, pde_workflow_parameters, mpde_workflow_parameters, popex_workflow_parameters, out_path_parameter)
    workflows(global_variables)
    shiny(global_variables)

    stop_time = timeit.default_timer()
    print
    print "Searchlight2 runtime: " + str(round((stop_time - start_time) / 60, 2)) + " minutes"
