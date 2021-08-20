[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FSearchlight2%2FSearchlight2&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits+today+%2F+all+time&edge_flat=false)](https://hits.seeyoufarm.com)

![link](/software/bin/report/logo.png)

### Automated bulk RNA-seq exploration and visualisation using dynamically generated R-scripts

<br>

# Table of contents
1. [Description](#Description)
2. [Pipeline overview](#Pipeline_overview)
3. [Example outputs](#Example_outputs)
4. [Download and first time setup](#Download_and_first_time_setup)
5. [Basic input files](#Basic_input_files)
6. [Quick start guide](#Quick_start_guide)
7. [Including a pathway analysis](#Including_a_pathway_analysis)
8. [Datasets with more than one differential comparison](#Datasets_with_more_than_one_differential_comparison)
9. [Including a formal signature analysis](#Including_a_formal_signature_analysis)
10. [Using the order sub-parameter](#Using_the_order_sub_parameter)
11. [Results](#Results)
12. [Downstream modification of plots and visualisations](#Downstream_modification_of_plots_and_visualisations)
13. [Default R settings](#Default_R_settings)
14. [Pathway database formats](#Pathway_database_formats)
15. [FAQ](#FAQ)
16. [List of parameters](#List_of_parameters)
17. [Contact and citation](#Contact_and_citation)

<br>

# Description <a name="Description"></a>

<br>

Once bulk RNA-seq differential data has been processed, i.e. aligned and then expression and differential tables generated, there remains the essential process where the biology is explored, visualised and interpreted. Culminating in report, thesis or manuscript figures. The typical method for completing this downstream step is a manually coded command line and R based (or similar) analysis. Which can be laborious - taking days or even weeks to complete.

Searchlight2 is a bulk RNA-seq exploration, visualisation and interpretation pipeline, that aims to automate the downstream analysis. When used alongside any standard alignment and processing pipeline (e.g. Star2, Hisat2, Kallisto, DEseq2, EdgeR, etc.) investigators can complete bulk RNA-seq projects in a matter of hours and with minimal effort. To a standard that is indistiguishable from a manual R based analysis. 

It is not a complicated pipeline to use or understand. It's strength are: 

1. A wide range of powerful and widely used analysis and visualization methods. 
2. The use of independent workflows covering expression, differential expression and signature analyssis. These provide compatibility with and experiment, regardless of  design, complexity, biology or organism. Whilst also simplifying the analysis. 
3. Generating comprehensive reports. 
4. Its use of R and R Shiny for all plots, making it easy for bioinformaticians and wet-lab scientists to modify all plots visually.
5. Its R-snippet database which allows users to modify the default appearance of all plots, to their own taste.
6. Searchlight2 is 100% automated.

Searchlight2 accepts typical RNA-seq downstream analysis inputs - such as a sample sheet, expression matrix and any number of differential expression tables.  It is designed to help bioinformaticians, RNA-seq service providers and bench scientists progress bulk RNA-seq research projects rapidly and with minimal effort, thus freeing up resources for further in-depth analysis or alternative analytical approaches.

**A sample analysis with reports can be found in the software download at sample_datasets/results.zip**

<br>

# Pipeline overview <a name="Pipeline_overview"></a>

<br>

From the outset it is important to note that Searchlight2 is not a processing pipeline as it does not perform alignment, count reads or calculate expression and
differential expression values. These stages must be completed prior to the use of Searchlight2. Any processing pipeline is suitable (FastP, Hisat2, Star2, Kallisto, Deseq2, EdgeR, etc.), so long as you have a matrix of expression values (TPM, RPKM, Rlog, etc) and at least one differential expression table (DEseq2, EdgeR, etc) you may use Searchlight2. 

Searchlight2 is executed as a single command. Firstly, it validates the input files and combines them into a single “master gene table”, from which the downstream analysis is based. Next, it iterates through each workflow, generating: intermediate files; statistical analysis result files; per plot and per workflow R scripts, plots; a report in HMTL; and finally a Shiny app.

![link](/media/outline.png)

<br>

# Example outputs <a name="Example_outputs"></a>

<br>

**A screenshot of the report format.** *Sample reports can be found in the software download at sample_datasets/results.zip*

![link](/media/report.png)

<br>

**A screenshot of the Shiny app**. 

![link](/media/shiny.png)

<br>

**Example outputs from a dataset exploring the effect of TGFB1 on primary cardiac fibroblasts.** This dataset has two sample groups, control and cells treated with TGFB1. The analysis, interpretation and figure generation was completed by a bioinformatician using 44 minutes and 30 seconds of work from a starting point of raw counts. Using DESeq2 and Searchlight2.

![link](/media/Ex1.png)

<br>

**Example outputs from a dataset exploring the synergistic effects of using a combination of RITA and CPI-203 on Chronic myeloid leukaemia (CML) haemopoietic stem cell (HSC) survival.** This dataset has four sample groups, Control, RITA, CPI and RITA plus CPI (Combo). The analysis, interpretation and figure generation was completed by a bioinformatician using 2 hours, 37 minutes and 11 seconds of work from a starting point of fastQ files. Using Star2, DESeq2 and Searchlight2.

![link](/media/Ex3.png)

<br>

# Download and first time setup <a name="Download_and_first_time_setup"></a>

<br>

Searchlight2 can be downloaded from this Github page. By clicking the green "Code" button near the top right of the page. Then selecting Download Zip. 

* Once downloaded place the zip file into a folder of choice and unzip
* No further installation is required for the software
* Next, you will need to install Python (2.7) and the libraries Scipy and Numpy. [Here is an online guide](https://wiki.python.org/moin/BeginnersGuide/Download)
* Next, you will need to install R. We recommend doing so via RStudio (choose the free version). [Here is an online guide](https://rstudio.com/products/rstudio/download/)
* Finally, you will need to install several widely used R-packages: ggplot2, reshape, amap, grid, gridExtra, gtable, ggally, network, sna. [Here is an online guide](https://www.datacamp.com/community/tutorials/r-packages-guide)
* If you also want to use the Shiny app feature you will need to install these additional R packages: shiny, shinyFiles, fs, shinycssloaders, graphics, dplyr.

If you do not pre-install the R libraries Searchlight2 will run successfully and produce plot R code and reports, however it won't be able to generate the actual images.

<br>

# Basic input files <a name="Basic_input_files"></a>


<br>

Searchlight2 is strict about the format of its inputs (but not the source) to ensure that analysis is correct. Setting up the input files is the most fiddly step but only takes a few minutes. **All input files for Searchlight2 must be tab delimited.**

* Expression Matrix (EM). Any standard matrix of expression values (TPM, RPKM, Rlog, etc). With genes by row and samples by column. The first column should be the gene ID (Ensembl, Refseq, etc). There must be a header row with the first cell as "ID" and the rest the sample names. Sample names can't start with a number and can only include numbers, letters and underscore (_). [Here is an example EM file.](https://github.com/Searchlight2/Searchlight2/blob/master/sample_datasets/EM.tsv)


* Differential expression table(s) (DE). Any standard differential expression table (DESeq2, EdgeR, etc). With the genes by row and the columns trimmed down to include only: gene ID, log2 fold change, p-value and adjusted p-value (in this order). There must be a header row with the headers as exactly: "ID", "Log2Fold", "P", "P.Adj". Not case sensitive, ignoring the quotes. The ID type must be the same as the expression matrix. I.e you can't use ensembl IDs for the expression matrix and Refseq for the differential expression tables. Please supply one differential expression table per comparison. [Here is an example DE file.](https://github.com/Searchlight2/Searchlight2/blob/master/sample_datasets/WT_vs_KO.tsv)

* Sample sheet (SS). A standard tab delimited sample sheet listing each sample by name in the first column and the sample group it belongs to in the second. There must be a header row with the headers as exactly: "sample", "sample_group". Not case sensitive, ignoring the quotes. If you have several layers of sample groupings (such as cell type and also treatment and also age) you may include additional coulmns, under any header that you wish. Sample names and sample group names can't start with a number and can only include numbers, letters and underscore (_). [Here is an example SS file.](https://github.com/Searchlight2/Searchlight2/blob/master/sample_datasets/SS.tsv)

* Background file (BG). A typical background annotation file for the organism and transcriptome build, listing all genes. We supply several of these with the software and they can easily be generated from Ensembls biomart. Genes should be in rows and specific annotation by column. The file must only have the annotations: Gene ID, Gene Symbol, Chromosome, Start position, Stop position and Biotype (type of gene). There must be a header row with the headers as exactly: "ID", "Symbol", "Chromosome", "Start", "Stop", "Biotype". Not case sensitive, ignoring the quotes. If you are unsure as to the gene symbol, just use the ID. If you are unsure at to the biotype simply put "gene" in every cell for that column. Please be aware, for every unique biotype (e.g. coding_gene, linc_RNA, etc) you enter Searchlgiht2 will perform and entire additional analysis (as well as asingle combined), which can be slow. For that reason we recommend simply to have all biotypes set as "gene" in you BG file, for your first few runs. [Here is an example BG file.](https://github.com/Searchlight2/Searchlight2/blob/master/backgrounds/human_GRCh38.p13.tsv)

<br>

# Quick start guide <a name="Quick_start_guide"></a>

<br>

To run Searchlight2, firstly ensure that you have correctly prepared your four basic input files as desribed [here](#Basic_input_files). The next (final) step is to set-up and run the command. Searchlight2 can be executed by navigating to the /Searchlight2/Software/ folder and running: 

<br>

```
python Searchlight2.py 
```

<br>

This will throw an error as you have not yet added the input parameters. Searchlight2 parameters have the format --parameter,sub-parameter=value. The key parameters are: 

<br>

```
--out path=my_desired_output_path
--bg file=path_to_my_background_file
--em file=path_to_my_expression_matrix_file
--ss file=path_to_my_sample_sheet_file
--de file=path_to_my_differential_expression_file,numerator=sample_group_1,denominator=sample_group_2
```

<br>

Mostly this is straightforward, except for the --de parameter which requires the additional sub-parameters: "numerator=" and denomintor=". Here you are expected to enter the names of the two sample groups that are being compared differentially. For example: if the DE file was of a comparison between WT and KO samples, we would enter numerator=KO,denominator=WT. The numerator should always be the sample group where a positive fold change in the DE file means an increase in expression. **It is very important to note** that the values entered into numerator= and denominator= (in this case KO & WT) must also be in the sample_group column of the sample sheet. With the same spelling. **Furthermore all paths must be complete from "root"** and not abbreviated from the working directory. **Importantly, do not put spaces between sub-parameters.**

<br>

To execute Searchlight2 using the provided sample dataset we might run the following. In this example we have simply placed Searchlight2 into a downloads folder, where we will also store the results. This will execute a comprehensive Searchlight2 analysis, producing statistical analysis, intermediate files, plots, reports, r-code and a Shiny app.

<br>

```
python Searchlight2.py --out path=/home/john/Downloads/results --bg file=/home/john/Downloads/Searchlight2/backgrounds/mouse_GRCm38.p6.tsv --em file=/home/john/Downloads/Searchlight2/sample_datasets/EM.tsv --ss file=/home/john/Downloads/Searchlight2/sample_datasets/SS.tsv --de file=/home/john/Downloads/Searchlight2/sample_datasets/DE_WT_vs_KO.tsv ,numerator=KO,denominator=WT
```

<br>

Broken down the command looks like this. 

<br>

```
python Searchlight2.py 
--out path=/home/john/Downloads/results 
--bg file=/home/john/Downloads/Searchlight2/backgrounds/mouse_GRCm38.p6.tsv 
--em file=/home/john/Downloads/Searchlight2/sample_datasets/EM.tsv 
--ss file=/home/john/Downloads/Searchlight2/sample_datasets/SS.tsv 
--de file=/home/john/Downloads/Searchlight2/sample_datasets/DE_WT_vs_KO.tsv,numerator=KO,denominator=WT
```

<br>

The default settings for deciding statistical significance are p.adj <= 0.05 and an absolute log2 fold change of >= 0.5 (i.e. at least 1.58 fold). These can be altered by using the log2fold= and p.adj= sub-parameters of the --de parameter. For example, re-running the sample command with the following would use a p.adj cut-off of 0.01 and no log2 fold cut-off:

<br>

```
--de file=/home/john/Downloads/Searchlight2/sample_datasets/DE_WT_vs_KO.tsv,numerator=KO,denominator=WT,p.adj=0.01,log2fold=0
```

<br>

# Including a pathway analysis <a name="Including_a_pathway_analysis"></a>

<br>

In the results you may notice that it does not currently include a pathway analysis (over-representation analysis (ORA) or upstream regulator analysis (URA)). This is because we have yet to include an ORA or URA database (such as GEO or TRRUST). To include over-representation analysis add the --ora parameter to the command:

<br>

```
--ora file=/home/john/Downloads/Searchlight2/gene_set_databases/GO_bp_mouse.tsv,type=GO_bp
```

<br>

The file= sub-parameter should point to a valid gene-set database file (such as GO, string, KEGG, etc) in the GMT format. Several of these are included in the download (Searchlight2/gene_set_databases/). For details of the GMT format please see [pathway database formats](#Pathway_database_formats). The type= sub-parameter is simply the name that you wish the database to be known as in the results. This name cannot start with a number and must include only letters, numbers and underscore (_). 

<br>

To also include an upstream regulator analysis add the --ura parameter to the command:

<br>

```
--ura file=/home/john/Downloads/Searchlight2/upstream_regulator_databases/TRRUST_mouse.tsv,type=TRRUST
```

<br>

The sub-parameters are analogous to those of the ORA parameter. Note that the upstream regulator database must be in the TRRUST format - see [pathway database formats](#Pathway_database_formats).

<br>

Using the sample dataset our full (broken down) command might look like this:

```
python Searchlight2.py 
--out path=/home/john/Downloads/results 
--bg file=/home/john/Downloads/Searchlight2/backgrounds/mouse_GRCm38.p6.tsv 
--em file=/home/john/Downloads/Searchlight2/sample_datasets/EM.tsv 
--ss file=/home/john/Downloads/Searchlight2/sample_datasets/SS.tsv 
--de file=/home/john/Downloads/Searchlight2/sample_datasets/DE_WT_vs_KO.tsv,numerator=KO,denominator=WT
--ora file=/home/john/Downloads/Searchlight2/gene_set_databases/GO_bp_mouse.tsv,type=GO_bp
--ura file=/home/john/Downloads/Searchlight2/upstream_regulator_databases/TRRUST_mouse.tsv,type=TRRUST
```

<br>

**It is important to note** that you may include as many different ORA or URA databases in a single run of Searchlight2. TO do so simply include an extra ORA or URA parameter pointing to a different database file. E.g.

<br>

```
--ora file=/home/john/Downloads/Searchlight2/gene_set_databases/GO_bp_mouse.tsv,type=GO_bp
--ora file=/home/john/Downloads/Searchlight2/gene_set_databases/GO_cc_mouse.tsv,type=GO_cc
--ora file=/home/john/Downloads/Searchlight2/gene_set_databases/GO_mf_mouse.tsv,type=GO_mf
--ura file=/home/john/Downloads/Searchlight2/upstream_regulator_databases/TRRUST_mouse.tsv,type=TRRUST
--ura file=/home/john/Downloads/IPA/IPA_database.tsv,type=IPA
```

<br>


# Datasets with more than one differential comparison <a name="Datasets_with_more_than_one_differential_comparison"></a>

<br>

**This section deals with what to do if your experiment has more than two types of sample, and so involves more than one differential expression comparison.** Searchlight2 fully supports these datasets, which we will refer to as "signature based" as they can include signatures beyond simply "up" or "down" regulated.

<br>

If you have more than one differential expression file (e.g. WT vs KO and KO vs KO_rescue) you may run all comparisons simultaneously simply by adding additional --de parameter. The broken down command for the sample dataset might look like this:

<br>

```
python Searchlight2.py 
--out path=/home/john/Downloads/results 
--bg file=/home/john/Downloads/Searchlight2/backgrounds/mouse_GRCm38.p6.tsv 
--em file=/home/john/Downloads/Searchlight2/sample_datasets/EM.tsv 
--ss file=/home/john/Downloads/Searchlight2/sample_datasets/SS.tsv 
--de file=/home/john/Downloads/Searchlight2/sample_datasets/DE_WT_vs_KO.tsv,numerator=KO,denominator=WT
--de file=/home/john/Downloads/Searchlight2/sample_datasets/DE_KO_rescue_vs_KO.tsv,numerator=KO_rescue,denominator=KO
```

<br>

In this scenario Searchlight2 will run a seperate de workflow for each, and will provide a seperate set of results for each (including a seperate report). **There is no upper limit to the number of differential comparisons that can be supplied this way**. 

<br>


# Including a formal signature analysis <a name="Including_a_formal_signature_analysis"></a>

<br>

So far, we have considered the sitation where we have several independant pairwise comparisons, which we have treated seperately (e.g. WT vs KO and KO vs KO_rescue). However, often it is desirable to ask how several groups of samples compare to each other in more a combinatorial or whole experiment sense. For example: what changes between WT and KO or what changes between KO and KO + rescue is interesting, but it does not tell us the extent to which the rescue returns the KO phenotype to WT. For this we would need to expore all three groups together. This can be achieved using the multiple differential expression (MDE) workflow, which is included via the --mde parameter. The --mde parameter has the following format:

<br>

```
--mde name=my_name,[numerator=DE_x_numerator*denominator=DE_x_denominator, numerator=DE_y_numerator*denominator=DE_y_denominator, ...]
```

<br>

The first sub-parameter is straightforward. --name= is simply a name for the workflow output folder. This as usual cannot start with a number and must include only letters, numbers and underscore (\_). The second sub-parameter takes a moment to consider. The --mde parameter allows two or more differential comparisons to be compared to each other simultaneously. This second sub-parameter tells Searchlight2 exactly which differential comparisons to include in the MDE. It does so by listing the specific numerator=,denominator= combination of each DE to be included. This DE must also be included in a valid --de parameter. For the sample dataset the broken down command might look like this:

<br>

```
python Searchlight2.py 
--out path=/home/john/Downloads/results 
--bg file=/home/john/Downloads/Searchlight2/backgrounds/mouse_GRCm38.p6.tsv 
--em file=/home/john/Downloads/Searchlight2/sample_datasets/EM.tsv 
--ss file=/home/john/Downloads/Searchlight2/sample_datasets/SS.tsv 
--de file=/home/john/Downloads/Searchlight2/sample_datasets/DE_WT_vs_KO.tsv,numerator=KO,denominator=WT
--de file=/home/john/Downloads/Searchlight2/sample_datasets/DE_KO_rescue_vs_KO.tsv,numerator=KO_rescue,denominator=KO
--mde name=rescue_effect,numerator=KO*denominator=WT,numerator=KO_rescue*denominator=KO
```

<br>

It is clear to see that to set-up the --mde all that we really needed to do was copy "numerator=,denominator=" from each --de parameters and substitute the , for a \*. This is Searchlight2s' way of understanding that we wish to include these two DE comparisons in a MDE. In this example Searchlight2 will use both sets of differential data and all WT, KO and KO_rescue samples to generate and explore signatures. It will additionally provide summaries and a formal overlap analysis between the two differential comparisons.

<br>

**Examples of the anlaysis and plots generated by the MDE workflow. From a dataset exploring steady state dendritic migration from the lamina propria (LP), through the mesentric lymph duct (ML) and into the mesenteric lymph node (MLN).**

![link](/media/MDE.png)

<br>

**It is very important to note** that there is no upper limit to either the number of DE's that can be included in a single MDE or the number of different MDE workflows that can be included in a single run of Searchlight2. Each different combination will ask a slightly different set of questions of the data. Our previous example (WT, KO, KO_rescue) included only two DE's and so there was only one possible combination of MDE. However, let us now consider a more complicated example. In a dataset with WT, KO and KO_rescue in two different tissues - skin and tendon we will have six groups of samples. We could have between 4 and 9 pertinent comparisons depending on the questions we wish to ask. Our broken down command might look like this:

<br>

```
python Searchlight2.py 
--out path=/home/john/Downloads/results 
--bg file=/home/john/Downloads/Searchlight2/backgrounds/mouse_GRCm38.p6.tsv 
--em file=/home/john/Downloads/complex_experiment/EM.tsv 
--ss file=/home/john/Downloads/complex_experiment/SS.tsv 
--de file=/home/john/Downloads/complex_experiment/DE_skin_WT_vs_skin_KO.tsv,numerator=skin_KO,denominator=skin_WT
--de file=/home/john/Downloads/complex_experiment/DE_skin_KO_rescue_vs_skin_KO.tsv,numerator=skin_KO_rescue,denominator=skin_KO
--de file=/home/john/Downloads/complex_experiment/DE_tendon_WT_vs_tendon_KO.tsv,numerator=tendon_KO,denominator=tendon_WT
--de file=/home/john/Downloads/complex_experiment/DE_tendon_KO_rescue_vs_tendon_KO.tsv,numerator=tendon_KO_rescue,denominator=tendon_KO
--de file=/home/john/Downloads/complex_experiment/DE_tendon_WT_vs_skin_WT.tsv,numerator=tendon_WT,denominator=skin_WT
--de file=/home/john/Downloads/complex_experiment/DE_tendon_KO_vs_skin_KO.tsv,numerator=tendon_KO,denominator=skin_KO
--de file=/home/john/Downloads/complex_experiment/DE_tendon_KO_rescue_vs_skin_KO_rescue.tsv,numerator=tendon_KO_rescue,denominator=skin_KO_rescue
--mde name=skin_rescue_effect,numerator=skin_KO*denominator=skin_WT,numerator=skin_KO_rescue*denominator=skin_KO
--mde name=tendon_rescue_effect,numerator=tendon_KO*denominator=tendon_WT,numerator=tendon_KO_rescue*denominator=tendon_KO
--mde name=KO_comparison,numerator=skin_KO*denominator=skin_WT,numerator=tendon_KO*denominator=tendon_WT
--mde name=rescue_comparison,numerator=skin_KO_rescue*denominator=skin_KO,numerator=tendon_KO_rescue*denominator=tendon_KO
--mde name=all,numerator=skin_KO*denominator=skin_WT,numerator=skin_KO_rescue*denominator=skin_KO,numerator=tendon_KO*denominator=tendon_WT,numerator=tendon_KO_rescue*denominator=tendon_KO
```

<br>

This is obviously starting to appear unweildy. However, it is worth noting that this complexity originates with the experimental design. In fact, Searchlight2 helps to simplify this by formally breaking the analysis down into useful components. That all of these reports will be generated does not mean that the user will wish to look them immediatley. They are readily available should the disucssion move in that direction. If we look at the --mde parameters we can see that many different, but speific research questions are being asked at once. Such as does rescue reverse the KO in skin or in tendon (skin_rescue_effect, tendon_rescue_effect). Does the KO influence the same genes in skin as it does tendon (KO_comparison). Is the rescue effect comparable between skin and tendon (rescue_comparison). Finally, if we look at all of the important genes across the whole experiment what do we see (all)? The experiment starts to become easier to handle when viewed this way. Especially as once executed (after 15 minutes or so of runtime) each of these questions and more will be fully answered. After discussion, panel selection and minor plot tweaking final manuscript figures can be quickly assembled.

<br>

# Using the order sub-parameter <a name="Using_the_order_sub_parameter"></a>

<br>

With the order= sub-parameter the order that sample groups appear in resultant plots can be manually chosen. It can be used in as part of a --de or --mde parameter. For example, in a DE comparing WT to KO the default is for WT to appear first on the plots and KO second. However if we add ,order=KO+WT this order will be reversed. This is purely visual, and does not affect the results. 

<br>

```
--de file=/home/john/Downloads/Searchlight2/sample_datasets/DE_WT_vs_KO.tsv,numerator=KO,denominator=WT,order=WT+KO
--mde name=rescue_effect,numerator=KO*denominator=WT,numerator=KO_rescue*denominator=KO,order=WT+KO+KO_rescue
```

<br>

**A further and highly useful feature of ,order=** is that it can be used to add sample groups that are not necessarily part of the DE or MDE - without actually affecting the result. For example, in a DE comparing WT to KO we might might want to know: at the genes that differ between WT and KO exclusively how do they behave in KO_rescue? To anser this we could use:

<br>

```
--de file=/home/john/Downloads/Searchlight2/sample_datasets/DE_WT_vs_KO.tsv,numerator=KO,denominator=WT,order=WT+KO+KO_rescue
```

<br>

This feature is particularly useful when using DE files generated from complex linear models, as it allows interaction terms (such as age, sex, etc) to be plotted alongside the differential terms. 

<br>

# Results <a name="Results"></a>

<br>

Searchlight2 produces comprehensive range of results. In this section we will outline what they are and where to find them. In the output folder you should see three items. If you used a sample sheet with multiple biotypes you will see these three items, plus a folder for each biotype.

<br>

![link](/media/results1.png)

<br>

The all_genes folder contains the results from the analysis using all genes supplied. Inside this folder you will see up to three folders - one for each type of workflow. If you didn't run a DE or MDE workflow these folders will not be present. The NE workflow is always generated. 

<br>

![link](/media/results2.png)

<br>

Each of these folders has a similar internal structure. We will therefore demonstrate via the DE folder. Inside the DE folder there will be one folder per DE workflow in your Searchlight2 run. By clicking on any of these it will bring us to the workflow results. These folders always contain three items only.

<br>

![link](/media/results3.png)

<br>

The report.html is usually the first item to look at in a new project. Double clicking will open a comrpehenisive report in your default web browser. This report hyperlinks the plots folder. Therefore if you move it away from this directory it will no longer show the images. The plots folder includes one folder for each type of analysis / plot used in the workflow (there will be many) alongside a workflow.r script and an r data / version dump. The workflow.r script is the script used by Searchlight2 to generate every plot in the workflow. This is further discussed in the [Downstream modification of plots and visualisations](#Downstream_modification_of_plots_and_visualisations) section. 

<br>

![link](/media/results4.png)

<br>

If we go back one level (away from plots) and enter the data folder, you will see a variety of intermediate data files for the workflow. Each of these can useful to further analysis in some way and are used by the R-scripts to generate the plots. There also be several sub-folders that are self explanatory. The statistical analysis folder includes resultant data files from statistical analysis modules such as: ORA, URA, signatures, overlap, etc.

<br>

![link](/media/results5.png)

<br>

# Downstream modification of plots and visualisations <a name="Downstream_modification_of_plots_and_visualisations"></a>

<br>

Once the results have been generated, and panels selected for report, thesis or manuscript figures it is usually necessary to perform plot "tweaking", such as resizing, or changeing dot colours to fit with other non-omic results. **As a deliberate design feature Searchlight2 plots are generated using R (ggplot2) and the R scripts used are supplied alongside the plot.** Each script is standalone, linking where necessary to the intermediate files located in the data folder. By modifying these scripts and re-running each plot can be quickly tweaked and regenerated. Scripts have a consistent, logical and well commented layout, with most visual features as named parameters, including a gg-theme. Below is an example of a folder with plot and r-script, and part of the contents of that script.

<br>

![link](/media/R1.png)

<br>

![link](/media/R2.png)

<br>

**In addition to individual scripts for each plot a "whole workflow" script is provided that will re-generate every plot in the workflow (workflow.r)**. By modifiying single parameters (such as fonts, colours, etc) in this workflow level r-script all plots can be modified simultaneously.

<br>

**For users who are not R literate, Searchlight2 also generates a Shiny app (graphical user interface)**, which allows a comprehensive range of visual features to be modified downstream for all plots in each workflow. To run the Shiny app please install R-studio ([see Download and first time setup](#Download_and_first_time_setup)). Next, goto the (base) results folder for your Searchlight2 run and open the "shiny" folder. Open the server.r file in R-studio click the "Run App" button in the top right, next to the green arrow. The app should open in your default web-browser. From there it is self explanatory. For example:

<br>

```
/Results/shiny/global.r
```

<br>

![link](/media/R3.png)

<br>

# Default R settings <a name="Default_R_settings"></a>

<br>

The default algorithms and visual style is suitable for publication, however it is possible to change. If you find that the style is not to your tastes, or you are changing e.g. font everytime that you run Searchlight2 it would be advantageous to modify the default behaviour. This can easily be achieved through Searchlight2s' R-snippet database. Which is located here:

<br>

```
/Searchlight2/software/bin/r
```

<br>

The R-scripts used to gernerate plots are assembles dynamically during run-time from a standard set of R-snippets. Each snippet contains code for one defined section of a script. For example, there is a snippet for the gg-theme and another for the default heatmap colours, and another for the clustering algorithm. Importantly these snippets are used to build the R-scripts for each plot that they are relevant. Thus, by modifying e.g. the default heatmap colouts R-snippet (to be a different colour) every plot that is a heatmap will have a new default, and this will be applied next time you run Searchlight2.

<br>

![link](/media/R4.png)


<br>

# Pathway database formats <a name="Pathway_database_formats"></a>

<br>

**Gene-set files** as used in the --ora parameter should be in the gmt format. I.e. one line per gene-set with the first cell as the gene-set name (such as cell cycle), the second cell as any notes (if there are none you can simply enter NA) and then one cell for each gene in the gene-set. [An example of a gene-set file can be found here.](https://github.com/Searchlight2/Searchlight2/blob/master/gene_set_databases/GO_bp_human.tsv)

<br>
**Updtream regulator files** as used in the --ura parameter should be in the trrust format. I.e. One line per regulator / target combo, with the first cell as the regulator (e.g. TP53) the second cell as the gene being regulated (e.g. BBC3) and the third cell as the direction (either Activation, Repression or Unknown).[An example of an upstream regulator file can be found here.](https://github.com/Searchlight2/Searchlight2/blob/master/upstream_regulator_databases/trrust.human.tsv)

<br>

# FAQ <a name="FAQ"></a>

<br>

**Does Searchlight 2 check my input data?** Yes. Searchlight2 thoroughly checks the integrity and format of all input data. Files which are in the wrong format (for example don't include numbers where they should, or the correct headers) are reported. In addition, all input parameters are checked for format.

<br>

**I am interested in exploring coding genes separately from non-coding genes. Can I do this?** Yes, Searchlight2 includes biotypes in the background file, and automatically runs a separate analysis for each type. Simply supply a background file with the appropriate biotypes. See ([basic input files](#Basic_input_files) for more information).

<br>

**I have used linear modeling with interaction terms for my differential expression. Which workflow does this fall under?** Though the interaction terms have been included in your model it is still a differential expression analysis (DE). Such models simply consider a pairwise interaction taking into account the effect of the interaction terms. It can however be useful to visualise the interaction terms alongside the differential results. This can be achieved using the order= sub-parameter

<br>

**There are plots in the plot folder but they don't appear in the report. All I see is a blank space. What’s going on?** The typical issue in this case is that either you are looking at a zipped version of the entire results folder (it must be unzipped). Or the report.html file has been moved somehow from its original folder. It must be located in the same directory as the plots folder. If neither of these are the case, please contact us. 

<br>


**I ran Searchlight2 but I can't see any plots in the plots folder. What’s going on?** Most likely the root cause is missing R libraries or an unforeseen bug in one of the plots in the R script. This will have a knock-on effect as Searclight2 runs the workflow R-scripts. Firstly ensure that you have installed all of the libraries listed in [Download and first time setup](#Download_and_first_time_setup). Next, try running the R script for the plots in question (e.g. plots/workflow.r) in R and investigating the error directly. If you cannot fix this easily, please contact us.

<br>

**My computer is not connected to the web, does this matter?** No. Searchlight 2 does not connect to anything external whatsoever, at any point. This is a deliberate design feature.

<br>

**I want to use p values instead of adjusted p values. Can I do this?** Yes, If you wish to use P values instead of adjusted P simply “munge” your file. I.e. replace the adjusted p values with the p values in the differential expression file. The format of each file is fixed – to make sure the user understands what they are doing, but its up to the user what they put in it.

<br>

**I am using a custom background file, and don’t have both gene IDs and gene symbols, nor gene biotypes what can I do?** As above though the format of each file is fixed it is up to the user what goes in. Try simply using the same values for IDs and symbols. Provided it matches the expression matrix and any differential expression files it doesn’t actually matter what is in these columns. So long as you are comfortable with what you are inputting. The same logic applies to biotypes, simply set them all to “gene”. 

<br>

**I have an issue that is not covered by the manual or FAQ.** Don’t we all! Email us directly using the contact provided. Though we are a small team we will try to respond ASAP.

<br>

# List of parameters <a name="List_of_parameters"></a>

<br>

**Annotations File.** Specifies any additional gene annotations, supplied as an annotation file. This parameter is optional.

```
--anno file=anotation_file_path.csv
```

<br>

**Background File.** Specifies the background file to be used. This parameter is required .

```
--bg file=background_file_path.csv
```

<br>

**Differential Expression Workflow.** Runs a differential expression workflow (DE) for a supplied DE file and sub-parameters. This option can be supplied more than once so long as it used a different DE file each time.

```
--de file=DE_file_path.csv,numerator=group_1,denominator=group2,log2fold=1,p.adj=0.05,order=group_1+group_2
```

| Sub-parameter | description |
| ----------- | ----------- |
| file | Full path to the DE file |
| numerator | Sample group that you wish to be the numerator. I.e. the sample group for which a positive fold change in the DE file indicates an increase in  	expression |
| numerator | Sample group that you wish to be the denominator. I.e. the sample group for which a negative fold change in the DE file indicates an increase in expression |
| log2fold | Log2 fold change cut-off for significance (absolute). A value of 0 indicates no cut-off. The default is 0.5 |
| p.adj | Adjusted p-avlue cut-off for significance. A value of 1 indicates no cut-off. The default is 0.05 |
| order | Manually specifcy the order for which sample groups appear in the results. Accepts sample groups separated by a +. Can inclide any sample groups in the sample sheet in any order. The default is numerator+denominator |

<br>

**Expression Matrix File.** Specifies the normalised expression matrix file to be used. This parameter is required.

```
--em file=EM_file_path.csv
```

<br>

**Ignore Normalised Expression Workflow.** Ignores the normalised expression workflow. Useful for debugging or rerunning only some workflows.

```
--ignore_ne T 
```

<br>

**Ignore Differential Expression Workflow.** Ignores the differential expression workflow. Useful for debugging or rerunning only some workflows.

```
--ignore_de T 
```

<br>

**Ignore Multiple Differential Expression Workflow.** Ignores the multiple differential expression workflow. Useful for debugging or rerunning only some workflows.

```
--ignore_mde T 
```

<br>

**Multiple Differential Expression Workflow.** Runs a multiple differential expression workflow (MDE) for a given combinaition of DE workflows. This option can be supplied more than once so long as it uses a different combination of DE workflows and name each time.

```
--mde file=DE_file_path.csv,numerator=group_1,denominator=group2,log2fold=1,p.adj=0.05,order=group_1+group_2
```

| Sub-parameter | description |
| ----------- | ----------- |
| name= | Name tag to give this MPDE. Can be any single word and is used only for identification. |
| numerator=*denominator= | Comma separated list of the DEs to be included in the MDE. Each DE in this list must also be supplied as a separate DE workflow. Each DE is referenced in this list by stating the numerator and denominator in the following format: numerator=sample_group1*denominator=sample_group2. E.g. the list might look like: numerator=sample_group1*denominator=sample_group2,numerator=sample_group3*denominator=sample_group4. There is no limit to the number of DEs that can be supplied to a MDE. |
| order | Manually specifcy the order for which sample groups appear in the results. Accepts sample groups separated by a +. Can include any sample groups in the sample sheet in any order. The default is all unique sample groups included within the MDE, in the order they appear in the sample sheet |
| scc | Threshold used for merging the various differential expression profiles into differential expression signatures. Two profiles that have a Spearman Correlation Coefficient above this value will be merged. The default is 0.75 |

<br>

**Over Representation Analysis.** Specifies the gene_set file and settings for an over representation analysis. This will be performed for each relevant workflow. This is parameter is optional, and can be included several times each with a different gene_set file (e.g. GO, KEGG, STRING), if desired.

```
--ora file=gene_set_file.csv,type=GO,p.adj=0.05,log2fold=1,min_set_size=5,max_set_size=250,network_overlap_ratio=0.5,network_overlap_size=5
```

| Sub-parameter | description |
| ----------- | ----------- |
| file= | Full path to gene set file |
| type= | Descriptive name for gene set file. Must be a single word. |
| p.adj= | Adjusted p value threshold for gene set significance. The default is 0.05. |
| log2fold= | Absolute log2fold enrichment threshold for gene set significance. The default is 1. |
| min_set_size= | To be included in the ORA a gene set must have at least this many genes in it. The default is 5 genes. |
| max_set_size= | To be included in the ORA a gene set must have less than this many genes in it. The default is 250 genes.  |
| network_overlap_ratio= | All network edges must have at least this overlap ratio. Using the Szymkiewicz-Simpson coefficient. The default is 0.5 |
| network_overlap_size= | All network edges must have at least this overlap size (number of genes). The default is 5 genes. |

<br>

**Output Folder Path.** Specifies the folder where results should be saved to. This parameter is required.

```
--out path=full_path_to_output_folder
```

<br>

**Sample Sheet File.** Specifies the sample sheet to be used. This parameter is required.

```
--ss file=SS_file_path.csv
```

<br>

**Upstream Regulator Analysis.** Specifies the upstream_regulator file and settings for an upstream regulator analysis. This will be performed for each relevant workflow. This is parameter is optional, and can be included several times each with a different upstream_regulator file (e.g. TRRUST, IPA), if desired.

```
--ura file=gene_set_file.csv,type=GO,zscore=2,p.adj=0.05,log2fold=1,min_set_size=5,max_set_size=250,network_overlap_ratio=0.5,network_overlap_size=5
```

| Sub-parameter | description |
| ----------- | ----------- |
| file= | Full path to upstream regulator file |
| type= | Descriptive name for upstream regulator file. Must be a single word (e.g TRRUST). |
| zscore= | Z-score threshold for upstream regulator activation. The default is 2. |
| p.adj= | Adjusted p value threshold for gene set significance. The default is 0.05. |
| log2fold= | Absolute log2fold enrichment threshold for gene set significance. The default is 1. |
| min_set_size= | To be included in the URA a gene set must have at least this many genes in it. The default is 5 genes. |
| max_set_size= | To be included in the URA a gene set must have less than this many genes in it. The default is 250 genes.  |
| network_overlap_ratio= | All network edges must have at least this overlap ratio. Using the Szymkiewicz-Simpson coefficient. The default is 0.5 |
| network_overlap_size= | All network edges must have at least this overlap size (number of genes). The default is 5 genes. |

<br>


# Contact and citation <a name="Contact_and_citation"></a>

<br>

To contact us please use the email address and header line below:

```
John[DOT]Cole[AT]glasgow[DOT]ac[DOT]uk

Header: Searchlight2 Query
```

<br>

To cite Searchlight2 please use: 

```
Cole, J.J., Faydaci, B.A., McGuinness, D. et al. Searchlight: automated bulk RNA-seq exploration and visualisation using dynamically generated R scripts. BMC Bioinformatics 22, 411 (2021). https://doi.org/10.1186/s12859-021-04321-2
```
<br>
