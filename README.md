## Searchlight2: rapid and comprehensive RNA-seq exploration and visualisation for unlimited differential datasets.

<br>

## Description

Once bulk RNA-seq differential data has been processed, i.e. aligned and then expression and differential tables generated, there remains the essential but lengthy process where the biology is explored, visualised and interpreted. Typically culminating in final manuscript figures. Remarkably, in both academia and industry the favoured method of bioinformaticians for completing this downstream step remains a semi-manually coded command line and R based (or similar) analysis which is laborious in the extreme, often taking weeks and months to complete.

Searchlight2 is a bulk RNA-seq exploration, visualisation and interpretation pipeline, which aims to automate this downstream analysis stage in its entirety, which it does so exclusively. When used alongside any standard alignment and processing pipeline (e.g. Star2, Hisat2, Kallisto, DEseq2, EdgeR, etc.) bioinfromaticians can consistently complete new bulk RNA-seq projects using under three hours of labour only. I.e. from raw sequence data to final manuscript figures, including all steps in-between - such as analysis plan, statistical analysis, visualisation, interpretation, panel selection and plot tweaking. 

Searchlight2 is suitable for use with any differential bulk RNA-seq experiment regardless of organism, experimental design, sample number or complexity. Results are indistinguishable from a manual analysis. The novelty of Searchlight2 is not complexity or that it is conceptually very challenging. It is brute force and user friendly. Its strength and novelty lie in: (1) recognising the need for independent but overlapping workflows allowing users to tailor analysis to meet specific questions; (2) providing a fully comprehensive statistical and visual analysis on the global, pathway and single gene levels; (3) providing means for comprehensive and familiar downstream user modification of all plots via user friendly R scripts and a Shiny graphical user interface; (4) allowing users to modify the default behaviour and visuals to their own taste, via the R-snippet database; (5) providing reports; (6) by being fully automated.

Searchlight2 accepts typical RNA-seq downstream analysis inputs - such as a sample sheet, expression matrix and any number of differential expression tables.  Searchlight2 is designed to help bioinformaticians, RNA-seq service providers and bench scientists progress bulk RNA-seq research projects rapidly and with minimal effort, thus freeing up resources for further in-depth analysis or alternative analytical approaches

Example outputs: https://github.com/Searchlight2/example-reports. 

<br>

## Download and setup


## Basic input files

All input files for Searchlight2 must be tab delimited. 

* Expression Matrix (EM). Any standard matrix of expression values (TPM, RPKM, Rlog, etc). With genes by row and samples by column. The first column should be the gene ID (Ensembl, Refseq, etc). There must be a header row with the first cell as "ID" and the rest the sample names. Sample names can't start with a number and can only include numbers, letters and underscore (_). 

* Differential expression table(s) (DE). 





## Quick start guide

To download the software please click the clone/download button above. **A quick start guide alongide a detailed usage guide can be found in the user manual provided with the download.** Searchlight accepts input files that are typical to RNA-seq. Namely a matrix of normalised expression values, a sample sheet, a transcriptome background file and tables of differential expression values (fold, p, adjusted p). Typical Searchlight runcode looks like this:

```
python Searchlight2.py 
--out path=out/
--normexp file=expression_matrix.tsv
--bg file=GRCh38_background.tsv
--ss file=sample_sheet.csv
--pde file=WT_vs_KO.tsv,numerator=KO,denominator=WT
```





