import os
from misc.new_directory import new_directory
from misc.get_Mde_columns_from_file import get_Mde_columns_from_file
from misc.ora_test import hypergeometric_test

def directional_overlaps(mde_file_path, out_path, de_IDs, overlap_statistics_list):

    # stores overlap stats
    overlap_statistics_dict = {}

    # infile
    mde_file = open(mde_file_path).readlines()

    # iterates through the pairwise combinations of des
    for de1_id in de_IDs:
        for de2_id in de_IDs:

            # iterates through the directions
            for de_1_direction in ["up","down"]:
                for de_2_direction in ["up", "down"]:


                    de1_id_parsed = de1_id.replace(" ", "_")
                    de2_id_parsed = de2_id.replace(" ", "_")
                    de_1_ID_direction = de1_id_parsed + "_" + de_1_direction
                    de_2_ID_direction = de2_id_parsed + "_" + de_2_direction


                    # excludes self comparing
                    if de1_id != de2_id:

                        # makes the directory
                        new_directory(os.path.join(out_path,"directional",de_1_ID_direction,de_2_ID_direction))

                        # gets the fold and significance columns for the des
                        de1_log2fold,de1_p,de1_padj,de1_sig,de1_valid =  get_Mde_columns_from_file(mde_file, de1_id)
                        de2_log2fold,de2_p, de2_padj, de2_sig, de2_valid = get_Mde_columns_from_file(mde_file, de2_id)

                        # stores the genes in each group
                        de1_unique_genes_IDs = []
                        de1_unique_genes_symbols = []
                        de2_unique_genes_IDs = []
                        de2_unique_genes_symbols = []
                        overlapping_genes_IDs = []
                        overlapping_genes_symbols = []

                        # gets the genes in each group
                        header = True
                        for line in mde_file:
                            if header:
                                header = False
                            else:
                                line_split = line.rstrip().split("\t")

                                # de1 unique
                                if line_split[de1_sig] == "True" and check_direction(de_1_direction,line_split[de1_log2fold]) == True:
                                    if line_split[de2_sig] != "True" or check_direction(de_2_direction,line_split[de2_log2fold]) == False:
                                        de1_unique_genes_IDs.append(line_split[0])
                                        de1_unique_genes_symbols.append(line_split[1])

                                # de2 unique
                                elif line_split[de2_sig] == "True" and check_direction(de_2_direction,line_split[de2_log2fold]) == True:
                                    if line_split[de1_sig] != "True" or check_direction(de_1_direction,line_split[de1_log2fold]) == False:
                                        if check_direction(de_2_direction,line_split[de2_log2fold]):
                                            de2_unique_genes_IDs.append(line_split[0])
                                            de2_unique_genes_symbols.append(line_split[1])

                                # overlapping
                                if line_split[de1_sig] == "True" and check_direction(de_1_direction,line_split[de1_log2fold]) == True:
                                    if line_split[de2_sig] == "True" and check_direction(de_2_direction,line_split[de2_log2fold]) == True:
                                        overlapping_genes_IDs.append(line_split[0])
                                        overlapping_genes_symbols.append(line_split[1])


                        # outputs the gene lists
                        de1_unique_genes_IDs_file = open(os.path.join(out_path,"directional",de_1_ID_direction,de_2_ID_direction,"IDs_" + de1_id_parsed + "_unique_genes.txt"),"w")
                        de1_unique_genes_symbols_file = open(os.path.join(out_path,"directional",de_1_ID_direction,de_2_ID_direction,"symbols_" + de1_id_parsed + "_unique_genes.txt"),"w")
                        de2_unique_genes_IDs_file = open(os.path.join(out_path,"directional",de_1_ID_direction,de_2_ID_direction,"IDs_" + de2_id.replace(" ","_") + "_unique_genes.txt"),"w")
                        de2_unique_genes_symbols_file = open(os.path.join(out_path,"directional",de_1_ID_direction,de_2_ID_direction,"symbols_" + de2_id_parsed + "_unique_genes.txt"),"w")
                        overlapping_genes_IDs_file = open(os.path.join(out_path,"directional",de_1_ID_direction,de_2_ID_direction,"IDs_overlapping_genes.txt"),"w")
                        overlapping_genes_symbols_file = open(os.path.join(out_path,"directional",de_1_ID_direction,de_2_ID_direction,"symbols_overlapping_genes.txt"),"w")

                        de1_unique_genes_IDs_file.write("\n".join(de1_unique_genes_IDs))
                        de1_unique_genes_symbols_file.write("\n".join(de1_unique_genes_symbols))
                        de2_unique_genes_IDs_file.write("\n".join(de2_unique_genes_IDs))
                        de2_unique_genes_symbols_file.write("\n".join(de2_unique_genes_symbols))
                        overlapping_genes_IDs_file.write("\n".join(overlapping_genes_IDs))
                        overlapping_genes_symbols_file.write("\n".join(overlapping_genes_symbols))


                        # gets the overlap stats
                        background_size = len(mde_file) -1
                        candidate_size = len(de1_unique_genes_IDs) + len(overlapping_genes_IDs)
                        gene_set_size = len(de2_unique_genes_IDs) + len(overlapping_genes_IDs)
                        overlap_size = len(overlapping_genes_IDs)
                        obs_vs_exp, p_Pos, p_Neg = hypergeometric_test(background_size, candidate_size, gene_set_size, overlap_size)

                        # updates the overlap stats (considers A up vs B up the same as B up vs A up)
                        sorted_de = "\t".join(sorted([de_1_ID_direction, de_2_ID_direction]))
                        if sorted_de not in overlap_statistics_dict:
                            overlap_statistics_list.append([de_1_ID_direction,de_2_ID_direction,background_size, candidate_size, gene_set_size,len(de1_unique_genes_IDs),len(de2_unique_genes_IDs),overlap_size,obs_vs_exp,p_Neg])
                        overlap_statistics_dict[sorted_de] = True


    return overlap_statistics_list




# tests for direction:
def check_direction(de_direction,de_log2fold):

    if (de_direction == "up" and float(de_log2fold) > 0) or (de_direction == "down" and float(de_log2fold) < 0):
        return True
    else:
        return False

