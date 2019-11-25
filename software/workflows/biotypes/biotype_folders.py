import os
from misc.new_directory import new_directory


def biotype_folders(global_variables):


    out_path = global_variables["out_path"]

    # makes the all genes directory
    new_directory(os.path.join(out_path,"all_genes"))


    if global_variables["biotypes_flag"]:

        biotypes_dict = global_variables["biotypes_dict"]

        for biotype in biotypes_dict:
            new_directory(os.path.join(out_path,biotype))
