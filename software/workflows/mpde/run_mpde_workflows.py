import os

# core workflow imports
from sub_directories.core_sub_directories import core_sub_directories
from output_files.MDPE_IDs import MPDE_IDs
from output_files.MPDE_symbols import MPDE_symbols
from output_files.MPDE_annotated import MPDE_annotated
from output_files.MDPE_all_significant_IDs import MPDE_all_significant_IDs
from output_files.MDPE_all_significant_symbols import MPDE_all_significant_symbols
from output_files.MDPE_all_significant_annotated import MPDE_all_significant_annotated
from output_files.MDPE_any_significant_IDs import MPDE_any_significant_IDs
from output_files.MDPE_any_significant_symbols import MPDE_any_significant_symbols
from output_files.MDPE_any_significant_annotated import MPDE_any_significant_annotated

# statistical analysis imports
from statistical_analysis_helpers.pairwise_overlap_helper import pairwise_overlap_helper
from statistical_analysis_helpers.differential_expression_signature_helper import differential_expression_signature_helper

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
def run_mpde_workflow(global_variables, biotype):

    print "-" * len(list(biotype))
    print biotype
    print "-" * len(list(biotype))
    print

    # gets the config for the workflow
    config = global_variables["config"]["MPDE"]

    # iterates through the PDEs
    parsed_mpde_parameters = global_variables["mpde_parameters"]
    for mpde_dict in parsed_mpde_parameters:
        mpde_ID = mpde_dict["mpde_ID"]
        pde_IDs = mpde_dict["pde_IDs"]

        print mpde_ID

        # gets the outpath for the workflow - as we use this a lot
        out_path = os.path.join(global_variables["out_path"], biotype, "mpde_workflows", mpde_ID)

        for element in config:

            element_name, element_active, element_type, element_subtype, element_path = element

            # checks prerequisites have been met:
            if check_element_prerequisites(element_active, element_type, element_subtype, element_path, global_variables):

                # methods for the core workflow
                if element_name == "mpde_sub_directories_core" and element_type == "core":
                    core_sub_directories(global_variables, out_path)

                elif element_name == "mpde_file_all_genes_IDs" and element_type == "core":
                    MPDE_IDs(global_variables, out_path, biotype, pde_IDs)
                elif element_name == "mpde_file_genes_significant_in_any_comparison_IDs" and element_type == "core":
                    MPDE_any_significant_IDs(global_variables, out_path, biotype, pde_IDs)
                elif element_name == "mpde_file_genes_significant_in_all_comparisons_IDs" and element_type == "core":
                    MPDE_all_significant_IDs(global_variables, out_path, biotype, pde_IDs)

                elif element_name == "mpde_file_all_genes_symbols" and element_type == "core":
                    MPDE_symbols(global_variables, out_path, biotype, pde_IDs)
                elif element_name == "mpde_file_genes_significant_in_any_comparison_symbols" and element_type == "core":
                    MPDE_any_significant_symbols(global_variables, out_path, biotype, pde_IDs)
                elif element_name == "mpde_file_genes_significant_in_all_comparisons_symbols" and element_type == "core":
                    MPDE_all_significant_symbols(global_variables, out_path, biotype, pde_IDs)

                elif element_name == "mpde_file_all_genes_annotated" and element_type == "core":
                    MPDE_annotated(global_variables, out_path, biotype, pde_IDs)
                elif element_name == "mpde_file_genes_significant_in_any_comparison_annotated" and element_type == "core":
                    MPDE_any_significant_annotated(global_variables, out_path, biotype, pde_IDs)
                elif element_name == "mpde_file_genes_significant_in_all_comparisons_annotated" and element_type == "core":
                    MPDE_all_significant_annotated(global_variables, out_path, biotype, pde_IDs)

                # methods for statistical analysis
                elif element_name == "mpde_analysis_pairwise_overlap" and element_type == "statistical":
                    pairwise_overlap_helper(out_path, pde_IDs)
                elif element_name == "mpde_differential_expression_signature" and element_type == "statistical":
                    mpde_dict = differential_expression_signature_helper(global_variables, out_path, pde_IDs, mpde_dict)

                # methods for the plots
                elif element_name == "mpde_start_plots" and element_type == "plot_core":
                    pr_dictionary = start_plots(global_variables, out_path, "MPDE", mpde_dict)
                elif element_type == "plot":
                    add_plot(element_path, pr_dictionary)
                elif element_name == "mpde_end_plots" and element_type == "plot_core":
                    end_plots(pr_dictionary)
                elif element_name == "mpde_run_r" and element_type == "plot_core":
                    run_r(pr_dictionary)

                # methods for the report
                elif element_name == "mpde_start_report" and element_type == "report_core":
                    start_report(global_variables, pr_dictionary, element_path)
                elif element_type == "report_title":
                    add_header_section_to_report(element_path, pr_dictionary)
                elif element_type == "report_text":
                    add_text_section_to_report(element_path, pr_dictionary, global_variables)
                elif element_type == "report_plot":
                    add_plot_section_to_report(element_path, pr_dictionary, global_variables)
                elif element_name == "mpde_end_report" and element_type == "report_core":
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