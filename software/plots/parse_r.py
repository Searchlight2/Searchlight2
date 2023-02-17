import os.path
import sys

from misc.new_directory import new_directory



def parse_r(r_script_path,pr_dictionary):

    # opens the r-script file
    try:
        r_script_file = open(r_script_path).readlines()
    except:
        print("Error: the r-script file: " + r_script_path + " cannot be opened.", file=sys.stderr)
        sys.exit(1)

    parsed_r_script = ""
    iteration_tag_active = False

    # iterates through the r script and replaces parsing instruction tags with the appropriate strings
    for line in r_script_file:


        # detects a hypergeom gene set iteration tag
        if "<*per_ora*>" in line:
            iteration_tag_active = True
            iteration_lines_list = []

        elif "<*/per_ora*>" in line:
            iteration_tag_active = False
            for ora_type in pr_dictionary["hypergeom_gene_set_types"]:
                for line in iteration_lines_list:
                    parsed_r_script += parse_line(line.replace("<*type*>", ora_type), pr_dictionary)
            continue


        #detects an IPA ureg iteration tag
        if "<*per_ura*>" in line:
            iteration_tag_active = True
            iteration_lines_list = []

        elif "<*/per_ura*>" in line:
            iteration_tag_active = False
            for ura_type in pr_dictionary["ura_types"]:
                for line in iteration_lines_list:
                    parsed_r_script += parse_line(line.replace("<*type*>", ura_type), pr_dictionary)
            continue


        # detects a differential expression signature hypergeom gene set iteration tag
        if "<*per_de_signature_hyper_gs*>" in line:
            iteration_tag_active = True
            iteration_lines_list = []

        elif "<*/per_de_signature_hyper_gs*>" in line:
            iteration_tag_active = False
            for de_signature in pr_dictionary["de_signatures"]:
                for ora_type in pr_dictionary["hypergeom_gene_set_types"]:
                    for line in iteration_lines_list:
                        parsed_r_script += parse_line(line.replace("<*type*>", ora_type).replace("<*de_signature*>", str(de_signature)),pr_dictionary)
            continue



        # tests for an active iteration tag
        if iteration_tag_active:
            iteration_lines_list.append(line)
        else:
            parsed_r_script += parse_line(line, pr_dictionary)


    return parsed_r_script



# detects general (non iterative) tags and parses
def parse_line(line,pr_dictionary):

    # detects general tags and replaces them with the appropriate string
    if "<*comparisons_list*>" in line:
        line = line.replace("<*comparisons_list*>", pr_dictionary["comparisons_r_string"])
    if "<*sample_sheet_column_names_list*>" in line:
        line = line.replace("<*sample_sheet_column_names_list*>", pr_dictionary["sample_sheet_column_names_r_string"])
    if "<*sample_groups_by_SS_column_list*>" in line:
        line = line.replace("<*sample_groups_by_SS_column_list*>", pr_dictionary["sample_groups_by_SS_column_r_string"])
    if "<*sample_groupings_by_SS_column_list*>" in line:
        line = line.replace("<*sample_groupings_by_SS_column_list*>", pr_dictionary["sample_groupings_by_SS_column_r_string"])
    if "<*samples_list*>" in line:
        line = line.replace("<*samples_list*>", pr_dictionary["samples_r_string"])
    if "<*sample_group_list*>" in line:
        line = line.replace("<*sample_group_list*>", pr_dictionary["sample_groups_r_string"])
    if "<*sample_groupings_list*>" in line:
        line = line.replace("<*sample_groupings_list*>", pr_dictionary["sample_groupings_r_string"])
    if "<*samples_by_sample_group_list*>" in line:
        line = line.replace("<*samples_by_sample_group_list*>", pr_dictionary["samples_by_sample_group_r_string"])
    if "<*default_sample_colours_list*>" in line:
        line = line.replace("<*default_sample_colours_list*>", pr_dictionary["default_samples_colours_r_string"])
    if "<*default_sample_colours_by_SS_column_list*>" in line:
        line = line.replace("<*default_sample_colours_by_SS_column_list*>", pr_dictionary["default_sample_colours_by_SS_column_r_string"])
    if "<*default_sample_group_colours_by_SS_column_list*>" in line:
        line = line.replace("<*default_sample_group_colours_by_SS_column_list*>", pr_dictionary["default_sample_group_colours_by_SS_column_r_string"])
    if "<*working_directory*>" in line:
        line = line.replace("<*working_directory*>", pr_dictionary["workflow_outpath"])
    if "<*per_ora*>" in line:
        line = ""
    if "<*/per_ora*>" in line:
        line = ""
    if "<*per_ura*>" in line:
        line = ""
    if "<*/per_ura*>" in line:
        line = ""
    if "<*per_de_signature_hyper_gs*>" in line:
        line = ""
    if "<*/per_de_signature_hyper_gs*>" in line:
        line = ""

    # detects a path tag and converts to os friendly version, and makes a new folder.
    if "<*path*>" in line and "<*/path*>" in line:
        path = line.split("<*path*>")[1].split("<*/path*>")[0]
        parsed_path = os.path.join(*path.split("/"))
        line = line.replace("<*path*>" + path + "<*/path*>", parsed_path)
        new_directory(os.path.join(pr_dictionary["workflow_outpath"], os.path.join(*path.split("/")[0:-1])))

    return line
