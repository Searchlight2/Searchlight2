import os
from statistical_analysis_tools.spatial_enrichment.spatial_enrichment import spatial_enrichment


def spatial_enrichment_helper(global_variables, out_path, de_parameter_dict):

    sample_groups = de_parameter_dict["order_list"]
    in_path = os.path.join(out_path,"data","de_annotated.csv")
    out_path = os.path.join(out_path,"data","statistical_analysis","spatial_enrichment")

    spatial_enrichment(global_variables, in_path, sample_groups, out_path, "de")


