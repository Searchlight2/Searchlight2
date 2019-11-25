import os

# core workflow imports
from sub_directories.core_sub_directories import core_sub_directories
from output_files.normexp_matrix_IDs import normexp_matrix_IDs
from output_files.normexp_matrix_annotated import normexp_matrix_annotated
from output_files.normexp_matrix_symbols import normexp_matrix_symbols
from output_files.normexp_gene_IDs import normexp_gene_IDs
from output_files.normexp_gene_symbols import normexp_gene_symbols

# plot imports
from plots.start_plots import start_plots
from plots.add_plot import add_plot
from plots.end_plots import end_plots
from plots.run_r import run_r

# report imports
from reports.start_report import start_report
from reports.add_header_section_to_report import add_header_section_to_report
from reports.add_plot_section_to_report import add_plot_section_to_report
from reports.add_text_section_to_report import add_text_section_to_report
from reports.end_report import end_report


# runs the workflow
def run_normexp_workflow(global_variables, biotype):

    print "-" * len(list(biotype))
    print biotype
    print "-" * len(list(biotype))
    print

    # gets the config for the workflow
    config = global_variables["config"]["NORMEXP"]

    # gets the outpath for the workflow - as we use this a lot
    out_path = os.path.join(global_variables["out_path"], biotype, "normexp_workflow")

    for element in config:

        element_name, element_active, element_type, element_subtype, element_path = element

        if check_element_prerequisites(element_active, element_type, element_subtype, element_path, global_variables):

            # methods for the core workflow
            if element_name == "normexp_sub_directories_core" and element_type == "core":
                core_sub_directories(global_variables, out_path)
            elif element_name == "normexp_file_matrix_annotated" and element_type == "core":
                normexp_matrix_annotated(global_variables, out_path, biotype)
            elif element_name == "normexp_file_matrix_IDs" and element_type == "core":
                normexp_matrix_IDs(global_variables, out_path, biotype)
            elif element_name == "normexp_file_matrix_symbols" and element_type == "core":
                normexp_matrix_symbols(global_variables, out_path, biotype)
            elif element_name == "normexp_file_gene_IDs" and element_type == "core":
                normexp_gene_IDs(global_variables, out_path, biotype)
            elif element_name == "normexp_file_gene_symbols" and element_type == "core":
                normexp_gene_symbols(global_variables, out_path, biotype)

            # methods for statistical analysis

            # methods for the plots
            elif element_name == "normexp_start_plots" and element_type == "plot_core":
                pr_dictionary = start_plots(global_variables, out_path, "NORMEXP", None)
            elif element_type == "plot":
                add_plot(element_path, pr_dictionary)
            elif element_name == "normexp_end_plots" and element_type == "plot_core":
                end_plots(pr_dictionary)
            elif element_name == "normexp_run_r" and element_type == "plot_core":
                run_r(pr_dictionary)

            # methods for the report
            elif element_name == "normexp_start_report" and element_type == "report_core":
                start_report(global_variables, pr_dictionary, element_path)
            elif element_type == "report_title":
                add_header_section_to_report(element_path, pr_dictionary)
            elif element_type == "report_text":
                add_text_section_to_report(element_path, pr_dictionary, global_variables)
            elif element_type == "report_plot":
                add_plot_section_to_report(element_path, pr_dictionary, global_variables)
            elif element_name == "normexp_end_report" and element_type == "report_core":
                end_report(pr_dictionary)
            print "done with: " + element_name.replace("_", " ")

    print


# checks that prerequisites have been met for running an elements command
def check_element_prerequisites(element_active, element_type, element_subtype, element_path, global_variables):

    if element_active == "FALSE":
        return False
    elif element_subtype == "hypergeometric_gene_set" and global_variables["hypergeom_gs_flag"] == False:
        return False
    elif element_subtype == "ipa_ureg" and global_variables["ipa_ureg_flag"] == False:
        return False
    elif element_type == "plot" and element_path.upper() == "NONE":
        return False
    else:
        return True