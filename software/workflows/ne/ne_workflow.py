from .run_ne_workflow import run_ne_workflow

# iterates through biotypes
def ne_workflow(global_variables):

    print()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~       ne       ~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()

    run_ne_workflow(global_variables, "all_genes")

    if global_variables["biotypes_flag"] and len(list(global_variables["biotypes_dict"].keys())) > 1:
        biotypes_dict = global_variables["biotypes_dict"]

        biotypes = sorted(biotypes_dict.keys())

        for biotype in biotypes:
            run_ne_workflow(global_variables, biotype)
