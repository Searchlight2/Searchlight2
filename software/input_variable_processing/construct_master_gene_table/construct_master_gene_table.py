
from add_input_variable.add_background import add_background
from add_input_variable.add_ne import add_ne
from add_input_variable.add_de import add_de
from add_input_variable.add_annotations import add_annotations

from group_stats_calculation.group_stats_caclulation import group_stats_calculation

def construct_master_gene_table(global_variables):


    master_gene_table = add_background(global_variables)

    if global_variables["ne_flag"]:
        master_gene_table = add_ne(global_variables, master_gene_table)
        master_gene_table = group_stats_calculation(global_variables, master_gene_table)
    if global_variables["annotations_flag"]:
        master_gene_table = add_annotations(global_variables, master_gene_table)
    if global_variables["de_workflows_flag"]:
        master_gene_table = add_de(global_variables, master_gene_table)


    global_variables["master_gene_table"] = master_gene_table

    print "master gene table constructed"

    return global_variables






