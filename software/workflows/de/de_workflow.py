from .run_de_workflows import run_de_workflow

# iterates through biotypes
def de_workflow(global_variables):

    print()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~         de         ~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()

    run_de_workflow(global_variables, "all_genes")

    if global_variables["biotypes_flag"] and len(list(global_variables["biotypes_dict"].keys())) > 1:
        biotypes_dict = global_variables["biotypes_dict"]

        biotypes = sorted(biotypes_dict.keys())

        for biotype in biotypes:
            run_de_workflow(global_variables, biotype)