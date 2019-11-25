from scipy.stats import zscore
import numpy as np

# method to get expression data of all samples
def get_expression_data(data, sample_list,genes_by_signature, signatures_by_gene):

    data_columns = []

    # get column index of each sample
    header_split = data[0].rstrip().split("\t")
    for sample in sample_list:
        column_index = 0
        for header in header_split:
            if sample == header:
                data_columns.append(column_index)
            column_index += 1


    # get expression data for each gene and add to the appropriate signature
    header = True
    for line in data:
        if header:
            header = False
        else:

            # gets the expression data
            line_split = line.rstrip().split("\t")
            gene = line_split[0] + "\t" + line_split[1]
            expression_data = []
            for column in data_columns:
                expression_data.append(line_split[column])

            # converts to a z-score
            zscore_data = np.array(expression_data).astype(np.float)
            z_transformed = zscore(zscore_data)

            # checks that the z-score is not nan
            if str(z_transformed[0]) == "nan":
                z_transformed = [0.0] * len(sample_list)

            # updates the signature
            signature = signatures_by_gene[gene]
            gene_information = genes_by_signature[signature][gene]
            gene_information["expression_data"] = expression_data
            gene_information["zscore_data"] = z_transformed
            genes_by_signature[signature][gene] = gene_information

    return genes_by_signature
