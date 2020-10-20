import os


from misc.get_chromosome_list import get_chromosome_list
from misc.get_r_string_sample_groups_by_SS_column import get_r_string_sample_groups_by_SS_column
from misc.get_r_string_default_samples_colours_by_SS_column import get_r_string_default_samples_colours_by_SS_column
from misc.get_r_string_sample_groupings_by_SS_column import get_r_string_sample_groupings_by_SS_column
from misc.get_r_string_default_sample_group_colours_by_SS_column import get_r_string_default_sample_group_colours_by_SS_column
from misc.get_samples_ordered_by_order_list import get_samples_ordered_by_order_list
from misc.get_r_string_samples import get_r_string_samples
from misc.get_r_string_sample_groups import get_r_string_sample_groups
from misc.get_r_string_sample_groupings import get_r_string_sample_groupings
from misc.get_r_string_samples_by_sample_group import get_r_string_samples_by_sample_group
from misc.get_r_string_default_sample_colours import get_r_string_default_sample_colours



# sets up the r plots dictionary
def start_plots(global_variables, outpath, workflow_type,workflow_parameter_dict):

    # instantiates the r dictionary
    pr_dictionary = {}

    # sets up the working directory
    pr_dictionary["workflow_outpath"] = outpath

    # sets up the bin/elements path
    pr_dictionary["element_bin_path"] = os.path.join(global_variables["SL_path"], "bin", "element_list")

    # sets up the bin/r path
    pr_dictionary["r_bin_path"] = os.path.join(global_variables["SL_path"], "bin", "r")

    # adds the version
    pr_dictionary["version"] = global_variables["version"]

    # adds the core input file paths for the report methods:
    pr_dictionary["ne_file_path"] = global_variables["ne_file_path"]
    pr_dictionary["background_file_path"] = global_variables["background_file_path"]

    # adds the core input processing statistics for the report methods:
    pr_dictionary["expression_set_size"] = global_variables["expression_set_size"]

    # sets up the workflow r code subsections
    pr_dictionary = add_subsection_r(os.path.join(pr_dictionary["r_bin_path"],"section_header", "searchlight_2.txt"),"subsection_r_title", "section_header/searchlight_2.txt",pr_dictionary)
    pr_dictionary = add_subsection_r(os.path.join(pr_dictionary["r_bin_path"],"section_header", "library.txt"),"subsection_r_library","section_header/library.txt",pr_dictionary)
    pr_dictionary = add_subsection_r(os.path.join(pr_dictionary["r_bin_path"],"section_header", "core_parameter.txt"),"subsection_r_core_parameter","section_header/core_parameter.txt",pr_dictionary)
    pr_dictionary = add_subsection_r(os.path.join(pr_dictionary["r_bin_path"],"section_header", "input_file.txt"),"subsection_r_input_file","section_header/input_file.txt",pr_dictionary)
    pr_dictionary = add_subsection_r(os.path.join(pr_dictionary["r_bin_path"],"section_header", "parse_data.txt"),"subsection_r_parse_data","section_header/parse_data.txt",pr_dictionary)
    pr_dictionary = add_subsection_r(os.path.join(pr_dictionary["r_bin_path"],"section_header", "helper_function.txt"),"subsection_r_helper_function","section_header/helper_function.txt",pr_dictionary)
    pr_dictionary = add_subsection_r(os.path.join(pr_dictionary["r_bin_path"],"section_header", "plot_function.txt"),"subsection_r_plot_function","section_header/plot_function.txt",pr_dictionary)
    pr_dictionary = add_subsection_r(os.path.join(pr_dictionary["r_bin_path"],"section_header", "default_aesthetic.txt"),"subsection_r_default_aesthetic","section_header/default_aesthetic.txt",pr_dictionary)
    pr_dictionary = add_subsection_r(os.path.join(pr_dictionary["r_bin_path"],"section_header", "plot.txt"),"subsection_r_plot","section_header/plot.txt",pr_dictionary)

    # sets up the individual plot r code list
    pr_dictionary["individual_plot_r_code_list"] = []

    # sets up the workflow specific parameters
    if workflow_type == "ne":
        add_ne_specific_parameters(global_variables, pr_dictionary)
    elif workflow_type == "de":
        add_de_specific_parameters(global_variables, pr_dictionary, workflow_parameter_dict)
    elif workflow_type == "Mde":
        add_Mde_specific_parameters(global_variables, pr_dictionary, workflow_parameter_dict)

    return pr_dictionary


# adds a new global r code subsection
def add_subsection_r(path,subsection_key, r_script_tag, pr_dictionary):

    # parses the header file
    parsed_r_script = ""
    header_file = open(path).readlines()
    for line in header_file:
        parsed_r_script += line

    # adds the subsection
    subsection_r_scripts_list =  []
    subsection_r_elements_dictionary = {}

    subsection_r_scripts_list.append(parsed_r_script)
    subsection_r_elements_dictionary[r_script_tag] = True
    subsection_r_information = [subsection_r_scripts_list,subsection_r_elements_dictionary]
    pr_dictionary[subsection_key] = subsection_r_information

    return pr_dictionary


