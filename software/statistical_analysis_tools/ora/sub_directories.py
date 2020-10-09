import os
from misc.new_directory import new_directory

def sub_directories(out_path,type,out_path_tag):

    new_directory(out_path)
    new_directory(os.path.join(out_path,type))
    new_directory(os.path.join(out_path,type,out_path_tag))
    new_directory(os.path.join(out_path,type,out_path_tag,"network_data"))

