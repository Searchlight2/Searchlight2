import sys, os
from parse_text_section import parse_text_section

def string_to_title(line):
    parsed_line = []
    line_split = line.split(" ")
    for word in line_split:
        word_split = list(word)
        word_split[0] = word_split[0].upper()
        parsed_line.append("".join(word_split))

    return " ".join(parsed_line)


def add_text_section_to_report(config_element_path, pr_dictionary, global_variables):

    # opens the text file
    try:
        text_path = os.path.join(pr_dictionary["html_bin_path"], config_element_path)
        text = open(text_path).read()

    except:
        print >> sys.stderr, "Error: the html elements list: " + config_element_path + " cannot be opened."
        sys.exit(1)

    # parses the text
    text = parse_text_section(text, pr_dictionary)

    # append element to side bar
    side_bar_name = string_to_title(config_element_path.split("/")[-1].split(".")[0].replace("_", " "))
    pr_dictionary["side_bar"] += "<li><a href=#"+side_bar_name+">" + side_bar_name + "</a></li>"

    # append element to report
    pr_dictionary["report_body"] += "<div class=text id=" + side_bar_name + "><h2>" + side_bar_name + "</h2><div>" + text + "</div></div>"

