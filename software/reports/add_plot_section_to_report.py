import os, sys
from .parse_text_section import parse_text_section


def add_plot_section_to_report(config_element_path, pr_dictionary, global_variables):
    pr_dictionary["plot_width"] = 80

    # gets the html elements list path from the config element:
    html_elements_list_path = os.path.join(pr_dictionary["element_bin_path"], os.path.join(*config_element_path.split("/")))
    pr_dictionary["subsections"] = html_elements_list_path.split("/")[-1].split(".")[0]

    # read the html elements list file
    try:
        html_elements_list = open(html_elements_list_path).readlines()
    except:
        print("Error: the html elements list: " + html_elements_list_path + " cannot be opened.", file=sys.stderr)
        sys.exit(1)

    # get the default html structure, this file will be parsed and appended to the report body
    try:
        default_html = open(pr_dictionary["html_bin_path"] + "/default_section.html").read()
    except:
        print("Error: the default html section cannot be open", file=sys.stderr)
        sys.exit(1)


    iteration_tag_active = False
    iteration_lines_list = []
    parsed_elements_list = ""
    pr_dictionary["plots"] = ""
    parsed_html = ""


    # reads the element list line by line
    for line in html_elements_list:

        # detects a sample group iteration tag
        if "<*per_sample_group*>" in line:
            iteration_tag_active = True
            iteration_lines_list = []

        elif "<*/per_sample_group*>" in line:
            iteration_tag_active = False
            for samples_group in pr_dictionary["order_list"]:
                for line in iteration_lines_list:
                    parsed_elements_list += str(parse_lines(line.replace("<*sample*>", samples_group), default_html, pr_dictionary, global_variables))
            continue

        # detects a sample iteration tag
        if "<*per_sample*>" in line:
            iteration_tag_active = True
            iteration_lines_list = []

        elif "<*/per_sample*>" in line:
            iteration_tag_active = False
            for samples in pr_dictionary["samples_ordered"]:
                for line in iteration_lines_list:
                    parsed_elements_list += str(
                        parse_lines(line.replace("<*sample*>", samples), default_html, pr_dictionary, global_variables))
            continue

        # detects an ipa ureg iteration tag
        if "<*per_ura*>" in line:
            iteration_tag_active = True
            iteration_lines_list = []

        elif "<*/per_ura*>" in line:
            iteration_tag_active = False
            for ura in pr_dictionary["ura_types"]:
                for line in iteration_lines_list:
                    parsed_elements_list += str(
                        parse_lines(line.replace("<*ura_type*>", ura), default_html, pr_dictionary, global_variables))
            continue

        # detects a hypergeom gene set iteration tag
        if "<*per_hypergeom_gene_set*>" in line:
            iteration_tag_active = True
            iteration_lines_list = []

        elif "<*/per_hypergeom_gene_set*>" in line:
            iteration_tag_active = False
            for ora_type in pr_dictionary["hypergeom_gene_set_types"]:
                for line in iteration_lines_list:
                    parsed_elements_list += str(
                        parse_lines(line.replace("<*hypergeom_type*>", ora_type), default_html, pr_dictionary, global_variables))
            continue

        # detects a sample sheet column iteration tag
        if "<*per_ss_column*>" in line:
            iteration_tag_active = True
            iteration_lines_list = []

        elif "<*/per_ss_column*>" in line:
            iteration_tag_active = False
            for ss_column_type in pr_dictionary["sample_sheet_column_names"]:
                for line in iteration_lines_list:
                    parsed_elements_list += str(
                        parse_lines(line.replace("<*ss_column_name*>", ss_column_type), default_html, pr_dictionary, global_variables))
            continue

        # detects a comparison iteration tag
        if "<*per_mde_comparison*>" in line:
            iteration_tag_active = True
            iteration_lines_list = []

        elif "<*/per_mde_comparison*>" in line:
            iteration_tag_active = False
            comparisons = pr_dictionary["comparisons"]

            for index1 in range(0, len(comparisons)-1):
                for index2 in range(index1+1, len(comparisons)):
                    mde_comparison = (comparisons[index1] + "_VS_" + comparisons[index2]).replace(" vs ", "_vs_")
                    mde_comparison_text = mde_comparison.replace("_VS_", "  VS  ").replace("_vs_", " vs ")
                    for line in iteration_lines_list:
                        parsed_elements_list += str(parse_lines(line.replace("<*mde_comparison*>", mde_comparison).replace("<*mde_comparison_text*>", mde_comparison_text), default_html,pr_dictionary, global_variables))
            continue

        # detects a chromosome iteration tag
        if "<*per_chromosome*>" in line:
            iteration_tag_active = True
            iteration_lines_list = []

        elif "<*/per_chromosome*>" in line:
            iteration_tag_active = False
            for chromosome in pr_dictionary["chromosome_list"]:
                for line in iteration_lines_list:
                    parsed_elements_list += str(parse_lines(line.replace("<*chromosome*>", chromosome), default_html, pr_dictionary,global_variables))
            continue

        # detects a differential expression signature iteration tag
        if "<*per_de_signature*>" in line:
            iteration_tag_active = True
            iteration_lines_list = []

        elif "<*/per_de_signature*>" in line:
            iteration_tag_active = False
            for de_signature in pr_dictionary["de_signatures"]:
                for line in iteration_lines_list:
                    parsed_elements_list += str(parse_lines(line.replace("<*de_signature*>", str(de_signature)), default_html, pr_dictionary, global_variables))
            continue

        # detects a differential expression signature hypergeom gene set iteration tag
        if "<*per_de_signature_hypergeom_gene_set*>" in line:
            iteration_tag_active = True
            iteration_lines_list = []

        elif "<*/per_de_signature_hypergeom_gene_set*>" in line:
            iteration_tag_active = False
            for de_signature in pr_dictionary["de_signatures"]:
                for ora_type in pr_dictionary["hypergeom_gene_set_types"]:
                    for line in iteration_lines_list:
                        parsed_elements_list += str(parse_lines(line.replace("<*de_signature*>", str(de_signature)).replace("<*type*>", ora_type), default_html, pr_dictionary, global_variables))
            continue

        # tests for an active iteration tag
        if iteration_tag_active:
            iteration_lines_list.append(line)
        else:
            parsed_lines, b, c = parse_lines(line, default_html, pr_dictionary, global_variables)
            parsed_elements_list += parsed_lines
            default_html = b
            pr_dictionary = c

    parsed_html += default_html.replace("<*plots*>", pr_dictionary["plots"])
    pr_dictionary["report_body"] += parsed_html


