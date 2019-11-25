from misc.new_directory import new_directory
import os


def write_data(out_path, genes_by_merged_signature):

    new_directory(out_path)
    new_directory(os.path.join(out_path, "gene_IDs"))
    new_directory(os.path.join(out_path, "gene_symbols"))

    # sort the signatures by number of genes
    sorted_on_number_of_genes = sorted(genes_by_merged_signature, key=lambda k: len(genes_by_merged_signature[k]), reverse=True)

    # prints the results for each signature
    signature_count = 1
    for signature in sorted_on_number_of_genes:

        signature_ids = []
        signature_symbols = []
        for gene in genes_by_merged_signature[signature]:
            signature_ids.append(gene.split("\t")[0] + "\n")
            signature_symbols.append(gene.split("\t")[1] + "\n")

        open(os.path.join(out_path, "gene_symbols", "signature_" + str(signature_count) + "_symbols.txt"), "w+").writelines(signature_symbols)
        open(os.path.join(out_path, "gene_IDs", "signature_" + str(signature_count) + "_IDs.txt"), "w+").writelines(signature_ids)

        signature_count += 1
