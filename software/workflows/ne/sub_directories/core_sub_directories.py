import os
from misc.new_directory import new_directory

def core_sub_directories(global_variables, out_path):


    new_directory(out_path)
    new_directory(os.path.join(out_path,"data"))
    new_directory(os.path.join(out_path,"data","gene_IDs"))
    new_directory(os.path.join(out_path,"data","gene_symbols"))
    new_directory(os.path.join(out_path,"data","statistical_analysis"))
    new_directory(os.path.join(out_path,"data","deciles"))
    new_directory(os.path.join(out_path,"data","quartiles"))
    new_directory(os.path.join(out_path,"plots"))