def parse_lines(line, html_default, pr_dictionary, global_variables):

    # detects general tags and replaces them with the appropriate string
    if "<*per_hypergeom_gene_set*>" in line:
        line = line.replace("<*per_hypergeom_gene_set*>", "")
    if "<*/per_hypergeom_gene_set*>" in line:
        line = line.replace("<*/per_hypergeom_gene_set*>", "")
    if "<*per_ura*>" in line:
        line = line.replace("<*per_ura*>", "")
    if "<*/per_ura*>" in line:
        line = line.replace("<*/per_ura*>", "")

    if line.split("=")[0] == "TITLE":
        plot_id = line.split("=")[1].replace(" ", "_").replace("\n", "")
        plot_title = line.split("=")[1]
        html_default = html_default.replace("<*plot_id*>", plot_id).replace("<*plot_title*>", plot_title)
        pr_dictionary["side_bar"] += "<li><a href=\"#" + plot_id + "\">" + plot_title + "</a></li>\n"

    if line.split("=")[0] == "SUB_TITLE":
        line = "<h4>" + line.split("=")[1] + "</h4>"
        pr_dictionary["plots"] += line

    if line.split("=")[0] == "PLOTS_PER_ROW":
        ppr = line.split("=")[1]
        pr_dictionary["plot_width"] = (1.0 / int(ppr)) * 100

    if line.split("=")[0] == "PLOT_PATH":
        line = "<img style=\"width:" + str(pr_dictionary["plot_width"]) + "%;\" src=\"" + line.split("=")[1] + "\"/>"
        pr_dictionary["plots"] += line

    if line.split("=")[0] == "R_CODE_PATH":
        r_path = os.path.join(pr_dictionary["workflow_outpath"], line.split("=")[1].replace("\n", ""))
        pr_dictionary["r_script"] = open(r_path, "r").read()
        pr_dictionary["r_script"] = pr_dictionary["r_script"].replace("\n", "<br>").replace("  ", " &emsp;").replace(
            "##--", "<span class=\"r_comment\">##--").replace("--##", "--##</span>")
        html_default = html_default.replace("<*path_to_r_script*>", pr_dictionary["r_script"])

    if line.split("=")[0] == "PLOT_DESCRIPTION":
        line = os.path.join(global_variables["SL_path"] + line.rstrip().split("=")[1])
        plot_description = open(line, "r").read()
        if plot_description == "":
            html_default = html_default.replace("<*plot_description*>", "warning: empty plot description")
        else:
            plot_description = parse_text_section(plot_description, pr_dictionary)
            html_default = html_default.replace("<*plot_description*>", plot_description)

    if line.split("=")[0] == "PLOT_LEGEND":
        line = os.path.join(global_variables["SL_path"] + line.rstrip().split("=")[1])
        plot_legend = open(line, "r").read()
        if plot_legend == "":
            html_default = html_default.replace("<*plot_legend*>", "warning: empty plot legend")
        else:
            plot_legend = parse_text_section(plot_legend, pr_dictionary)
            html_default = html_default.replace("<*plot_legend*>", plot_legend)

    return line, html_default, pr_dictionary
