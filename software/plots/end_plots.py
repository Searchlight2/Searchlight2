import os

def end_plots(pr_dictionary):


    # iterates through the per plot r code, outputting the code
    individual_plot_r_code_list = pr_dictionary["individual_plot_r_code_list"]
    for individual_plot_r_code in individual_plot_r_code_list:

        # gets the path in os friendly version
        plot_r_code = individual_plot_r_code[0]
        r_code_outpath = individual_plot_r_code[1]

        #prints the plot r-code to file
        out_file = open(os.path.join(pr_dictionary["workflow_outpath"],r_code_outpath),"w")
        out_file.write(plot_r_code)


    # outputs the workflow r-code
    r_script_out_file = open(os.path.join(pr_dictionary["workflow_outpath"],"plots","workflow.r"),"w")
    r_data_out_file = os.path.join(pr_dictionary["workflow_outpath"],"plots","workflow.rdata")
    r_session_out_file = os.path.join(pr_dictionary["workflow_outpath"],"plots","workflow_session_info.txt")

    output_workflow_r_subsection(pr_dictionary["subsection_r_title"], r_script_out_file)
    output_workflow_r_subsection(pr_dictionary["subsection_r_workflow_type"], r_script_out_file)
    output_workflow_r_subsection(pr_dictionary["subsection_r_library"], r_script_out_file)
    output_workflow_r_subsection(pr_dictionary["subsection_r_core_parameter"], r_script_out_file)
    output_workflow_r_subsection(pr_dictionary["subsection_r_input_file"], r_script_out_file)
    output_workflow_r_subsection(pr_dictionary["subsection_r_parse_data"], r_script_out_file)
    output_workflow_r_subsection(pr_dictionary["subsection_r_default_aesthetic"], r_script_out_file)
    output_workflow_r_subsection(pr_dictionary["subsection_r_helper_function"], r_script_out_file)
    output_workflow_r_subsection(pr_dictionary["subsection_r_plot_function"], r_script_out_file)
    output_workflow_r_subsection(pr_dictionary["subsection_r_plot"], r_script_out_file)

    # Code to save session and image
    r_script_out_file.write("\n##---- image and session info ----##\n")
    r_script_out_file.write("save.image(\"" + str(r_data_out_file) + "\")\n")
    r_script_out_file.write("write.table(capture.output(sessionInfo()), file=\"" + str(r_session_out_file) + "\")\n")




# outputs the workflow subsection r-code
def output_workflow_r_subsection(workflow_r_subsection_information,out_file):

    # gets the subsection list
    workflow_r_subsection_scripts_list = workflow_r_subsection_information[0]

    for r_code in workflow_r_subsection_scripts_list:
        out_file.write(r_code + "\n")

    out_file.write("\n")









