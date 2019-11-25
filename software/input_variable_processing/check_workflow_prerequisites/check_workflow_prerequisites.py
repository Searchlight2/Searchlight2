import sys

def check_workflow_prerequisites(global_variables):

    # Checks if an output path has been specified
    if not global_variables["out_path_flag"]:
        print >> sys.stderr, "Error: no output path has been specified. Where will we keep your results? "
        sys.exit(1)

    # Checks if sample sheet has been supplied
    if not global_variables["ss_flag"]:
        print >> sys.stderr, "Error: no sample sheet has been supplied. How will we know what your samples are?"
        sys.exit(1)

    # checks if a background file has been supplied.
    if not global_variables["background_flag"]:
        print >> sys.stderr, "Error: no background gene list has been supplied. How will we know what genes there are?"
        sys.exit(1)

    # checks if a normexp file has been supplied.
    if not global_variables["normexp_flag"]:
        print >> sys.stderr, "Error: no normexp file has been supplied. How will we know whats being expressed?"
        sys.exit(1)