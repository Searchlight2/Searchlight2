import os

# core workflow imports
from workflows.mde.sub_directories.core_sub_directories import core_sub_directories
from workflows.mde.output_files.MDPE_IDs import Mde_IDs
from workflows.mde.output_files.Mde_symbols import Mde_symbols
from workflows.mde.output_files.Mde_annotated import Mde_annotated
from workflows.mde.output_files.MDPE_all_significant_IDs import Mde_all_significant_IDs
from workflows.mde.output_files.MDPE_all_significant_symbols import Mde_all_significant_symbols
from workflows.mde.output_files.MDPE_all_significant_annotated import Mde_all_significant_annotated
from workflows.mde.output_files.MDPE_any_significant_IDs import Mde_any_significant_IDs
from workflows.mde.output_files.MDPE_any_significant_symbols import Mde_any_significant_symbols
from workflows.mde.output_files.MDPE_any_significant_annotated import Mde_any_significant_annotated

# statistical analysis imports
from workflows.mde.statistical_analysis_helpers.pairwise_overlap_helper import pairwise_overlap_helper
from workflows.mde.statistical_analysis_helpers.differential_expression_signature_helper import differential_expression_signature_helper

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
def run_mde_workflow(global_variables, biotype):

    print("-" * len(list(biotype)))
    print(biotype)
    print("-" * len(list(biotype)))
    print()

    # gets the config for the workflow
    config = global_variables["config"]["MDE"]

    # iterates through the des
    parsed_mde_parameters = global_variables["mde_parameters"]
    for mde_dict in parsed_mde_parameters:
        mde_ID = mde_dict["mde_ID"]
        de_IDs = mde_dict["de_IDs"]

        print(mde_ID)

        # gets the outpath for the workflow - as we use this a lot
        out_path = os.path.join(global_variables["out_path"], biotype, "mde_workflows", mde_ID)

        for element in config:

            element_name, element_active, element_type, element_subtype, element_path = element

            # checks prerequisites have been met:
            if check_element_prerequisites(element_active, element_type, element_subtype, element_path, global_variables):

                # methods for the core workflow
                if element_name == "mde_sub_directories_core" and element_type == "core":
                    core_sub_directories(global_variables, out_path)

                elif element_name == "mde_file_all_genes_IDs" and element_type == "core":
                    Mde_IDs(global_variables, out_path, biotype, de_IDs)
                elif element_name == "mde_file_genes_significant_in_any_comparison_IDs" and element_type == "core":
                    Mde_any_significant_IDs(global_variables, out_path, biotype, de_IDs)
                elif element_name == "mde_file_genes_significant_in_all_comparisons_IDs" and element_type == "core":
                    Mde_all_significant_IDs(global_variables, out_path, biotype, de_IDs)

                elif element_name == "mde_file_all_genes_symbols" and element_type == "core":
                    Mde_symbols(global_variables, out_path, biotype, de_IDs)
                elif element_name == "mde_file_genes_significant_in_any_comparison_symbols" and element_type == "core":
                    Mde_any_significant_symbols(global_variables, out_path, biotype, de_IDs)
                elif element_name == "mde_file_genes_significant_in_all_comparisons_symbols" and element_type == "core":
                    Mde_all_significant_symbols(global_variables, out_path, biotype, de_IDs)

                elif element_name == "mde_file_all_genes_annotated" and element_type == "core":
                    Mde_annotated(global_variables, out_path, biotype, de_IDs)
                elif element_name == "mde_file_genes_significant_in_any_comparison_annotated" and element_type == "core":
                    Mde_any_significant_annotated(global_variables, out_path, biotype, de_IDs)
                elif element_name == "mde_file_genes_significant_in_all_comparisons_annotated" and element_type == "core":
                    Mde_all_significant_annotated(global_variables, out_path, biotype, de_IDs)

                # methods for statistical analysis
                elif element_name == "mde_analysis_pairwise_overlap" and element_type == "statistical":
                    pairwise_overlap_helper(out_path, de_IDs)
                elif element_name == "mde_differential_expression_signature" and element_type == "statistical":
                    mde_dict = differential_expression_signature_helper(global_variables, out_path, de_IDs, mde_dict)

                # methods for the plots
                elif element_name == "mde_start_plots" and element_type == "plot_core":
                    pr_dictionary = start_plots(global_variables, out_path, "Mde", mde_dict)
                elif element_type == "plot":
                    add_plot(element_path, pr_dictionary)
                elif element_name == "mde_end_plots" and element_type == "plot_core":
                    end_plots(pr_dictionary)
                elif element_name == "mde_run_r" and element_type == "plot_core":
                    run_r(pr_dictionary, global_variables)

                # methods for the report
                elif element_name == "mde_start_report" and element_type == "report_core":
                    start_report(global_variables, pr_dictionary, element_path)
                elif element_type == "report_title":
                    add_header_section_to_report(element_path, pr_dictionary)
                elif element_type == "report_text":
                    add_text_section_to_report(element_path, pr_dictionary, global_variables)
                elif element_type == "report_plot":
                    add_plot_section_to_report(element_path, pr_dictionary, global_variables)
                elif element_name == "mde_end_report" and element_type == "report_core":
                    end_report(pr_dictionary)

                print("done with: " + element_name.replace("_", " "))

        print()


# checks that prerequisites have been met for running an elements command
def check_element_prerequisites(element_active, element_type, element_subtype, element_path, global_variables):

    if element_active == "FALSE":
        return False
    elif element_subtype == "ora" and global_variables["ora_flag"] == False:
        return False
    elif element_subtype == "ura" and global_variables["ura_flag"] == False:
        return False
    elif element_type == "plot" and element_path.upper() == "NONE":
        return False
    else:
        return True