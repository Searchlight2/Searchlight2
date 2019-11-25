import os


def start_report(global_variables, pr_dictionary, config_element_path):

    # sets up the bin/HTML path
    pr_dictionary["html_bin_path"] = os.path.join(global_variables["SL_path"], "bin", "report")

    # parsing the html title (shown in the browser, not file name)
    report_title = pr_dictionary["workflow_ID"]

    # read and write meta data to pr_dictionary
    pr_dictionary["meta_data"] = open(pr_dictionary["html_bin_path"] + "/meta.html", "r").read().replace("<title>Searchlight 2</title>", "<title>"+report_title+"</title>")

    # read and write the report header to pr_dictionary
    pr_dictionary["report_header"] = open(pr_dictionary["html_bin_path"] + "/report_header.html", "r").read()

    # initializing the side bar
    logo_path = os.path.join("plots", "logo.png")
    pr_dictionary["side_bar"] = "<li><a href=""#tp""><img src=" + logo_path + " style=""width:100%;""></a></li>"

    # initializing report_body, the plot section are appended in the add_report.py class
    pr_dictionary["report_body"] = ""
