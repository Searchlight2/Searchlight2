import sys

def check_workflow_prerequisites(global_variables):

    # Checks if an output path has been specified
    if not global_variables["out_path_flag"]:
        print("Error: no output path has been specified. Where will we keep your results? ", file=sys.stderr)
        sys.exit(1)

    # Checks if sample sheet has been supplied
    if not global_variables["ss_flag"]:
        print("Error: no sample sheet has been supplied. How will we know what your samples are?", file=sys.stderr)
        sys.exit(1)

    # checks if a background file has been supplied.
    if not global_variables["background_flag"]:
        print("Error: no background gene list has been supplied. How will we know what genes there are?", file=sys.stderr)
        sys.exit(1)

    # checks if a ne file has been supplied.
    if not global_variables["ne_flag"]:
        print("Error: no ne file has been supplied. How will we know whats being expressed?", file=sys.stderr)
        sys.exit(1)