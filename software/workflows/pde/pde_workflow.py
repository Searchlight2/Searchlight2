from run_pde_workflows import run_pde_workflow

# iterates through biotypes
def pde_workflow(global_variables):

    print
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "~~~~~         PDE         ~~~~~"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print

    run_pde_workflow(global_variables, "all_genes")

    if global_variables["biotypes_flag"] and len(global_variables["biotypes_dict"].keys()) > 1:
        biotypes_dict = global_variables["biotypes_dict"]

        biotypes = sorted(biotypes_dict.keys())

        for biotype in biotypes:
            run_pde_workflow(global_variables, biotype)