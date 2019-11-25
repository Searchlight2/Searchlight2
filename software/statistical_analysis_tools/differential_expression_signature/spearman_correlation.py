from scipy.stats import spearmanr
import numpy as np


def spearman_correlation(meta_genes):

    highest_correlation = [-10.0,"None","None"]

    for signature1 in meta_genes:
        for signature2 in meta_genes:

            spearman, p = spearmanr(meta_genes[signature1],meta_genes[signature2])

            if spearman > highest_correlation[0] and spearman != 1.0 and signature1 != signature2:
                highest_correlation = [spearman,signature1,signature2]

    return highest_correlation[0],highest_correlation[1],highest_correlation[2]
