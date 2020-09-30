## Searchlight2: rapid and comprehensive RNA-seq exploration and visualisation for unlimited differential datasets.

<br>

## Description

<br>

Once bulk RNA-seq differential data has been processed, i.e. aligned and then expression and differential tables generated, there remains the essential but lengthy process where the biology is explored, visualised and interpreted. Typically culminating in final manuscript figures. Remarkably, in both academia and industry the favoured method of bioinformaticians for completing this downstream step remains a semi-manually coded command line and R based (or similar) analysis which is laborious in the extreme, often taking weeks and months to complete.

Searchlight2 is a bulk RNA-seq exploration, visualisation and interpretation pipeline, which aims to automate this downstream analysis stage in its entirety, which it does so exclusively. When used alongside any standard alignment and processing pipeline (e.g. Star2, Hisat2, Kallisto, DEseq2, EdgeR, etc.) bioinfromaticians can consistently complete new bulk RNA-seq projects using under three hours of labour only. I.e. from raw sequence data to final manuscript figures, including all steps in-between - such as analysis plan, statistical analysis, visualisation, interpretation, panel selection and plot tweaking. 

Searchlight2 is suitable for use with any differential bulk RNA-seq experiment regardless of organism, experimental design, sample number or complexity. Results are indistinguishable from a manual analysis. The novelty of Searchlight2 is not complexity or that it is conceptually very challenging. It is brute force and user friendly. Its strength and novelty lie in: (1) recognising the need for independent but overlapping workflows allowing users to tailor analysis to meet specific questions; (2) providing a fully comprehensive statistical and visual analysis on the global, pathway and single gene levels; (3) providing means for comprehensive and familiar downstream user modification of all plots via user friendly R scripts and a Shiny graphical user interface; (4) allowing users to modify the default behaviour and visuals to their own taste, via the R-snippet database; (5) providing reports; (6) by being fully automated.

Searchlight2 accepts typical RNA-seq downstream analysis inputs - such as a sample sheet, expression matrix and any number of differential expression tables.  Searchlight2 is designed to help bioinformaticians, RNA-seq service providers and bench scientists progress bulk RNA-seq research projects rapidly and with minimal effort, thus freeing up resources for further in-depth analysis or alternative analytical approaches


<br>

## Pipeline Overview

<br>

From the outset it is important to note that Searchlight2 is not a processing pipeline as it does not perform alignment, count reads or calculate expression and
differential expression values. These stages must be completed prior to the use of Searchlight2. Any processing pipeline is suitable (FastP, Hisat2, Star2, Kallisto, Deseq2, EdgeR, etc.), so long as you have a matrix of expression values (TPM, RPKM, Rlog, etc) and at least one differential expression table (DEseq2, EdgeR, etc) you may use Searchlight2. 

Searchlight2 is executed as a single command. Firstly, it validates the input files and combines them into a single “master gene table”, from which the downstream analysis is based. Next, it iterates through each workflow, generating: intermediate files; statistical analysis result files; per plot and per workflow R scripts, plots; a report in HMTL; and finally a Shiny app.

![link](/media/outline.png)

<br>

## Example outputs

<br>

**A screenshot of the report format**. [An example of the report is given here](https://github.com/Searchlight2/example-reports).

![link](/media/report.png)

<br>

**A screenshot of the Shiny app**. 

![link](/media/shiny.png)


<br>

**Sample outputs from various workflows**. 

![link](/media/NE.png)

<br>

## Download and first time setup

<br>

Searchlight2 can be downloaded from this Github page. By clicking the green "Code" button near the top right of the page. Then selecting Download Zip. 

* Once downloaded place the zip file into a folder of choice and unzip
* No further installation is required for the software
* Next, you will need to install Python (2.7) and the libraries Scipy and Numpy. [Here is an online guide](https://wiki.python.org/moin/BeginnersGuide/Download)
* Next, you will need to install R. We recommend doing so via RStudio (choose the free version). [Here is an online guide](https://rstudio.com/products/rstudio/download/)
* Finally, you will need to install several widely used R-packages: ggplot2, reshape, amap, grid, gridExtra, gtable, ggally, network, sna [Here is an online guide](https://www.datacamp.com/community/tutorials/r-packages-guide)
* If you also want to use the Shiny app feature you will need to install these additional R packages: shiny, shinyFiles, fs, shinycssloaders, graphics, dplyr

If you do not pre-install the R libraries Searchlight2 will run successfully and produce plot R code and reports, however it won't be able to generate the actual images.

<br>

## Basic input files


<br>

Searchlight2 is strict about the format of its inputs (but not the source) to ensure that analysis is correct. Setting up the input files is the most fiddly step but only takes a few minutes. **All input files for Searchlight2 must be tab delimited.**

* Expression Matrix (EM). Any standard matrix of expression values (TPM, RPKM, Rlog, etc). With genes by row and samples by column. The first column should be the gene ID (Ensembl, Refseq, etc). There must be a header row with the first cell as "ID" and the rest the sample names. Sample names can't start with a number and can only include numbers, letters and underscore (_). [Here is an example EM file.](https://raw.githubusercontent.com/Searchlight2/Searchlight2/master/example_data/normexp.tsv)


* Differential expression table(s) (DE). Any standard differential expression table (DESeq2, EdgeR, etc). With the genes by row and the columns trimmed down to include only: gene ID, log2 fold change, p-value and adjusted p-value (in this order). There must be a header row with the headers as exactly: "ID", "Log2Fold", "P", "P.Adj". Not case sensitive, ignoring the quotes. The ID type must be the same as the expression matrix. I.e you can't use ensembl IDs for the expression matrix and Refseq for the differential expression tables. Please supply one differential expression table per comparison. [Here is an example DE file.](https://raw.githubusercontent.com/Searchlight2/Searchlight2/master/example_data/ML_vs_LP.tsv)

* Sample sheet (SS). A standard tab delimited sample sheet listing each sample by name in the first column and the sample group it belongs to in the second. There must be a header row with the headers as exactly: "sample", "sample_group". Not case sensitive, ignoring the quotes. If you have several layers of sample groupings (such as cell type and also treatment and also age) you may include additional coulmns, under any header that you wish. Sample names and sample group names can't start with a number and can only include numbers, letters and underscore (_). [Here is an example SS file.](https://github.com/Searchlight2/Searchlight2/blob/master/example_data/sample_sheet.tsv)

* Background file (BG). A typical background annotation file for the organism and transcriptome build, listing all genes. We supply several of these with the software and they can easily be generated from Ensembls biomart. Genes should be in rows and specific annotation by column. The file must only have the annotations: Gene ID, Gene Symbol, Chromosome, Start position, Stop position and Biotype (type of gene). There must be a header row with the headers as exactly: "ID", "Symbol", "Chromosome", "Start", "Stop", "Biotype". Not case sensitive, ignoring the quotes. If you are unsure as to the gene symbol, just use the ID. If you are unsure at to the biotype simply put "gene" in every cell for that column. Please be aware, for every unique biotype (e.g. coding_gene, linc_RNA, etc) you enter Searchlgiht2 will perform and entire additional analysis (as well as asingle combined), which can be slow. For that reason we recommend simply to have all biotypes set as "gene" in you BG file, for your first few runs. [Here is an example BG file.](https://raw.githubusercontent.com/Searchlight2/Searchlight2/master/databases/background/human/Ensembl.GRCh37.p13.tsv)

<br>

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





