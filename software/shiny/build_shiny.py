import os
from misc.new_directory import new_directory
from shutil import copyfile


def build_shiny(global_variables, shiny_info):

    build_server(global_variables, shiny_info)
    copy_shiny_files(global_variables)
    get_rdata(global_variables)


# builds the server
def build_server(global_variables, shiny_info):

    SL_path = global_variables["SL_path"]
    out_path = global_variables["out_path"]

    # builds the server
    new_directory(os.path.join(out_path, "shiny"))
    server_in_file = open(os.path.join(SL_path, "shiny", "app", "server_end.r")).readlines()
    server_out_file = open(os.path.join(out_path, "shiny", "server.r"), "w")

    server_out_file.write("###--- SERVER ---####\n")
    server_out_file.write("options(shiny.maxRequestSize=30*1024^2)\n")
    server_out_file.write("server <- function(input, output, session)\n")
    server_out_file.write("{\n\n")
    server_out_file.write(shiny_info)

    for line in server_in_file:
        server_out_file.write(line)


# copies files that don't need any modification
def copy_shiny_files(global_variables):

    SL_path = global_variables["SL_path"]
    out_path = global_variables["out_path"]

    # Adds the UI
    ui_in_path = os.path.join(SL_path, "shiny", "app", "ui.r")
    ui_out_path = os.path.join(out_path, "shiny", "ui.r")
    copyfile(ui_in_path, ui_out_path)

    # Adds the server
    server_in_path = os.path.join(SL_path, "shiny", "app", "global.r")
    server_out_path = os.path.join(out_path, "shiny", "global.r")
    copyfile(server_in_path, server_out_path)

    # Adds the www
    new_directory(os.path.join(out_path, "shiny", "www"))
    www_in_path = os.path.join(SL_path, "shiny", "app", "www", "sl2.gif")
    www_out_path = os.path.join(out_path, "shiny", "www", "sl2.gif")
    copyfile(www_in_path, www_out_path)
    www_in_path = os.path.join(SL_path, "shiny", "app", "www", "sl2.png")
    www_out_path = os.path.join(out_path, "shiny", "www", "sl2.png")
    copyfile(www_in_path, www_out_path)
    www_in_path = os.path.join(SL_path, "shiny", "app", "www", "style.css")
    www_out_path = os.path.join(out_path, "shiny", "www", "style.css")
    copyfile(www_in_path, www_out_path)


#finds the workflow rdata dumps and copies them to the shiny folder
def copy_rdata(biotype, global_variables):

    out_path = global_variables["out_path"]
    new_directory(os.path.join(out_path, "shiny", "rdata", biotype))

    if global_variables["normexp_flag"]:

        new_directory(os.path.join(out_path, "shiny", "rdata", biotype, "normexp_workflow"))
        rdata_in_path = os.path.join(out_path, biotype, "normexp_workflow", "plots", "workflow.rdata")
        rdata_out_path = os.path.join(out_path, "shiny", "rdata", biotype, "normexp_workflow", "workflow.rdata")

        try:
            copyfile(rdata_in_path, rdata_out_path)
        except:
            print "Warning: the normexp workflow Rdata file is missing. It will be omitted from Shiny."


    if global_variables["pde_workflows_flag"]:

        parsed_pde_parameters = global_variables["pde_parameters"]
        for pde_parameter_dict in parsed_pde_parameters:

            pde_ID = pde_parameter_dict["pde_ID"]
            pde_ID_no_spaces = pde_ID.replace(" ", "_")
            new_directory(os.path.join(out_path, "shiny", "rdata", biotype, "pde_workflows", pde_ID_no_spaces))
            rdata_in_path = os.path.join(out_path, biotype, "pde_workflows", pde_ID_no_spaces, "plots", "workflow.rdata")
            rdata_out_path = os.path.join(out_path, "shiny", "rdata", biotype, "pde_workflows", pde_ID_no_spaces, "workflow.rdata")

            try:
                copyfile(rdata_in_path, rdata_out_path)
            except:
                print "Warning: the PDE workflow " + pde_ID + " Rdata file is missing. It will be omitted from Shiny."

    if global_variables["mpde_workflows_flag"]:
        parsed_mpde_parameters = global_variables["mpde_parameters"]
        for mpde_dict in parsed_mpde_parameters:
            
            mpde_ID = mpde_dict["mpde_ID"]
            new_directory(os.path.join(out_path, "shiny","rdata", biotype, "mpde_workflows", mpde_ID))
            rdata_in_path = os.path.join(out_path, biotype, "mpde_workflows", mpde_ID, "plots", "workflow.rdata")
            rdata_out_path = os.path.join(out_path, "shiny","rdata", biotype, "mpde_workflows", mpde_ID, "workflow.rdata")

            try:
                copyfile(rdata_in_path, rdata_out_path)
            except:
                print "Warning: the MPDE workflow " + mpde_ID + " Rdata file is missing. It will be omitted from Shiny."


# gets the rdata
def get_rdata(global_variables):

    out_path = global_variables["out_path"]

    # does the work for "all genes"
    new_directory(os.path.join(out_path, "shiny","rdata"))
    copy_rdata("all_genes", global_variables)

    #does the work for the biotypes
    if global_variables["biotypes_flag"] and len(global_variables["biotypes_dict"].keys()) > 1:
        biotypes_dict = global_variables["biotypes_dict"]
        biotypes = sorted(biotypes_dict.keys())
        for biotype in biotypes:
            copy_rdata(biotype, global_variables)





