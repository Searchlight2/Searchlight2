import os
from statistical_analysis_tools.ipa_ureg.ipa_ureg import ipa_ureg


def ipa_ureg_helper(out_path,global_variables):
    background_path = os.path.join(out_path, "data", "gene_symbols", "gene_symbols.txt")
    ipa_candidate_list_path = os.path.join(out_path, "data", "PDE_annotated.csv")
    hypergeometric_candidate_list_path = os.path.join(out_path,"data","gene_symbols","gene_symbols_significant.txt")
    ureg_out_path = os.path.join(out_path, "data", "statistical_analysis", "upstream_regulators")
    ipa_ureg(ipa_candidate_list_path,hypergeometric_candidate_list_path, background_path, global_variables, ureg_out_path,"NONE")