# adds ne specific parameters
def add_ne_specific_parameters(global_variables, pr_dictionary):

    pr_dictionary = add_subsection_r(os.path.join(pr_dictionary["r_bin_path"], "section_header", "ne_workflow.txt"),"subsection_r_workflow_type", "section_header/ne_workflow.txt", pr_dictionary)

    # gets the various samples and sample group lists for ne:
    order_list = global_variables["sample_groups_default_order"]
    sample_groups_by_column = global_variables["sample_groups_by_column"]
    samples_by_sample_groups = global_variables["samples_by_sample_groups"]
    sample_sheet_column_names = global_variables["sample_sheet_column_names"]
    samples_ordered = get_samples_ordered_by_order_list(order_list[0:len(sample_groups_by_column[0])], samples_by_sample_groups)

    # gets the various R code strings:
    samples_r_string = "c(\"" + "\",\"".join(samples_ordered) + "\")"
    sample_groups_r_string = "c(\"" + "\",\"".join(order_list) + "\")"
    sample_groupings_r_string = get_r_string_sample_groupings(order_list, samples_by_sample_groups)
    samples_by_sample_group_r_string = get_r_string_samples_by_sample_group(order_list,samples_by_sample_groups)
    sample_groups_by_SS_column_r_string = get_r_string_sample_groups_by_SS_column(order_list,sample_groups_by_column)
    sample_groupings_by_SS_column_r_string = get_r_string_sample_groupings_by_SS_column(order_list, sample_groups_by_column, samples_by_sample_groups)
    default_samples_colours_by_SS_column_r_string = get_r_string_default_samples_colours_by_SS_column(samples_by_sample_groups,order_list,sample_groups_by_column)
    default_sample_group_colours_by_SS_column_r_string = get_r_string_default_sample_group_colours_by_SS_column(samples_by_sample_groups,order_list,sample_groups_by_column)
    sample_sheet_column_names_r_string = "c(\"" + "\",\"".join(sample_sheet_column_names) + "\")"

    # updates the pr dictionary
    pr_dictionary["workflow_ID"] = "Normalised Expression"
    pr_dictionary["sample_sheet_column_names"] = sample_sheet_column_names
    pr_dictionary["order_list"] = order_list
    pr_dictionary["samples_ordered"] = samples_ordered
    pr_dictionary["samples_r_string"] = samples_r_string
    pr_dictionary["sample_groups_r_string"] = sample_groups_r_string
    pr_dictionary["sample_groupings_r_string"] = sample_groupings_r_string
    pr_dictionary["samples_by_sample_group_r_string"] = samples_by_sample_group_r_string
    pr_dictionary["sample_groups_by_SS_column_r_string"] = sample_groups_by_SS_column_r_string
    pr_dictionary["sample_groupings_by_SS_column_r_string"] = sample_groupings_by_SS_column_r_string
    pr_dictionary["default_sample_colours_by_SS_column_r_string"] = default_samples_colours_by_SS_column_r_string
    pr_dictionary["default_sample_group_colours_by_SS_column_r_string"] = default_sample_group_colours_by_SS_column_r_string
    pr_dictionary["sample_sheet_column_names_r_string"] = sample_sheet_column_names_r_string


    return pr_dictionary


