import scipy.stats as stats
import math

#Method to get the overlap p-value and fold:
def hypergeometric_test(background_size, candidate_size, gene_set_size, overlap_size):

    p_Pos = stats.hypergeom.cdf(overlap_size ,background_size, candidate_size, gene_set_size)
    p_Neg = stats.hypergeom.sf(overlap_size - 1,background_size, candidate_size, gene_set_size)

    if candidate_size > 0 and gene_set_size  > 0 and overlap_size > 0:
        exp = (float(gene_set_size) / float(background_size)) * float(candidate_size)
        obs_vs_exp = math.log(float(overlap_size),2) - math.log(float(exp),2)

    else:
        obs_vs_exp = "NA"

    return obs_vs_exp, p_Pos, p_Neg
