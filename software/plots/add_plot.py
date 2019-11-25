import os
import sys

from plots.parse_r import parse_r


def add_plot(config_element_path,pr_dictionary):

    # gets the various paths
    workflow_outpath = pr_dictionary["workflow_outpath"]
    r_code_outpath = None

    # string to store the individual plot r-code
    individual_plot_r_code = ""


    # opens the plot element list
    plot_element_list_path = os.path.join(pr_dictionary["element_bin_path"],os.path.join(*config_element_path.split("/")))
    try:
        plot_element_list = open(plot_element_list_path).readlines()
    except:
        print >> sys.stderr, "Error: the element list at: " + plot_element_list_path + " cannot be opened."
        sys.exit(1)


    # iterates through the elements list and parses the r scripts into r code
    for plot_element in plot_element_list:
        plot_element = plot_element.rstrip()

        # checks for the  individual plot r code outpath
        if "R_CODE_OUTPATH=" in plot_element:
            r_code_outpath = os.path.join(*plot_element.split("=")[1].split("/"))

        # tests for an r element and not a blank line
        elif len(plot_element.split("/")) == 2 and plot_element != "":

            # gets the subsection key and tests that its valid:
            subsection_key = "subsection_r_" + plot_element.split("/")[0]
            if subsection_key not in pr_dictionary:
                print >> sys.stderr, "Error: The element list at: " + plot_element_list_path + " contains an element (" + plot_element + ") with an invalid path."
                sys.exit(1)

            # retrieves the existing subsection information
            subsection_r_information = pr_dictionary[subsection_key]
            subsection_r_scripts_list = subsection_r_information[0]
            subsection_r_elements_dictionary = subsection_r_information[1]

            # parses the element r-script (if it has not already previously parsed)
            plot_element_path = os.path.join(pr_dictionary["r_bin_path"],plot_element)

            if plot_element not in subsection_r_elements_dictionary:
                parsed_r_script = parse_r(plot_element_path, pr_dictionary)
                subsection_r_scripts_list.append(parsed_r_script)
                subsection_r_elements_dictionary[plot_element] = parsed_r_script
                pr_dictionary[subsection_key] = [subsection_r_scripts_list, subsection_r_elements_dictionary]
            else:
                parsed_r_script = subsection_r_elements_dictionary[plot_element]

            # updates the individual plot r code with the parsed r-script
            individual_plot_r_code += parsed_r_script


    # updates the individual plot r code list with the individual plot r-cde
    local_r_code_list = pr_dictionary["individual_plot_r_code_list"]
    local_r_code_list.append([individual_plot_r_code,r_code_outpath])


    return pr_dictionary