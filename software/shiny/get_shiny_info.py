import os

def get_shiny_info(global_variables):

    biotypes = ["\"all genes\" = \"all_genes\""]
    workflow_types = []
    pde_workflow_names = []
    mpde_workflows_names = []
    normexp_plots = []
    pde_plots = []
    mpde_plots = []
    hgsea_types = []
    ipa_ureg_types = []

    # parses the biotypes
    if global_variables["biotypes_flag"] and len(global_variables["biotypes_dict"].keys()) > 1:
        biotypes_dict = global_variables["biotypes_dict"]
        biotype_names = sorted(biotypes_dict.keys())
        for biotype in biotype_names:
            biotypes.append("\"" + biotype.replace("_", " ") + "\" = \"" + biotype + "\"")


    # parses the normexp workflow info
    if global_variables["normexp_flag"] and global_variables["ss_flag"] and global_variables["background_flag"] and len(global_variables["sample_groups"].keys()) > 0:

        # normexp workflow type
        workflow_types.append("\"normexp\" = \"normexp_workflow\"")

        # normexp workflow plots
        normexp_plots = add_plots(global_variables["config"]["NORMEXP"], global_variables)


    # parses the pde workflow info
    if global_variables["pde_workflows_flag"] and global_variables["ss_flag"] and global_variables["background_flag"] and global_variables["normexp_flag"]:

        # pde workflow type
        workflow_types.append("\"pde\" = \"pde_workflows\"")

        # pde workflow names
        parsed_pde_parameters = global_variables["pde_parameters"]
        for pde_parameter_dict in parsed_pde_parameters:
            pde_workflow_names.append("\"" + pde_parameter_dict["pde_ID"] + "\" = \"" + pde_parameter_dict["pde_ID"].replace(" ", "_") + "\"")

        # pde workflow plots
        pde_plots = add_plots(global_variables["config"]["PDE"], global_variables)


    if global_variables["mpde_workflows_flag"] and global_variables["ss_flag"] and global_variables["background_flag"] and global_variables["normexp_flag"] and global_variables["pde_workflows_flag"]:

        # mpde workflow type
        workflow_types.append("\"mpde\" = \"mpde_workflows\"")

        # mpde workflow names
        parsed_mpde_parameters = global_variables["mpde_parameters"]
        for mpde_dict in parsed_mpde_parameters:
            mpde_workflows_names.append("\"" + mpde_dict["mpde_ID"].replace("_", " ") + "\" = \"" + mpde_dict["mpde_ID"] + "\"")

        # mpde workflow plots
        mpde_plots = add_plots(global_variables["config"]["MPDE"], global_variables)

    if global_variables["hypergeom_gs_flag"]:
        parsed_hypergeom_gene_sets_parameters = global_variables["hypergeom_gs_parameters"]
        for hypergeom_gene_set_parameter_dict in parsed_hypergeom_gene_sets_parameters:
            hgsea_types.append("\"" + hypergeom_gene_set_parameter_dict["type"] + "\"")

    if global_variables["ipa_ureg_flag"]:
        parsed_ipa_ureg_parameters = global_variables["ipa_ureg_parameters"]
        for ipa_ureg_parameters_dict in parsed_ipa_ureg_parameters:
            ipa_ureg_types.append("\"" + ipa_ureg_parameters_dict["type"] + "\"")




    # prints the Shiny info
    shiny_info = "\n"
    shiny_info += "\tbiotypes = c(" + ",".join(biotypes) + ")\n"
    shiny_info += "\tworkflow_types = c(" + ",".join(workflow_types) + ")\n"
    shiny_info += "\tpde_workflow_names = c(" + ",".join(pde_workflow_names) + ")\n"
    shiny_info += "\tmpde_workflow_names = c(" + ",".join(mpde_workflows_names) + ")\n"
    shiny_info += "\tnormexp_plots = c(" + ",".join(normexp_plots) + ")\n"
    shiny_info += "\tpde_plots = c(" + ",".join(pde_plots) + ")\n"
    shiny_info += "\tmpde_plots = c(" + ",".join(mpde_plots) + ")\n"
    shiny_info += "\thgsea_databases = c(" + ",".join(hgsea_types) + ")\n"
    shiny_info += "\tureg_databases = c(" + ",".join(ipa_ureg_types) + ")\n"
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
                        plot_names.append("\"" + plot_name.replace("mpde_","").replace("pde_","").replace("normexp_","").replace("_"," ") + "\" = \"" + plot_name+ "\"")

    return plot_names



# checks that prerequisites have been met for running an elements command
def check_element_prerequisites(element_active, element_type, element_subtype, element_path, global_variables):

    if element_active == "FALSE":
        return False
    elif element_subtype == "hypergeometric_gene_set" and global_variables["hypergeom_gs_flag"] == False:
        return False
    elif element_subtype == "ipa_ureg" and global_variables["ipa_ureg_flag"] == False:
        return False
    elif element_type == "plot" and element_path.upper() == "NONE":
        return False
    else:
        return True