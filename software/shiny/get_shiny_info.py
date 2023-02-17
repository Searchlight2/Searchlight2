import os

def get_shiny_info(global_variables):

    biotypes = ["\"all genes\" = \"all_genes\""]
    workflow_types = []
    de_workflow_names = []
    mde_workflows_names = []
    ne_plots = []
    de_plots = []
    mde_plots = []
    hgsea_types = []
    ura_types = []

    # parses the biotypes
    if global_variables["biotypes_flag"] and len(list(global_variables["biotypes_dict"].keys())) > 1:
        biotypes_dict = global_variables["biotypes_dict"]
        biotype_names = sorted(biotypes_dict.keys())
        for biotype in biotype_names:
            biotypes.append("\"" + biotype.replace("_", " ") + "\" = \"" + biotype + "\"")


    # parses the ne workflow info
    if global_variables["ne_flag"] and global_variables["ss_flag"] and global_variables["background_flag"] and len(list(global_variables["sample_groups"].keys())) > 0:

        # ne workflow type
        workflow_types.append("\"ne\" = \"ne_workflow\"")

        # ne workflow plots
        ne_plots = add_plots(global_variables["config"]["NE"], global_variables)


    # parses the de workflow info
    if global_variables["de_workflows_flag"] and global_variables["ss_flag"] and global_variables["background_flag"] and global_variables["ne_flag"]:

        # de workflow type
        workflow_types.append("\"de\" = \"de_workflows\"")

        # de workflow names
        parsed_de_parameters = global_variables["de_parameters"]
        for de_parameter_dict in parsed_de_parameters:
            de_workflow_names.append("\"" + de_parameter_dict["de_ID"] + "\" = \"" + de_parameter_dict["de_ID"].replace(" ", "_") + "\"")

        # de workflow plots
        de_plots = add_plots(global_variables["config"]["DE"], global_variables)


    if global_variables["mde_workflows_flag"] and global_variables["ss_flag"] and global_variables["background_flag"] and global_variables["ne_flag"] and global_variables["de_workflows_flag"]:

        # mde workflow type
        workflow_types.append("\"mde\" = \"mde_workflows\"")

        # mde workflow names
        parsed_mde_parameters = global_variables["mde_parameters"]
        for mde_dict in parsed_mde_parameters:
            mde_workflows_names.append("\"" + mde_dict["mde_ID"].replace("_", " ") + "\" = \"" + mde_dict["mde_ID"] + "\"")

        # mde workflow plots
        mde_plots = add_plots(global_variables["config"]["MDE"], global_variables)

    if global_variables["ora_flag"]:
        parsed_hypergeom_gene_sets_parameters = global_variables["ora_parameters"]
        for hypergeom_gene_set_parameter_dict in parsed_hypergeom_gene_sets_parameters:
            hgsea_types.append("\"" + hypergeom_gene_set_parameter_dict["type"] + "\"")

    if global_variables["ura_flag"]:
        parsed_ura_parameters = global_variables["ura_parameters"]
        for ura_parameters_dict in parsed_ura_parameters:
            ura_types.append("\"" + ura_parameters_dict["type"] + "\"")




    # prints the Shiny info
    shiny_info = "\n"
    shiny_info += "\tbiotypes = c(" + ",".join(biotypes) + ")\n"
    shiny_info += "\tworkflow_types = c(" + ",".join(workflow_types) + ")\n"
    shiny_info += "\tde_workflow_names = c(" + ",".join(de_workflow_names) + ")\n"
    shiny_info += "\tmde_workflow_names = c(" + ",".join(mde_workflows_names) + ")\n"
    shiny_info += "\tne_plots = c(" + ",".join(ne_plots) + ")\n"
    shiny_info += "\tde_plots = c(" + ",".join(de_plots) + ")\n"
    shiny_info += "\tmde_plots = c(" + ",".join(mde_plots) + ")\n"
    shiny_info += "\thgsea_databases = c(" + ",".join(hgsea_types) + ")\n"
    shiny_info += "\tureg_databases = c(" + ",".join(ura_types) + ")\n"
    return shiny_info




# gets a list of the plots from the config file
def add_plots(config, global_variables):

    plot_names = []

    # iterates through the elements
    for element in config:
        element_name, element_active, element_type, element_subtype, element_path = element

        # checks prerequisites
        if check_element_prerequisites(element_active, element_type, element_subtype, element_path, global_variables):

            # checks for a plot
            if element_type == "plot":

                # gets the R plot snippet name:
                element_file = open(os.path.join(global_variables["SL_path"], "bin", "element_list", element_path)).readlines()

                for line in element_file:
                    if line.startswith("plot/"):
                        plot_name = line.rstrip().replace("plot/","").replace(".txt","")
                        plot_names.append("\"" + plot_name.replace("mde_","").replace("de_","").replace("ne_","").replace("_"," ") + "\" = \"" + plot_name+ "\"")

    return plot_names



# checks that prerequisites have been met for running an elements command
def check_element_prerequisites(element_active, element_type, element_subtype, element_path, global_variables):

    if element_active == "FALSE":
        return False
    elif element_subtype == "ora" and global_variables["ora_flag"] == False:
        return False
    elif element_subtype == "ura" and global_variables["ura_flag"] == False:
        return False
    elif element_type == "plot" and element_path.upper() == "NONE":
        return False
    else:
        return True