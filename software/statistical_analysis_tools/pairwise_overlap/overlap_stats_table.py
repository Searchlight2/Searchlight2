import os

def overlap_stats_table(out_path, overlap_statistics_list):

    out_file = open(os.path.join(out_path,"overlap_statistics.csv"),"w")
    out_file.write("\t".join(["set_1_name","set_2_name", "background_genes","set_1_total_genes","set_2_total_genes","set 1_unique_gene","set_2_unique_genes","overlapping_genes","fold enrichment","p_value\n"]))

    for overlap in overlap_statistics_list:
        out_file.write("\t".join(str(x) for x in overlap) + "\n")
