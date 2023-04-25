from workflows.mde.run_mde_workflows import run_mde_workflow


# iterates through biotypes
def mde_workflow(global_variables):

    print()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~        Mde         ~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()

    run_mde_workflow(global_variables, "all_genes")

    if global_variables["biotypes_flag"] and len(global_variables["biotypes_dict"].keys()) > 1:
        biotypes_dict = global_variables["biotypes_dict"]

        biotypes = sorted(biotypes_dict.keys())

        for biotype in biotypes:
            run_mde_workflow(global_variables, biotype)



