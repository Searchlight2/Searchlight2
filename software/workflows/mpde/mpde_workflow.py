from run_mpde_workflows import run_mpde_workflow


# iterates through biotypes
def mpde_workflow(global_variables):

    print
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "~~~~~        MPDE         ~~~~~"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print

    run_mpde_workflow(global_variables, "all_genes")

    if global_variables["biotypes_flag"] and len(global_variables["biotypes_dict"].keys()) > 1:
        biotypes_dict = global_variables["biotypes_dict"]

        biotypes = sorted(biotypes_dict.keys())

        for biotype in biotypes:
            run_mpde_workflow(global_variables, biotype)



