import os

# directory imports
from sub_directories.core_sub_directories import core_sub_directories

# output file imports
from output_files.gene_IDs import gene_IDs
from output_files.gene_IDs_upregulated import gene_IDs_upregulated
from output_files.gene_IDs_downregulated import gene_IDs_downregulated
from output_files.gene_IDs_significant import gene_IDs_significant
from output_files.gene_IDs_significant_upregulated import gene_IDs_significant_upregulated
from output_files.gene_IDs_significant_downregulated import gene_IDs_significant_downregulated

from output_files.gene_symbols import gene_symbols
from output_files.gene_symbols_upregulated import gene_symbols_upregulated
from output_files.gene_symbols_downregulated import gene_symbols_downregulated
from output_files.gene_symbols_significant import gene_symbols_significant
from output_files.gene_symbols_significant_upregulated import gene_symbols_significant_upregulated
from output_files.gene_symbols_significant_downregulated import gene_symbols_significant_downregulated

from output_files.PDE_annotated import PDE_annotated
from output_files.PDE_annotated_downregulated import PDE_annotated_downregulated
from output_files.PDE_annotated_significant import PDE_annotated_significant
from output_files.PDE_annotated_significant_downregulated import PDE_annotated_significant_downregulated
from output_files.PDE_annotated_significant_upregulated import PDE_annotated_significant_upregulated
from output_files.PDE_annotated_upregulated import PDE_annotated_upregulated

# statistical analysis imports
from statistical_analysis_helpers.hyerpgeometric_gene_set_helper import hypergeometric_gene_set_helper
from statistical_analysis_helpers.ipa_ureg_helper import ipa_ureg_helper
from statistical_analysis_helpers.spatial_enrichment_helper import spatial_enrichment_helper

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
def run_pde_workflow(global_variables, biotype):

    print "-" * len(list(biotype))
    print biotype
    print "-" * len(list(biotype))
    print

    # gets the config for the workflow
    config = global_variables["config"]["PDE"]

    # iterates through the PDEs
    parsed_pde_parameters = global_variables["pde_parameters"]
    for pde_parameter_dict in parsed_pde_parameters:
        pde_ID = pde_parameter_dict["pde_ID"]
        print pde_ID
        pde_ID_no_spaces = pde_ID.replace(" ", "_")

        # gets the outpath for the workflow - as we use this a lot
        out_path = os.path.join(global_variables["out_path"], biotype, "pde_workflows", pde_ID_no_spaces)

        # iterates through the elements in the config
        for element in config:

            element_name, element_active, element_type, element_subtype, element_path = element

            # checks prerequisites have been met:
            if check_element_prerequisites(element_active, element_type, element_subtype, element_path, global_variables):

                # methods for the core workflow
                if element_name == "pde_sub_directories_core" and element_type == "core":
                    core_sub_directories(global_variables, out_path)

                elif element_name == "pde_file_gene_IDs" and element_type == "core":
                    gene_IDs(global_variables, out_path, biotype, pde_ID)
                elif element_name == "pde_file_gene_IDs_upregulated" and element_type == "core":
                    gene_IDs_upregulated(global_variables, out_path, biotype, pde_ID)
                elif element_name == "pde_file_gene_IDs_downregulated" and element_type == "core":
                    gene_IDs_downregulated(global_variables, out_path, biotype, pde_ID)
                elif element_name == "pde_file_gene_IDs_significant" and element_type == "core":
                    gene_IDs_significant(global_variables, out_path, biotype, pde_ID)
                elif element_name == "pde_file_gene_IDs_significant_upregulated" and element_type == "core":
                    gene_IDs_significant_upregulated(global_variables, out_path, biotype, pde_ID)
                elif element_name == "pde_file_gene_IDs_significant_downregulated" and element_type == "core":
                    gene_IDs_significant_downregulated(global_variables, out_path, biotype, pde_ID)

                elif element_name == "pde_file_gene_symbols" and element_type == "core":
                    gene_symbols(global_variables, out_path, biotype, pde_ID)
                elif element_name == "pde_file_gene_symbols_upregulated" and element_type == "core":
                    gene_symbols_upregulated(global_variables, out_path, biotype, pde_ID)
                elif element_name == "pde_file_gene_symbols_downregulated" and element_type == "core":
                    gene_symbols_downregulated(global_variables, out_path, biotype, pde_ID)
                elif element_name == "pde_file_gene_symbols_significant" and element_type == "core":
                    gene_symbols_significant(global_variables, out_path, biotype, pde_ID)
                elif element_name == "pde_file_gene_symbols_significant_upregulated" and element_type == "core":
                    gene_symbols_significant_upregulated(global_variables, out_path, biotype, pde_ID)
                elif element_name == "pde_file_gene_symbols_significant_downregulated" and element_type == "core":
                    gene_symbols_significant_downregulated(global_variables, out_path, biotype, pde_ID)

                elif element_name == "pde_file_annotated" and element_type == "core":
                    PDE_annotated(global_variables, out_path, biotype, pde_ID)
                elif element_name == "pde_file_annotated_upregulated" and element_type == "core":
                    PDE_annotated_upregulated(global_variables, out_path, biotype, pde_ID)
                elif element_name == "pde_file_annotated_downregulated" and element_type == "core":
                    PDE_annotated_downregulated(global_variables, out_path, biotype, pde_ID)
                elif element_name == "pde_file_annotated_significant" and element_type == "core":
                    PDE_annotated_significant(global_variables, out_path, biotype, pde_ID)
                elif element_name == "pde_file_annotated_significant_upregulated" and element_type == "core":
                    PDE_annotated_significant_upregulated(global_variables, out_path, biotype, pde_ID)
                elif element_name == "pde_file_annotated_significant_downregulated" and element_type == "core":
                    PDE_annotated_significant_downregulated(global_variables, out_path, biotype, pde_ID)

                # methods for statistical analysis
                elif element_name == "pde_analysis_spatial" and element_type == "statistical":
                    spatial_enrichment_helper(global_variables, out_path, pde_parameter_dict)
                elif element_name == "pde_analysis_hypergeometric_gene_sets" and element_type == "statistical":
                    hypergeometric_gene_set_helper(out_path, global_variables)
                elif element_name == "pde_analysis_ipa_upstream_regulators" and element_type == "statistical":
                    ipa_ureg_helper(out_path, global_variables)

                # methods for the plots
                elif element_name == "pde_start_plots" and element_type == "plot_core":
                    pr_dictionary = start_plots(global_variables, out_path, "PDE", pde_parameter_dict)
                elif element_type == "plot":
                    add_plot(element_path, pr_dictionary)
                elif element_name == "pde_end_plots" and element_type == "plot_core":
                    end_plots(pr_dictionary)
                elif element_name == "pde_run_r" and element_type == "plot_core":
                    run_r(pr_dictionary)

                # methods for the report
                elif element_name == "pde_start_report" and element_type == "report_core":
                    start_report(global_variables, pr_dictionary, element_path)
                elif element_type == "report_title":
                    add_header_section_to_report(element_path, pr_dictionary)
                elif element_type == "report_text":
                    add_text_section_to_report(element_path, pr_dictionary, global_variables)
                elif element_type == "report_plot":
                    add_plot_section_to_report(element_path, pr_dictionary, global_variables)
                elif element_name == "pde_end_report" and element_type == "report_core":
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
