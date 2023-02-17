from .master_gene_table_report import master_gene_table_report
from .biotypes_report import biotypes_report

def processing_report(global_variables):

    print()
    print("=====================================")
    print("=====     processing report     =====")
    print("=====================================")
    print()

    if global_variables["biotypes_flag"]:
        biotypes_report(global_variables)

    if global_variables["ss_flag"] and global_variables["background_flag"]:
        master_gene_table_report(global_variables)


