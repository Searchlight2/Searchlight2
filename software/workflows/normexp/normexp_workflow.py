from run_normexp_workflow import run_normexp_workflow

# iterates through biotypes
def normexp_workflow(global_variables):

    print
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "~~~~~       normexp       ~~~~~"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print

    run_normexp_workflow(global_variables, "all_genes")

    if global_variables["biotypes_flag"] and len(global_variables["biotypes_dict"].keys()) > 1:
        biotypes_dict = global_variables["biotypes_dict"]

        biotypes = sorted(biotypes_dict.keys())

        for biotype in biotypes:
            run_normexp_workflow(global_variables, biotype)