# adds de specific parameters
def add_de_specific_parameters(global_variables, pr_dictionary, workflow_parameter_dict):


    # adds the r subsection workflow type
    pr_dictionary = add_subsection_r(os.path.join(pr_dictionary["r_bin_path"], "section_header", "de_workflow.txt"),"subsection_r_workflow_type", "section_header/de_workflow.txt", pr_dictionary)


    # gets the various samples and sample group lists for de:
    order_list = workflow_parameter_dict["order_list"]
    samples_by_sample_groups = global_variables["samples_by_sample_groups"]
    samples_ordered = get_samples_ordered_by_order_list(order_list, samples_by_sample_groups)

    # gets the various R code strings:
    samples_r_string = get_r_string_samples(samples_ordered)
    sample_groups_r_string = get_r_string_sample_groups(order_list)
    sample_groupings_r_string = get_r_string_sample_groupings(order_list, samples_by_sample_groups)
    samples_by_sample_group_r_string = get_r_string_samples_by_sample_group(order_list,samples_by_sample_groups)
    default_samples_colours_r_string = get_r_string_default_sample_colours(order_list, samples_by_sample_groups)
    comparisons_r_string = "c(\"" +  workflow_parameter_dict["de_ID"] + "\")"

    # gets the list of chromosomes
    chromosomes_list = get_chromosome_list(os.path.join(pr_dictionary["workflow_outpath"],"data","de_annotated.csv"))

    # updates the pr_dictionary
    pr_dictionary["workflow_ID"] = workflow_parameter_dict["de_ID"]
    pr_dictionary["de_p_threshold"] = workflow_parameter_dict["p_threshold"]
    pr_dictionary["de_fold_threshold"] = workflow_parameter_dict["fold_threshold"]
    pr_dictionary["de_numerator_group"] = workflow_parameter_dict["numerator_group"]
    pr_dictionary["de_denominator_group"] = workflow_parameter_dict["denominator_group"]
    pr_dictionary["de_file_path"] = workflow_parameter_dict["de_file_path"]
    pr_dictionary["differential_expression_set_size"] = workflow_parameter_dict["differential_expression_set_size"]

    pr_dictionary["order_list"] = order_list
    pr_dictionary["samples_ordered"] = samples_ordered
    pr_dictionary["comparisons_r_string"] = comparisons_r_string
    pr_dictionary["samples_by_sample_groups"] = samples_by_sample_groups
    pr_dictionary["sample_groups_r_string"] = sample_groups_r_string
    pr_dictionary["samples_r_string"] = samples_r_string
    pr_dictionary["sample_groupings_r_string"] = sample_groupings_r_string
    pr_dictionary["samples_by_sample_group_r_string"] = samples_by_sample_group_r_string
    pr_dictionary["default_samples_colours_r_string"] = default_samples_colours_r_string
    pr_dictionary["chromosome_list"] = chromosomes_list


    # gets the hypergeometric gene set types
    if global_variables["ora_flag"]:
        hypergeom_gene_set_types = []
        hypergeom_gene_set_min_set_sizes = []
        hypergeom_gene_set_max_set_sizes = []
        hypergeom_gene_set_p_thresholds = []
        hypergeom_gene_set_fold_thresholds = []
        hypergeom_gene_set_network_overlap_ratios = []

        parsed_hypergeom_gene_sets_parameters = global_variables["ora_parameters"]
        for hypergeom_gene_set_parameter_dict in parsed_hypergeom_gene_sets_parameters:
            hypergeom_gene_set_types.append(hypergeom_gene_set_parameter_dict["type"])
            hypergeom_gene_set_min_set_sizes.append(hypergeom_gene_set_parameter_dict["min_set_size"])
            hypergeom_gene_set_max_set_sizes.append(hypergeom_gene_set_parameter_dict["max_set_size"])
            hypergeom_gene_set_p_thresholds.append(hypergeom_gene_set_parameter_dict["p_threshold"])
            hypergeom_gene_set_fold_thresholds.append(hypergeom_gene_set_parameter_dict["fold_threshold"])
            hypergeom_gene_set_network_overlap_ratios.append(hypergeom_gene_set_parameter_dict["network_overlap_ratio"])

        pr_dictionary["hypergeom_gene_set_types"] = hypergeom_gene_set_types
        pr_dictionary["hypergeom_gene_set_min_set_sizes"] = hypergeom_gene_set_min_set_sizes
        pr_dictionary["hypergeom_gene_set_max_set_sizes"] = hypergeom_gene_set_max_set_sizes
        pr_dictionary["hypergeom_gene_set_p_thresholds"] = hypergeom_gene_set_p_thresholds
        pr_dictionary["hypergeom_gene_set_fold_thresholds"] = hypergeom_gene_set_fold_thresholds
        pr_dictionary["hypergeom_gene_set_network_overlap_ratios"] = hypergeom_gene_set_network_overlap_ratios


    # gets the ipa ureg types
    if global_variables["ura_flag"]:
        ura_types = []
        ura_min_set_sizes = []
        ura_max_set_sizes = []
        ura_zscore_thresholds = []
        ura_p_thresholds = []
        ura_fold_thresholds = []
        ura_overlap_ratios = []

        parsed_ura_parameters = global_variables["ura_parameters"]
        for ura_parameters_dict in parsed_ura_parameters:
            ura_types.append(ura_parameters_dict["type"])
            ura_min_set_sizes.append(ura_parameters_dict["min_set_size"])
            ura_max_set_sizes.append(ura_parameters_dict["max_set_size"])
            ura_zscore_thresholds.append(ura_parameters_dict["zscore_threshold"])
            ura_p_thresholds.append(ura_parameters_dict["p_threshold"])
            ura_fold_thresholds.append(ura_parameters_dict["fold_threshold"])
            ura_overlap_ratios.append(ura_parameters_dict["network_overlap_ratio"])

        pr_dictionary["ura_types"] = ura_types
        pr_dictionary["ura_min_set_sizes"] = ura_min_set_sizes
        pr_dictionary["ura_max_set_sizes"] = ura_max_set_sizes
        pr_dictionary["ura_zscore_thresholds"] = ura_zscore_thresholds
        pr_dictionary["ura_p_thresholds"] = ura_p_thresholds
        pr_dictionary["ura_fold_thresholds"] = ura_fold_thresholds
        pr_dictionary["ura_overlap_ratios"] = ura_overlap_ratios


    return pr_dictionary


