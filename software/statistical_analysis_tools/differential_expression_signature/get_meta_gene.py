def get_meta_gene(genes_by_signature, sample_list):

    meta_genes = {}

    # iterates through the signatures, creates the meta-gene
    for signature in list(genes_by_signature.keys()):

        meta_gene = [0.0]*len(sample_list)
        signature_genes = genes_by_signature[signature]

        # iterates through the genes in the signature
        for gene in list(signature_genes.keys()):
            gene_information = signature_genes[gene]
            z_transformed = gene_information["zscore_data"]

            # adds the gene z-score to each samples total
            for index in range(0,len(meta_gene)):
                meta_gene[index] = meta_gene[index] + z_transformed[index]

        # gets the mean z-score per sample, for the signature (i.e. the metagene)
        for index in range(0,len(meta_gene)):
            meta_gene[index] = float(meta_gene[index]) / float(len(list(signature_genes.keys())))

        meta_genes[signature] = meta_gene

    return meta_genes





