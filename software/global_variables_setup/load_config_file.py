import os
import sys

def load_config_file(global_variables, config_file_parameter):

    # opens the config file
    if global_variables["config_file_flag"]:
        try:
            config_file = open(config_file_parameter.split("=")[1]).readlines()
        except:
            print >> sys.stderr, "Error: the config file path supplied is not valid: " + config_file_parameter
            sys.exit(1)
    else:
        SL_path = global_variables["SL_path"]
        config_file_path = os.path.join(SL_path, "bin", "config_file", "config.txt")
        config_file = open(config_file_path).readlines()


    config_dict = parse_config(config_file)
    check_config(config_dict)
    global_variables["config"] = config_dict


    if global_variables["config_file_flag"]:
        print "config loaded"
    else:
        print "default config loaded"

    return global_variables


# parses the config file
def parse_config(config_file):

    config_dict = {}
    first_workflow = True

    # iterates through the config elements:
    for line in config_file:

        # tests for a new workflow
        if line.rstrip().startswith("##---- ") and line.rstrip().endswith(" ----##"):

            # adds the previous workflow (if not the first)
            if first_workflow:
                first_workflow = False
            else:
                config_dict[workflow_name] = workflow_config_list

            # starts a new workflow
            workflow_name = line.rstrip().replace("##---- ","").replace(" ----##","").upper()
            workflow_config_list = []


        # adds a new element
        else:

            # ignores a blank line
            if line.rstrip() == "":
                continue

            else:
                #validates the element:
                if len(line.rstrip().split("\t")) != 3:
                    print >> sys.stderr, "Error: the config file entry: " + line.rstrip() + " is not in a valid format."
                    sys.exit(1)
                if len(line.rstrip().split("\t")[1].split(":")) != 3:
                    print >> sys.stderr, "Error: the config file entry: " + line.rstrip() + " is not in a valid format."
                    sys.exit(1)

                # parses the element and adds it to the workflow config list
                element_name,element_parameters,element_path = line.rstrip().split("\t")
                element_active,element_type,element_subtype = element_parameters.split(":")
                workflow_config_list.append([element_name,element_active.upper(),element_type,element_subtype,element_path])


    # always adds the final workflow
    config_dict[workflow_name] = workflow_config_list

    return config_dict


# checks that the config has all of the correct headers:
def check_config(config_dict):

    normexp = False
    pde = False
    mpde = False
    popex = False

    for workflow_name in config_dict:

        if workflow_name.upper() == "NORMEXP":
            normexp = True
        elif workflow_name.upper() == "PDE":
            pde = True
        elif workflow_name.upper() == "MPDE":
            mpde = True


    if normexp == False or pde == False or mpde == False:
        print >> sys.stderr, "Error: the config file does not have all of the required headers."
        sys.exit(1)




