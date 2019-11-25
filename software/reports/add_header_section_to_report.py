def add_header_section_to_report(config_element_path, pr_dictionary):

    pr_dictionary["side_bar"] += "<li class=\"side_bar_header\">" + config_element_path + "</li>"
    return pr_dictionary["side_bar"]
