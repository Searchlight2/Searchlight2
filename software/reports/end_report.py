import shutil
import os


def end_report(pr_dictionary):

    # copy sl logo to report folder
    shutil.copy(os.path.join(pr_dictionary["html_bin_path"], "logo.png"), os.path.join(pr_dictionary["workflow_outpath"],"plots"))

    # initialize a new report file
    report = open(pr_dictionary["workflow_outpath"] + "/report.html", "w")

    # replace the section tags in report_meta_data by the content generated in add_report.py
    report_out = pr_dictionary["meta_data"].replace("<*side_bar*>", pr_dictionary["side_bar"])\
        .replace("<*report_body*>", str(pr_dictionary["report_body"])).replace("<*report_header*>", pr_dictionary["report_header"])

    # write to file
    report.write(report_out)