# adds Mde specific parameters
def add_Mde_specific_parameters(global_variables, pr_dictionary, workflow_parameter_dict):

    pr_dictionary = add_subsection_r(os.path.join(pr_dictionary["r_bin_path"], "section_header", "mde_workflow.txt"),"subsection_r_workflow_type", "section_header/mde_workflow.txt", pr_dictionary)

    # gets the various samples and sample group lists for Mde:
    order_list = workflow_parameter_dict["order_list"]
    samples_by_sample_groups = global_variables["samples_by_sample_groups"]
    samples_ordered = get_samples_ordered_by_order_list(order_list, samples_by_sample_groups)
    comparisons = workflow_parameter_dict["de_IDs"]

    # gets the number of signatures
    de_signatures =  workflow_parameter_dict["de_signatures"]

    # gets the various R code strings:
    samples_r_string = get_r_string_samples(samples_ordered)
    sample_groups_r_string = get_r_string_sample_groups(order_list)
    sample_groupings_r_string = get_r_string_sample_groupings(order_list, samples_by_sample_groups)
    samples_by_sample_group_r_string = get_r_string_samples_by_sample_group(order_list, samples_by_sample_groups)
    default_samples_colours_r_string = get_r_string_default_sample_colours(order_list, samples_by_sample_groups)
    comparisons_r_string = "c(\"" + "\",\"".join(comparisons) + "\")"

    # updates the pr_dictionary
    pr_dictionary["workflow_ID"] = workflow_parameter_dict["mde_ID"]
    pr_dictionary["signatures_scc"] = workflow_parameter_dict["signatures_scc"]
    pr_dictionary["order_list"] = order_list
    pr_dictionary["samples_ordered"] = samples_ordered
    pr_dictionary["comparisons"] = comparisons
    pr_dictionary["comparisons_r_string"] = comparisons_r_string
    pr_dictionary["samples_by_sample_groups"] = samples_by_sample_groups
    pr_dictionary["sample_groups_r_string"] = sample_groups_r_string
    pr_dictionary["samples_r_string"] = samples_r_string
    pr_dictionary["sample_groupings_r_string"] = sample_groupings_r_string
    pr_dictionary["samples_by_sample_group_r_string"] = samples_by_sample_group_r_string
    pr_dictionary["default_samples_colours_r_string"] = default_samples_colours_r_string
    pr_dictionary["de_signatures"] = de_signatures


    # gets the hypergeometric gene set types
    if global_variables["ora_flag"]:
        hypergeom_gene_set_types = []
        hypergeom_gene_set_min_set_sizes = []
        hypergeom_gene_set_max_set_sizes = []
        hypergeom_gene_set_p_thresholds = []
        hypergeom_gene_set_fold_thresholds = []
        hypergeom_gene_set_network_overlap_ratios = []

        parsed_hypergeom_gene_sets_parameters = global_variables["ora_parameters"]
        for hypergeom_gene_set_parameter_dict in parsed_hypergeom_gene_sets_parameters:
            hypergeom_gene_set_types.append(hypergeom_gene_set_parameter_dict["type"])
            hypergeom_gene_set_min_set_sizes.append(hypergeom_gene_set_parameter_dict["min_set_size"])
            hypergeom_gene_set_max_set_sizes.append(hypergeom_gene_set_parameter_dict["max_set_size"])
            hypergeom_gene_set_p_thresholds.append(hypergeom_gene_set_parameter_dict["p_threshold"])
            hypergeom_gene_set_fold_thresholds.append(hypergeom_gene_set_parameter_dict["fold_threshold"])
            hypergeom_gene_set_network_overlap_ratios.append(hypergeom_gene_set_parameter_dict["network_overlap_ratio"])

        pr_dictionary["hypergeom_gene_set_types"] = hypergeom_gene_set_types
        pr_dictionary["hypergeom_gene_set_min_set_sizes"] = hypergeom_gene_set_min_set_sizes
        pr_dictionary["hypergeom_gene_set_max_set_sizes"] = hypergeom_gene_set_max_set_sizes
        pr_dictionary["hypergeom_gene_set_p_thresholds"] = hypergeom_gene_set_p_thresholds
        pr_dictionary["hypergeom_gene_set_fold_thresholds"] = hypergeom_gene_set_fold_thresholds
        pr_dictionary["hypergeom_gene_set_network_overlap_ratios"] = hypergeom_gene_set_network_overlap_ratios

    return pr_dictionary







