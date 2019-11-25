## Searchlight 2: rapid and comprehensive RNA-seq exploration and communication for unlimited differential datasets.

<br>

**Searchlight 2 automates the data exploration and visualisation stage of RNA-seq differential analysis as far as its possible**, by assuming that most experiments can be simplified into a combination of pre-set workflows, based on the experimental design. In doing so it has the potential to save days, weeks and even months worth of labour and associated cost per RNA-seq experiment - at no loss to specificity. It provides a comprehensive, yet breadth and depth curated selection of results including intermediate files, statistical analysis, extensive visualisation, simple and modifiable r-code, a Shiny app and fully realised reports. It is compatible with any annotated organism and any experimental design regardless of complexity. Searchlight 2 is easy to setup and use, has minimal requirements, and typically runs in under 5 minutes per workflow. We envisage Searchlight 2 to be of use to a wide range of RNA-seq users. Namely project bioinformaticians, RNA-seq service providers and to bench scientists with a cursory understanding of RNA-seq data analysis. Searchlight 2 is available at: https://github.com/Searchlight2/Searchlight2 and as a galaxy module.

<br>

## Downloading and using Searchlight 2.

To download the software please click the clone/download button above. A quick start guide alongide a detailed usage guide can be found in the user manual provided with the download. Searchlight accepts input files that are typical to RNA-seq. Namely a matrix of normalised expression values, a sample sheet, a transcriptome background file and tables of differential expression values (fold, p, adjusted p). Typical Searchlight runcode looks like this:

```
python Searchlight2.py 
--out path=out/
--normexp file=expression_matrix.tsv
--bg file=GRCh38_background.tsv
--ss file=sample_sheet.csv
--pde file=WT_vs_KO.tsv,numerator=KO,denominator=WT
```

Examples of Searchlight 2s outputs (including several reports) can be downkloaded from here: https://github.com/Searchlight2/example-reports. 

<br>

## Version 2.0.3

Changes as of 25th November 2019:
* Shiny app implemented
* minor fixes and tweaks to R code

<br>

## Version 2.0.2

Changes as of 17th April 2019:
* Revamped pairwise overlap and differential expression signautres algorithms.
* Plot descriptions, legends and methods added to the reports.
* User manual, example data and example reports included.
* General parameter and element name streamlining.
* Formal and rigorous testing applied. 

<br>

## Version 2.0.1

Changes as of 30th January 2019:
* Normexp, PDE and MPDE workflow types available with key functionality.
* Includes plots and reports in HMTL. Reports missing descriptions, legends and methods.
* Includes Intermediate files.
* Includes R scripts generated via dynamic R code snippets, controlled via elements lists.
* Hypergeometric gene set enrichement algorithm.
* Upstream regulator algorithm.
* Spatial analysis algorthim.
* Pairwise overlap algorithm.


