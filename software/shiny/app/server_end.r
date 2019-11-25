

# populate the dropdowns
output$biotypeDropdown <- renderUI({
  selectInput("biotype", "biotype", choices = c("SELECT A BIOTYPE" = "", biotypes))
})

output$workflowTypeDropdown <- renderUI({
  if (exists("workflow_types")){selectInput("workflow_type", "workflow type", choices = c("SELECT A WORKFLOW TYPE" = "", workflow_types))}
})

output$workflowNameDropdown <- renderUI({
  if (!is.null(input$biotype) && !is.null(input$workflow_type)) {
    if (input$workflow_type == "pde_workflows"){selectInput("workflow_name", "workflow name", choices = c("SELECT A WORKFLOW" = "", pde_workflow_names))}
    else if (input$workflow_type == "mpde_workflows"){selectInput("workflow_name", "workflow name", choices = c("SELECT A WORKFLOW" = "", mpde_workflow_names))}
  }
})

output$plotDropdown <- renderUI({
  if (!is.null(input$biotype) && !is.null(input$workflow_type)) {
    
    # for a normexp workflow - which has a single fixed name
    if (input$workflow_type == "normexp_workflow") {
      
      # loads the R data
      rData_path = paste(getwd(),"rdata",input$biotype,"normexp_workflow","workflow.rdata",sep=.Platform$file.sep)
      env <- reactiveFileReader(intervalMillis = 1000, session = session, filePath = rData_path, readFunc = LoadEnv)
      env()[[names(env())[1]]]
      
      # creates the plot selection box
      selectInput("plot_type", "plot", choices = c("SELECT A PLOT" = "", normexp_plots))
    }
    
    # for PDE and MPDE workflows - which can have a choice of names
    else if (!is.null(input$workflow_name) && input$workflow_name != "") {
      print(input$workflow_name)
      if (input$workflow_type == "pde_workflows") {
        
        # loads the R data
        rData_path = paste(getwd(),"rdata",input$biotype,"pde_workflows",input$workflow_name,"workflow.rdata",sep=.Platform$file.sep)
        env <- reactiveFileReader(intervalMillis = 1000, session = session, filePath = rData_path, readFunc = LoadEnv)
        env()[[names(env())[1]]]
        
        # creates the plot selection box
        selectInput("plot_type", "plot", choices = c("SELECT A PLOT" = "", pde_plots))
      }
      else if (input$workflow_type == "mpde_workflows") {
        
        # loads the R data
        rData_path = paste(getwd(),"rdata",input$biotype,"mpde_workflows",input$workflow_name,"workflow.rdata",sep=.Platform$file.sep)
        env <- reactiveFileReader(intervalMillis = 1000, session = session, filePath = rData_path, readFunc = LoadEnv)
        env()[[names(env())[1]]]
        
        # creates the plot selection box
        selectInput("plot_type", "plot", choices = c("SELECT A PLOT" = "", mpde_plots))
      }
    }
  }
})


# render plot options per plot
output$ui <- renderUI({
  
  
  if (is.null(input$plot_type))
    return()
  
  
  # renders each plot
  switch(input$plot_type,
         "normexp_distribution_of_expression_values" = tagList(
           selectInput("sample","sample",samples, samples[1]),
           numericInput("line_thickness","line thickness",1),
           ###selectInput("legend_position","legend position",c("top" = "top", "right" = "right", "bottom" = "bottom", "left" = "left", "none" = "n"), "n"),
           textInput("x_axis_label","x axis label","expression (log10)"),
           textInput("y_axis_label","y axis label","density"),
           numericInput("transparency","transparency",0.5),
           numericInput("plot_height","plot height",250),
           numericInput("plot_width","plot width",250)),
         
         "normexp_pca_contribution_of_components" = tagList(
           selectInput("line_type","line type",c("blank", "solid", "dashed", "dotted", "dotdash", "longdash", "twodash", "1F", "F1", "4C88C488", "12345678"), "solid"),
           textInput("line_colour","line colour","black"),
           textInput("dot_colour","dot colour","red"),
           numericInput("dot_size","dot size",4),
           numericInput("dot_transparency","dot transparency",1),
           textInput("x_axis_label","x axis label","component"),
           textInput("y_axis_label","y axis label","proportion of variance (%)"),
           numericInput("line_size","line size",1),
           numericInput("plot_height","plot height",300),
           numericInput("plot_width","plot width",400)),
         
         "normexp_pca_scatter_plot" = tagList(
           selectInput("ss_column","sample sheet column",sample_sheet_column_names,sample_sheet_column_names[1]),
           selectInput("component_x","component x",c("1"="PC1", "2"="PC2", "3"="PC3", "4"="PC4"), "PC1"),
           selectInput("component_y","component y",c("1"="PC1", "2"="PC2", "3"="PC3", "4"="PC4"), "PC2"),
           selectInput("show_proportion_of_variance","show proportion of variance",c("yes" = TRUE, "no" = FALSE), "yes"),
           numericInput("dot_size","dot size",4),
           numericInput("dot_transparency","dot transparency",1),
           numericInput("sample_label_size","sample label size",4.5),
           selectInput("legend_position","legend position",c("top" = "top", "right" = "right", "bottom" = "bottom", "left" = "left", "none" = "n"), "bottom"),
           numericInput("plot_height","plot height",400),
           numericInput("plot_width","plot width",400)),
         
         "normexp_correlation_analysis_heatmap" = tagList(
           textInput("distance_method","distance method","spearman"),
           textInput("reorder_function","reorder function","average"),
           textInput("clustering_method","clustering method","average"),
           selectInput("cluster_x","cluster x",c("yes" = TRUE, "no" = FALSE), FALSE),
           selectInput("cluster_y","cluster y",c("yes" = TRUE, "no" = FALSE), FALSE),
           numericInput("plot_height","plot height",600),
           numericInput("plot_width","plot width",750)),
         
         "normexp_most_expressed_genes_violin_plots" = tagList(
           selectInput("sample_group","sample_group",sample_groups, sample_groups[1]),
           selectInput("plot_number","plot_number",c(1:10), 1),
           numericInput("jitter_dot_size","jitter dot size",2),
           numericInput("jitter_dot_width","jitter dot width",0.2),
           textInput("jitter_dot_colour","jitter dot colour","black"),
           ###textInput("violin_labels","violin labels",default_sample_group_labels),
           numericInput("violin_line_thickness","violin line thickness",1),
           numericInput("violin_width","violin width",0.75),
           numericInput("violin_transparency","violin transparency",0.5),
           ###textInput("violin_colours","violin colours",default_sample_group_colours),
           textInput("trim_violin","trim violin",FALSE),
           selectInput("legend_position","legend position",c("top" = "top", "right" = "right", "bottom" = "bottom", "left" = "left", "none" = "n"), "n"),
           numericInput("summary_size","summary size",0.25),
           textInput("x_axis_label","x axis label",""),
           textInput("y_axis_label","y axis label","expression"),
           textInput("summary_colour","summary colour","red"),
           numericInput("plot_height","plot height",350),
           numericInput("plot_width","plot width",350)),
         
         "pde_distribution_of_expression_values" = tagList(
           selectInput("sample","sample",samples, samples[1]),
           numericInput("line_thickness","line thickness",1),
           ###selectInput("legend_position","legend position",c("top" = "top", "right" = "right", "bottom" = "bottom", "left" = "left", "none" = "n"), "n"),
           textInput("x_axis_label","x axis label","expression (log10)"),
           textInput("y_axis_label","y axis label","density"),
           numericInput("transparency","transparency",0.5),
           numericInput("plot_height","plot height",250),
           numericInput("plot_width","plot width",250)),
         
         "pde_pca_contribution_of_components" = tagList(
           selectInput("line_type","line type",c("blank", "solid", "dashed", "dotted", "dotdash", "longdash", "twodash", "1F", "F1", "4C88C488", "12345678"), "solid"),
           textInput("line_colour","line colour","black"),
           textInput("dot_colour","dot colour","red"),
           numericInput("dot_size","dot size",4),
           numericInput("dot_transparency","dot transparency",1),
           textInput("x_axis_label","x axis label","component"),
           textInput("y_axis_label","y axis label","proportion of variance (%)"),
           numericInput("line_size","line size",1),
           numericInput("plot_height","plot height",300),
           numericInput("plot_width","plot width",400)),
         
         "pde_pca_scatter_plot" = tagList(
           selectInput("component_x","component x",c("1"="PC1", "2"="PC2", "3"="PC3", "4"="PC4"), "PC1"),
           selectInput("component_y","component y",c("1"="PC1", "2"="PC2", "3"="PC3", "4"="PC4"), "PC2"),
           selectInput("show_proportion_of_variance","show proportion of variance",c("yes" = TRUE, "no" = FALSE), "yes"),
           numericInput("dot_size","dot size",4),
           numericInput("dot_transparency","dot transparency",1),
           selectInput("legend_position","legend position",c("top" = "top", "right" = "right", "bottom" = "bottom", "left" = "left", "none" = "n"), "bottom"),
           ##textInput("x_axis_label","x axis label","PC1"),
           ##textInput("y_axis_label","y axis label","PC2"),
           numericInput("sample_label_size","sample label size",4.5),
           numericInput("plot_height","plot height",300),
           numericInput("plot_width","plot width",300)),
         
         "pde_correlation_analysis_heatmap" = tagList(
           textInput("distance_method","distance method","spearman"),
           textInput("reorder_function","reorder function","average"),
           textInput("clustering_method","clustering method","average"),
           selectInput("cluster_x","cluster x",c("yes" = TRUE, "no" = FALSE), FALSE),
           selectInput("cluster_y","cluster y",c("yes" = TRUE, "no" = FALSE), FALSE),
           numericInput("plot_height","plot height",600),
           numericInput("plot_width","plot width",750)),
         
         "pde_most_expressed_genes_violin_plots" = tagList(
           selectInput("sample_group","sample_group",sample_groups, sample_groups[1]),
           selectInput("plot_number","plot_number",c(1:10), 1),
           numericInput("jitter_dot_size","jitter dot size",2),
           numericInput("jitter_dot_width","jitter dot width",0.2),
           textInput("jitter_dot_colour","jitter dot colour","black"),
           ###textInput("violin_labels","violin labels",default_sample_group_labels),
           numericInput("violin_line_thickness","violin line thickness",1),
           numericInput("violin_width","violin width",0.75),
           numericInput("violin_transparency","violin transparency",0.5),
           ###textInput("violin_colours","violin colours",default_sample_group_colours),
           textInput("trim_violin","trim violin",FALSE),
           selectInput("legend_position","legend position",c("top" = "top", "right" = "right", "bottom" = "bottom", "left" = "left", "none" = "n"), "n"),
           numericInput("summary_size","summary size",0.25),
           textInput("x_axis_label","x axis label",""),
           textInput("y_axis_label","y axis label","expression"),
           textInput("summary_colour","summary colour","red"),
           numericInput("plot_height","plot height",350),
           numericInput("plot_width","plot width",350)),
         
         "pde_volcano_plot" = tagList(
           numericInput("dot_size","dot size",1.5),
           numericInput("dot_transparency","dot transparency",1),
           textInput("significant_name","significant name","significant"),
           textInput("non_significant_colour","non significant colour",default_non_significant_colour),
           numericInput("data_label_size","data label size",4.5),
           selectInput("legend_position","legend position",c("top" = "top", "right" = "right", "bottom" = "bottom", "left" = "left", "none" = "n"), "bottom"),
           textInput("x_axis_label","x axis label","log2 fold change"),
           textInput("y_axis_label","y axis label","-log10 p-value"),
           textInput("significant_colour","significant colour",default_significant_colour),
           textInput("non_significant_name","non significant name","non-significant"),
           numericInput("plot_height","plot height",500),
           numericInput("plot_width","plot width",600)),
         
         "pde_ma_plot" = tagList(
           textInput("non_significant_name","non significant name","non-significant"),
           textInput("significant_name","significant name","significant"),
           textInput("non_significant_colour","non significant colour",default_non_significant_colour),
           textInput("significant_colour","significant colour",default_significant_colour),
           numericInput("dot_size","dot size",1.5),
           numericInput("dot_transparency","dot transparency",1),
           selectInput("legend_position","legend position",c("top" = "top", "right" = "right", "bottom" = "bottom", "left" = "left", "none" = "n"), "bottom"),
           numericInput("data_label_size","data label size",4.5),
           textInput("x_axis_label","x axis label","mean expression (log10)"),
           textInput("y_axis_label","y axis label","log2 fold change"),
           numericInput("plot_height","plot height",500),
           numericInput("plot_width","plot width",600)),
         
         "pde_number_of_significant_genes_bar_chart" = tagList(
           ##textInput("bar_colours","bar colours",default_two_tone_greyscale),
           numericInput("bar_outline_size","bar outline size",1),
           numericInput("data_label_size","data label size",5),
           ##textInput("direction_labels","direction labels",c("up","down")),
           selectInput("legend_position","legend position",c("top" = "top", "right" = "right", "bottom" = "bottom", "left" = "left", "none" = "n"), "bottom"),
           textInput("x_axis_label","x axis label",""),
           textInput("y_axis_label","y axis label","number of significant genes"),
           ##textInput("comparison_labels","comparison labels",default_comparison_labels),
           numericInput("plot_height","plot height",350),
           numericInput("plot_width","plot width",350)),
         
         "pde_significant_genes_heatmap" = tagList(
           selectInput("cluster","cluster",c("yes" = TRUE, "no" = FALSE), "no"),
           ###textInput("colours","colours",default_three_tone_heatmap_colours),
           textInput("distance_method","distance method","spearman"),
           textInput("reorder_function","reorder function","average"),
           textInput("clustering_method","clustering method","average"),
           selectInput("cluster_x","cluster x",c("yes" = TRUE, "no" = FALSE), FALSE),
           selectInput("cluster_y","cluster y",c("yes" = TRUE, "no" = FALSE), TRUE),
           numericInput("plot_height","plot height",750),
           numericInput("plot_width","plot width",500)),
         
         "pde_most_differential_genes_violin_plots" = tagList(
           selectInput("direction_type","direction type", c("most upregulated by p value" = "most_upregulated_by_p_value", "most upregulated by log2fold" = "most_upregulated_by_log2fold", "most downregulated by p value" = "most_downregulated_by_p_value" ,"most downregulated by log2fold" = "most_downregulated_by_log2fold"), "most_upregulated_by_p_value"),
           selectInput("plot_number","plot number",c(1:10), 1),
           numericInput("jitter_dot_size","jitter dot size",2),
           numericInput("jitter_dot_width","jitter dot width",0.2),
           textInput("jitter_dot_colour","jitter dot colour","black"),
           ###textInput("violin_labels","violin labels",default_sample_group_labels),
           numericInput("violin_line_thickness","violin line thickness",1),
           numericInput("violin_width","violin width",0.75),
           numericInput("violin_transparency","violin transparency",0.5),
           ###textInput("violin_colours","violin colours",default_sample_group_colours),
           textInput("trim_violin","trim violin",FALSE),
           selectInput("legend_position","legend position",c("top" = "top", "right" = "right", "bottom" = "bottom", "left" = "left", "none" = "n"), "n"),
           numericInput("summary_size","summary size",0.25),
           textInput("x_axis_label","x axis label",""),
           textInput("y_axis_label","y axis label","expression"),
           textInput("summary_colour","summary colour","red"),
           numericInput("plot_height","plot height",300),
           numericInput("plot_width","plot width",300)),
         
         "pde_spatial_enrichment_distribution_plots" = tagList(
           selectInput("chromosome","select chromosome", sort(unique(PDE_annotated$chromosome)), sort(unique(PDE_annotated$chromosome))[1]),
           selectInput("spatial_enrichment_type","plot type",c("fold" = "FOLD", "density" = "DENSITY"), "FOLD"),
           numericInput("dot_size","dot size",1.5),
           numericInput("dot_transparency","dot transparency",1),
           textInput("significant_name","significant name","significant"),
           textInput("non_significant_name","non significant name","non-significant"),
           textInput("significant_colour","significant colour",default_significant_colour),
           textInput("non_significant_colour","non significant colour",default_non_significant_colour),
           numericInput("data_label_size","data label size",4.5),
           selectInput("legend_position","legend position",c("top" = "top", "right" = "right", "bottom" = "bottom", "left" = "left", "none" = "n"), "bottom"),
           textInput("x_axis_label","x axis label","gene location"),
           textInput("y_axis_label","y axis label","log2 fold change"),
           numericInput("density_curve_line_thickness","density curve line thickness",0),
           numericInput("density_curve_transparency","density curve transparency",0.5),
           numericInput("plot_height","plot height",300),
           numericInput("plot_width","plot width",750)),
         
         "pde_hypergeometric_enriched_gene_sets_barcharts" = tagList(
           selectInput("hgsea_database","select database",hgsea_databases, hgsea_databases[1]),
           selectInput("direction_type","choose gene list",c("all significant genes" = "all","upregulated genes" = "up","downregulated genes" = "down"), "all"),
           numericInput("bar_transparency","bar transparency",0.75),
           numericInput("bar_outline_size","bar outline size",1),
           textInput("significant_name","significant name","significant"),
           textInput("non_significant_colour","non significant colour",default_non_significant_colour),
           numericInput("data_label_size","data label size",5),
           selectInput("legend_position","legend position",c("top" = "top", "right" = "right", "bottom" = "bottom", "left" = "left", "none" = "n"), "bottom"),
           textInput("x_axis_label","x axis label","-log10 p-value"),
           textInput("y_axis_label","y axis label",""),
           textInput("significant_colour","significant colour",default_significant_colour),
           textInput("non_significant_name","non significant name","non-significant"),
           numericInput("plot_height","plot height",350),
           numericInput("plot_width","plot width",1000)),
         
         "pde_hypergeometric_enriched_gene_sets_boxplot" = tagList(
           selectInput("hgsea_database","select database",hgsea_databases, hgsea_databases[1]),
           selectInput("direction_type","choose gene list",c("all significant genes" = "all","upregulated genes" = "up","downregulated genes" = "down"), "all"),
           selectInput("plot_number","plot number",c(1:10), 1),
           ##textInput("box_colours","box colours",default_sample_group_colours),
           numericInput("box_line_thickness","box line thickness",0.75),
           numericInput("box_transparency","box transparency",0.75),
           ##textInput("box_labels","box labels",default_sample_group_labels),
           selectInput("legend_position","legend position",c("top" = "top", "right" = "right", "bottom" = "bottom", "left" = "left", "none" = "n"), "right"),
           textInput("x_axis_label","x axis label",""),
           textInput("y_axis_label","y axis label","expression (z-score)"),
           numericInput("plot_height","plot height",250),
           numericInput("plot_width","plot width",1000)),
         
         "pde_hypergeometric_enriched_gene_sets_network_plots" = tagList(
           selectInput("hgsea_database","select database",hgsea_databases, hgsea_databases[1]),
           selectInput("direction_type","choose gene list",c("all significant genes" = "all","upregulated genes" = "up","downregulated genes" = "down"), "all"),
           numericInput("node_inner_max_size","node inner max size",20),
           numericInput("node_outer_max_size","node outer max size",25),
           numericInput("node_label_size","node label size",3),
           ##textInput("node_colours","node colours",default_two_tone_network_node_colours),
           numericInput("edge_width","edge width",2),
           textInput("edge_colour","edge colour",default_network_edge_colour),
           numericInput("edge_transparency","edge transparency",0.5),
           numericInput("plot_height","plot height",1000),
           numericInput("plot_width","plot width",1500)),
         
         "pde_hypergeometric_underenriched_gene_sets_barcharts" = tagList(
           selectInput("hgsea_database","select database",hgsea_databases, hgsea_databases[1]),
           selectInput("direction_type","choose gene list",c("all significant genes" = "all","upregulated genes" = "up","downregulated genes" = "down"), "all"),
           numericInput("bar_transparency","bar transparency",0.75),
           numericInput("bar_outline_size","bar outline size",1),
           textInput("significant_name","significant name","significant"),
           textInput("non_significant_colour","non significant colour",default_non_significant_colour),
           numericInput("data_label_size","data label size",5),
           selectInput("legend_position","legend position",c("top" = "top", "right" = "right", "bottom" = "bottom", "left" = "left", "none" = "n"), "bottom"),
           textInput("x_axis_label","x axis label","-log10 p-value"),
           textInput("y_axis_label","y axis label",""),
           textInput("significant_colour","significant colour",default_significant_colour),
           textInput("non_significant_name","non significant name","non-significant"),
           numericInput("plot_height","plot height",350),
           numericInput("plot_width","plot width",1000)),
         
         "pde_IPA_upstream_regulators_bar_charts" = tagList(
           selectInput("ureg_database","select database",ureg_databases, ureg_databases[1]),
           selectInput("direction_type","choose test",c("activation" = "activated","inhibition" = "inhibited","enrichment" = "enriched"), "activated"),
           numericInput("bar_transparency","bar transparency",0.75),
           numericInput("bar_outline_size","bar outline size",1),
           textInput("significant_name","significant name","significant"),
           textInput("non_significant_colour","non significant colour",default_non_significant_colour),
           numericInput("data_label_size","data label size",5),
           selectInput("legend_position","legend position",c("top" = "top", "right" = "right", "bottom" = "bottom", "left" = "left", "none" = "n"), "bottom"),
           textInput("x_axis_label","x axis label","-log10 p-value"),
           textInput("y_axis_label","y axis label",""),
           textInput("significant_colour","significant colour",default_significant_colour),
           textInput("non_significant_name","non significant name","non-significant"),
           numericInput("plot_height","plot height",350),
           numericInput("plot_width","plot width",500)),
         
         "pde_IPA_upstream_regulators_boxplots" = tagList(
           selectInput("ureg_database","select database",ureg_databases, ureg_databases[1]),
           selectInput("direction_type","choose test",c("activation" = "activated","inhibition" = "inhibited","enrichment" = "enriched"), "activated"),
           selectInput("plot_number","plot number",c(1:10), 1),
           ##textInput("box_colours","box colours",default_sample_group_colours),
           numericInput("box_line_thickness","box line thickness",0.75),
           numericInput("box_transparency","box transparency",0.75),
           ##textInput("box_labels","box labels",default_sample_group_labels),
           selectInput("legend_position","legend position",c("top" = "top", "right" = "right", "bottom" = "bottom", "left" = "left", "none" = "n"), "right"),
           textInput("x_axis_label","x axis label",""),
           textInput("y_axis_label","y axis label","expression (z-score)"),
           numericInput("plot_height","plot height",250),
           numericInput("plot_width","plot width",1000)),
         
         "pde_IPA_upstream_regulators_network_plots" = tagList(
           selectInput("ureg_database","select database",ureg_databases, ureg_databases[1]),
           selectInput("direction_type","choose test",c("activation / inhibition" = FALSE,"enrichment" = TRUE), FALSE),
           numericInput("node_inner_max_size","node inner max size",40),
           numericInput("node_outer_max_size","node outer max size",50),
           numericInput("node_label_size","node label size",3),
           ##textInput("node_colours","node colours",default_two_tone_network_node_colours),
           ##textInput("activated_node_colours","activated node colours",default_four_tone_network_node_colours_high),
           ##textInput("inhibited_node_colours","inhibited node colours",default_four_tone_network_node_colours_low),
           numericInput("edge_width","edge width",4),
           textInput("edge_colour","edge colour",default_network_edge_colour),
           numericInput("edge_transparency","edge transparency",0.5),
           numericInput("plot_height","plot height",1000),
           numericInput("plot_width","plot width",1500)),
         
         "mpde_distribution_of_expression_values" = tagList(
           selectInput("sample","sample",samples, samples[1]),
           numericInput("line_thickness","line thickness",1),
           selectInput("legend_position","legend position",c("top" = "top", "right" = "right", "bottom" = "bottom", "left" = "left", "none" = "n"), "n"),
           textInput("x_axis_label","x axis label","expression (log10)"),
           textInput("y_axis_label","y axis label","density"),
           numericInput("transparency","transparency",0.5),
           numericInput("plot_height","plot height",250),
           numericInput("plot_width","plot width",250)),
         
         "mpde_pca_contribution_of_components" = tagList(
           selectInput("line_type","line type",c("blank", "solid", "dashed", "dotted", "dotdash", "longdash", "twodash", "1F", "F1", "4C88C488", "12345678"), "solid"),
           textInput("line_colour","line colour","black"),
           textInput("dot_colour","dot colour","red"),
           numericInput("dot_size","dot size",4),
           numericInput("dot_transparency","dot transparency",1),
           textInput("x_axis_label","x axis label","component"),
           textInput("y_axis_label","y axis label","proportion of variance (%)"),
           numericInput("line_size","line size",1),
           numericInput("plot_height","plot height",300),
           numericInput("plot_width","plot width",400)),
         
         "mpde_pca_scatter_plot" = tagList(
           selectInput("component_x","component x",c("1"="PC1", "2"="PC2", "3"="PC3", "4"="PC4"), "PC1"),
           selectInput("component_y","component y",c("1"="PC1", "2"="PC2", "3"="PC3", "4"="PC4"), "PC2"),
           selectInput("show_proportion_of_variance","show proportion of variance",c("yes" = TRUE, "no" = FALSE), "yes"),
           numericInput("dot_size","dot size",4),
           numericInput("dot_transparency","dot transparency",1),
           selectInput("legend_position","legend position",c("top" = "top", "right" = "right", "bottom" = "bottom", "left" = "left", "none" = "n"), "bottom"),
           ##textInput("x_axis_label","x axis label","PC1"),
           ##textInput("y_axis_label","y axis label","PC2"),
           numericInput("sample_label_size","sample label size",4.5),
           numericInput("plot_height","plot height",400),
           numericInput("plot_width","plot width",400)),
         
         "mpde_correlation_analysis_heatmap" = tagList(
           textInput("distance_method","distance method","spearman"),
           textInput("reorder_function","reorder function","average"),
           textInput("clustering_method","clustering method","average"),
           selectInput("cluster_x","cluster x",c("yes" = TRUE, "no" = FALSE), FALSE),
           selectInput("cluster_y","cluster y",c("yes" = TRUE, "no" = FALSE), FALSE),
           numericInput("plot_height","plot height",600),
           numericInput("plot_width","plot width",750)),
         
         "mpde_most_expressed_genes_violin_plots" = tagList(
           selectInput("sample_group","sample_group",sample_groups, sample_groups[1]),
           selectInput("plot_number","plot_number",c(1:10), 1),
           numericInput("jitter_dot_size","jitter dot size",2),
           numericInput("jitter_dot_width","jitter dot width",0.2),
           textInput("jitter_dot_colour","jitter dot colour","black"),
           ###textInput("violin_labels","violin labels",default_sample_group_labels),
           numericInput("violin_line_thickness","violin line thickness",1),
           numericInput("violin_width","violin width",0.75),
           numericInput("violin_transparency","violin transparency",0.5),
           ###textInput("violin_colours","violin colours",default_sample_group_colours),
           textInput("trim_violin","trim violin",FALSE),
           selectInput("legend_position","legend position",c("top" = "top", "right" = "right", "bottom" = "bottom", "left" = "left", "none" = "n"), "n"),
           numericInput("summary_size","summary size",0.25),
           textInput("x_axis_label","x axis label",""),
           textInput("y_axis_label","y axis label","expression"),
           textInput("summary_colour","summary colour","red"),
           numericInput("plot_height","plot height",350),
           numericInput("plot_width","plot width",350)),
         
         "mpde_number_of_significant_genes_bar_chart" = tagList(
           ###textInput("bar_colours","bar colours",default_two_tone_greyscale),
           numericInput("bar_outline_size","bar outline size",1),
           numericInput("data_label_size","data label size",5),
           ###textInput("direction_labels","direction labels",c("up","down") ),
           selectInput("legend_position","legend position",c("top" = "top", "right" = "right", "bottom" = "bottom", "left" = "left", "none" = "n"), "bottom"),
           textInput("x_axis_label","x axis label",""),
           textInput("y_axis_label","y axis label","number of significant genes"),
           ###textInput("comparison_labels","comparison labels",default_comparison_labels),
           numericInput("plot_height","plot height",500),
           numericInput("plot_width","plot width",750)),
         
         "mpde_significant_genes_heatmap" = tagList(
           selectInput("sig_any_all","significance",c("must be sig in all comparisons" = "all", "can be sig in any one comparison" = "any"), "any"),
           ##textInput("colours","colours",default_three_tone_heatmap_colours),
           textInput("distance_method","distance method","spearman"),
           textInput("reorder_function","reorder function","average"),
           textInput("clustering_method","clustering method","average"),
           selectInput("cluster_x","cluster x",c("yes" = TRUE, "no" = FALSE), "no"),
           selectInput("cluster_y","cluster y",c("yes" = TRUE, "no" = FALSE), "no"),
           numericInput("plot_height","plot height",750),
           numericInput("plot_width","plot width",500)),
         
         "mpde_fold_vs_fold_scatterplots" = tagList(
           selectInput("comparison_1","comparison 1",comparisons, comparisons[1]),
           selectInput("comparison_2","comparison 2",comparisons, comparisons[2]),
           ##textInput("colours","colours",c(default_significant_both_colour,default_significant_a_colour,default_significant_b_colour,default_non_significant_colour)),
           numericInput("dot_size","dot size",1.5),
           numericInput("dot_transparency","dot transparency",1),
           numericInput("data_label_size","data label size",4.5),
           selectInput("legend_position","legend position",c("top" = "top", "right" = "right", "bottom" = "bottom", "left" = "left", "none" = "n"), "bottom"),
           numericInput("plot_height","plot height",600),
           numericInput("plot_width","plot width",600)),
         
         "mpde_differential_expression_signature_metagene_violin_plot" = tagList(
           selectInput("signature_number","select signature",c(1:nrow(signature_summary)), 1),
           numericInput("jitter_dot_size","jitter dot size",2),
           numericInput("jitter_dot_width","jitter dot width",0.2),
           textInput("jitter_dot_colour","jitter dot colour","black"),
           ###textInput("violin_labels","violin labels",default_sample_group_labels),
           numericInput("violin_line_thickness","violin line thickness",1),
           numericInput("violin_width","violin width",0.75),
           numericInput("violin_transparency","violin transparency",0.5),
           ###textInput("violin_colours","violin colours",default_sample_group_colours),
           textInput("trim_violin","trim violin",FALSE),
           selectInput("legend_position","legend position",c("top" = "top", "right" = "right", "bottom" = "bottom", "left" = "left", "none" = "n"), "n"),
           numericInput("summary_size","summary size",0.25),
           textInput("x_axis_label","x axis label",""),
           textInput("y_axis_label","y axis label","expression"),
           textInput("summary_colour","summary colour","red"),
           numericInput("plot_height","plot height",350),
           numericInput("plot_width","plot width",350)),
         
         "mpde_differential_expression_signatures_heatmap" = tagList(
           selectInput("signature_number","select signature",c(1:nrow(signature_summary)), 1),
           ##textInput("colours","colours",default_three_tone_heatmap_colours),
           textInput("distance_method","distance method","spearman"),
           textInput("reorder_function","reorder function","average"),
           textInput("clustering_method","clustering method","average"),
           selectInput("cluster_x","cluster x",c("yes" = TRUE, "no" = FALSE), FALSE),
           selectInput("cluster_y","cluster y",c("yes" = TRUE, "no" = FALSE), FALSE),
           numericInput("plot_height","plot height",750),
           numericInput("plot_width","plot width",500)),
         
         "mpde_differential_expression_signature_hypergeometric_gene_sets_barchart" = tagList(
           selectInput("hgsea_database","select database",hgsea_databases, hgsea_databases[1]),
           selectInput("signature_number","select signature",c(1:nrow(signature_summary)), 1),
           numericInput("bar_transparency","bar transparency",0.75),
           numericInput("bar_outline_size","bar outline size",1),
           textInput("significant_name","significant name","significant"),
           ##textInput("non_significant_colour","non significant colour",default_non_significant_colour),
           numericInput("data_label_size","data label size",5),
           selectInput("legend_position","legend position",c("top" = "top", "right" = "right", "bottom" = "bottom", "left" = "left", "none" = "n"), "bottom"),
           textInput("x_axis_label","x axis label","-log10 p-value"),
           textInput("y_axis_label","y axis label",""),
           ##textInput("significant_colour","significant colour",default_significant_colour),
           textInput("non_significant_name","non significant name","non-significant"),
           numericInput("plot_height","plot height",350),
           numericInput("plot_width","plot width",1000))
         
  )
})

plotInput <- reactive({
  if (is.null(input$plot_type))
    return()
  
  # set theme?
  theme_SL2 <- function () {
    theme_bw() %+replace%
      theme(
        plot.background = element_rect(fill = input$th_plot_fill, colour = input$th_plot_colour),
        panel.grid = element_line(colour = input$th_panel_grid_colour, linetype = input$th_panel_grid_linetype, size = input$th_grid_size),
        panel.background = element_rect(fill = input$th_panel_background_fill , colour = input$th_panel_background_colour , linetype = input$th_panel_background_linetype, size = input$th_panel_size),
        panel.border = element_rect(colour = "black", fill=NA, size=1),
        legend.background = element_rect(fill=input$th_legend_fill, colour=input$th_legend_colour),
        legend.key = element_rect(fill=input$th_legend_key_fill, colour=input$th_legend_key_colour),
        plot.title = element_text(size = input$th_title_size, margin = margin(r = 10),hjust=0.5,vjust=0.5, family=input$th_font_family, face=input$th_font_face),
        title = element_text(size = input$th_title_size, margin = margin(r = 10),hjust=0.5,vjust=0.5, family=input$th_font_family, face=input$th_font_face),
        axis.text.y = element_text(size = input$th_axis_text_size, margin = margin(r = 5),hjust=1,vjust=0.5, family=input$th_font_family, face=input$th_font_face, colour=input$th_text_colour),
        axis.text.x = element_text(size = input$th_axis_text_size, margin = margin(t = 5),hjust=0.5,vjust=1, family=input$th_font_family, face=input$th_font_face, colour=input$th_text_colour),
        axis.title.y = element_text(size = input$th_axis_title_size, margin = margin(r = 10),angle = 90,hjust=0.5,vjust=0.5, family=input$th_font_family, face=input$th_font_face),
        axis.title.x = element_text(size = input$th_axis_title_size, margin = margin(t = 10),hjust=0.5,vjust=1, family=input$th_font_family, face=input$th_font_face),
        legend.text=element_text(size=14, family=input$th_font_family, face=input$th_font_face),
        legend.title=element_blank(),
        legend.key.size=unit(2.5,"line"),
        plot.margin=unit(c(0.4,0.4,0.4,0.4), "cm"
        )
      )
  }
  
  
  if (input$plot_type == "normexp_distribution_of_expression_values") 
  {
    sample_index = match(input$sample,samples)
    plot_sample = samples[plot_sample_index]
    plot_colour = unlist(default_samples_colours[1])[sample_index]
    ggp = make_distribution_of_expression_values_plot(input$sample,plot_colour,input$transparency,input$line_thickness,input$x_axis_label,input$y_axis_label,input$legend_position)
    print(ggp)
  }
  
  else if (input$plot_type == "normexp_pca_contribution_of_components") 
  {
    ggp = make_PCA_contribution_of_components_plot(input$x_axis_label,input$y_axis_label,input$dot_size,input$dot_transparency,input$dot_colour,input$line_type,input$line_colour,input$line_size)
    print(ggp)
  }
  
  else if (input$plot_type == "normexp_pca_scatter_plot") 
  {
    column_index = match(input$ss_column,sample_sheet_column_names)
    print(column_index)
    print(input$ss_column)
    
    plot_sample_groupings = unlist(sample_groupings_by_SS_column[column_index])
    plot_sample_groupings = factor(plot_sample_groupings, levels = sample_groups)
    plot_sample_group_colours = unlist(default_sample_group_colours_by_SS_column[column_index])
    
    plot_sample_group_labels = default_sample_group_labels
    plot_sample_labels = default_sample_labels
    
    x_axis_label = input$component_x
    y_axis_label = input$component_y
    
    ggp = make_PCA_scatterplot(plot_sample_groupings,input$component_x,input$component_y,x_axis_label,y_axis_label,plot_sample_group_colours,plot_sample_group_labels,plot_sample_labels,input$dot_size,input$dot_transparency,input$legend_position,input$sample_label_size,input$show_proportion_of_variance)
    print(ggp)
  }
  
  else if (input$plot_type == "normexp_correlation_analysis_heatmap") 
  {
    colours = default_three_tone_heatmap_colours
    sample_names = default_sample_labels
    
    ggp = make_correlation_analysis_heatmap(colours,sample_names,input$cluster_x,input$cluster_y,input$distance_method,input$clustering_method,input$reorder_function)
    print(ggp)
  }
  
  else if (input$plot_type == "normexp_most_expressed_genes_violin_plots") 
  {
    violin_colours = default_sample_group_colours 
    violin_labels = default_sample_group_labels
    top_10_genes = get_top_10_genes_by_mean_expression(match(input$sample_group,sample_groups))
    gene = top_10_genes[as.numeric(input$plot_number)]
    
    ggp = make_gene_expression_violin_plot(normexp_matrix_transposed,gene,input$violin_transparency,input$violin_width,input$violin_line_thickness,violin_colours,violin_labels,input$trim_violin,input$jitter_dot_size,input$jitter_dot_colour,input$jitter_dot_width,input$summary_colour,input$summary_size,input$x_axis_label,input$y_axis_label,input$legend_position)
    print(ggp)
  }
  
  else if (input$plot_type == "pde_distribution_of_expression_values") 
  {
    sample_index = match(input$sample,samples)
    plot_colour = default_samples_colours[sample_index]
    print(plot_colour)
    print(input$sample)
    ggp = make_distribution_of_expression_values_plot(input$sample,plot_colour,input$transparency,input$line_thickness,input$x_axis_label,input$y_axis_label,input$legend_position)
    print(ggp)
  }
  
  else if (input$plot_type == "pde_pca_contribution_of_components") 
  {
    ggp = make_PCA_contribution_of_components_plot(input$x_axis_label,input$y_axis_label,input$dot_size,input$dot_transparency,input$dot_colour,input$line_type,input$line_colour,input$line_size)
    print(ggp)
  }
  
  else if (input$plot_type == "pde_pca_scatter_plot") 
  {
    plot_sample_group_colours = default_sample_group_colours
    plot_sample_group_labels = default_sample_group_labels
    plot_sample_labels = default_sample_labels
    plot_sample_groupings = sample_groupings
    
    x_axis_label = input$component_x
    y_axis_label = input$component_y
    
    ggp = make_PCA_scatterplot(plot_sample_groupings,input$component_x,input$component_y,x_axis_label,y_axis_label,plot_sample_group_colours,plot_sample_group_labels,plot_sample_labels,input$dot_size,input$dot_transparency,input$legend_position,input$sample_label_size,input$show_proportion_of_variance)
    print(ggp)
  }
  
  else if (input$plot_type == "pde_correlation_analysis_heatmap") 
  {
    colours = default_three_tone_heatmap_colours
    sample_names = default_sample_labels
    
    ggp = make_correlation_analysis_heatmap(colours,sample_names,input$cluster_x,input$cluster_y,input$distance_method,input$clustering_method,input$reorder_function)
    print(ggp)
  }
  
  else if (input$plot_type == "pde_most_expressed_genes_violin_plots") 
  {
    violin_colours = default_sample_group_colours 
    violin_labels = default_sample_group_labels
    top_10_genes = get_top_10_genes_by_mean_expression(match(input$sample_group,sample_groups))
    gene = top_10_genes[as.numeric(input$plot_number)]
    
    ggp = make_gene_expression_violin_plot(normexp_matrix_transposed,gene,input$violin_transparency,input$violin_width,input$violin_line_thickness,violin_colours,violin_labels,input$trim_violin,input$jitter_dot_size,input$jitter_dot_colour,input$jitter_dot_width,input$summary_colour,input$summary_size,input$x_axis_label,input$y_axis_label,input$legend_position)
    print(ggp)
  }
  
  else if (input$plot_type == "pde_volcano_plot") 
  {
    ggp = make_volcano_plot(input$non_significant_colour,input$significant_colour,input$dot_size,input$dot_transparency,input$significant_name,input$non_significant_name,input$x_axis_label,input$y_axis_label,input$legend_position,input$data_label_size)
    print(ggp)
  }
  
  else if (input$plot_type == "pde_ma_plot") 
  {
    ggp = make_MA_plot(input$non_significant_colour,input$significant_colour,input$dot_size,input$dot_transparency,input$significant_name,input$non_significant_name,input$x_axis_label,input$y_axis_label,input$legend_position,input$data_label_size)
    print(ggp)
  }
  
  else if (input$plot_type == "pde_number_of_significant_genes_bar_chart") 
  {
    comparison_labels = default_comparison_labels
    direction_labels = c("up","down")
    bar_colours = default_two_tone_greyscale
    
    ggp = make_number_of_significant_genes_barchart(input$x_axis_label,input$y_axis_label,comparison_labels,direction_labels,bar_colours,input$legend_position,input$data_label_size,input$bar_outline_size)
    print(ggp)
  }
  
  else if (input$plot_type == "pde_significant_genes_heatmap") 
  {
    colours = default_three_tone_heatmap_colours
    sample_names = default_sample_labels
    
    ggp = make_significant_genes_heatmap(normexp_matrix_sig_scaled,colours,sample_names,input$cluster_x,input$cluster_y,input$distance_method,input$clustering_method,input$reorder_function)
    print(ggp)
  }
  
  else if (input$plot_type == "pde_most_differential_genes_violin_plots") 
  {
    violin_colours = default_sample_group_colours
    violin_labels = default_sample_group_labels
    
    if (input$direction_type == "most_downregulated_by_log2fold")
    {
      top_10_genes = get_top_10_differential_genes(FALSE,"log2fold")
    }
    else if (input$direction_type == "most_downregulated_by_p_value")
    {
      top_10_genes = get_top_10_differential_genes(FALSE,"p")
    }
    else if (input$direction_type == "most_upregulated_by_log2fold")
    {
      top_10_genes = get_top_10_differential_genes(TRUE,"log2fold")
    }   
    else if (input$direction_type == "most_upregulated_by_p_value")
    {
      top_10_genes = get_top_10_differential_genes(TRUE,"p")
    }   
    
    gene = top_10_genes[as.numeric(input$plot_number)]
    
    ggp = make_gene_expression_violin_plot(normexp_matrix_transposed,gene,input$violin_transparency,input$violin_width,input$violin_line_thickness,violin_colours,violin_labels,input$trim_violin,input$jitter_dot_size,input$jitter_dot_colour,input$jitter_dot_width,input$summary_colour,input$summary_size,input$x_axis_label,input$y_axis_label,input$legend_position)
    print(ggp)
  }
  
  else if (input$plot_type == "pde_spatial_enrichment_distribution_plots") 
  { 
    if (input$spatial_enrichment_type == "FOLD")
    {
      ggp = make_spatial_enrichment_fold_distribution_plot(input$chromosome,input$non_significant_colour,input$significant_colour,input$dot_size,input$dot_transparency,input$significant_name,input$non_significant_name,input$x_axis_label,input$y_axis_label,input$legend_position,input$data_label_size)
    }
    else
    {
      ggp = make_spatial_enrichment_gene_distribution_plot(input$chromosome,input$non_significant_colour,input$significant_colour,input$density_curve_transparency,input$density_curve_line_thickness,input$significant_name,input$non_significant_name,input$x_axis_label,input$y_axis_label,input$legend_position)
    }
    print(ggp)
  }
  
  else if (input$plot_type == "pde_hypergeometric_enriched_gene_sets_barcharts") 
  {
    if (input$direction_type == "all")
    {
      temp1 = paste(input$hgsea_database,"_all_gene_sets",sep="")
      temp2 = paste(input$hgsea_database,"_all_signficant_genes_enriched_gene_sets",sep="")
    }
    else if (input$direction_type == "up")
    {
      temp1 = paste(input$hgsea_database,"_upregulated_gene_sets",sep="")
      temp2 = paste(input$hgsea_database,"_upregulated_enriched_gene_sets",sep="") 
    }
    else if (input$direction_type == "down")
    {
      temp1 = paste(input$hgsea_database,"_downregulated_gene_sets",sep="")
      temp2 = paste(input$hgsea_database,"_downregulated_enriched_gene_sets",sep="")   
    }  
    
    top_10_gene_sets = get_top10_hypergeometric_gene_sets_by_p_value(get(temp1),get(temp2),"enrichment")  
    ggp <- make_hypergeometric_gene_sets_bar_chart(top_10_gene_sets,input$x_axis_label,input$y_axis_label,input$non_significant_colour,input$significant_colour,input$bar_outline_size,input$bar_transparency,input$legend_position,input$significant_name,input$non_significant_name,input$data_label_size)
    print(ggp)
  }
  
  else if (input$plot_type == "pde_hypergeometric_enriched_gene_sets_boxplot") 
  {
    if (input$direction_type == "all")
    {
      temp1 = paste(input$hgsea_database,"_all_gene_sets",sep="")
      temp2 = paste(input$hgsea_database,"_all_signficant_genes_enriched_gene_sets",sep="")
    }
    else if (input$direction_type == "up")
    {
      temp1 = paste(input$hgsea_database,"_upregulated_gene_sets",sep="")
      temp2 = paste(input$hgsea_database,"_upregulated_enriched_gene_sets",sep="") 
    }
    else if (input$direction_type == "down")
    {
      temp1 = paste(input$hgsea_database,"_downregulated_gene_sets",sep="")
      temp2 = paste(input$hgsea_database,"_downregulated_enriched_gene_sets",sep="")   
    }  
    
    top_10_gene_sets = get_top10_hypergeometric_gene_sets_by_p_value(get(temp1),get(temp2),"enrichment")  
    gene_set = top_10_gene_sets[as.numeric(input$plot_number),]
    plot_title = gene_set[["gene_set"]]
    
    box_colours = default_sample_group_colours 	
    box_labels = default_sample_group_labels
    
    ggp = make_hypergeometric_gene_set_boxplot(gene_set,plot_title,input$box_transparency,input$box_line_thickness,box_colours,box_labels,input$x_axis_label,input$y_axis_label,input$legend_position)
    print(ggp)
  }
  
  else if (input$plot_type == "pde_hypergeometric_enriched_gene_sets_network_plots") 
  {
    if (input$direction_type == "all")
    {
      temp1 = paste(input$hgsea_database,"_all_significant_gene_sets_edges",sep="")
      temp2 = paste(input$hgsea_database,"_all_significant_gene_sets_nodes",sep="")
    }
    else if (input$direction_type == "up")
    {
      temp1 = paste(input$hgsea_database,"_upregulated_gene_sets_edges",sep="")
      temp2 = paste(input$hgsea_database,"_upregulated_gene_sets_nodes",sep="") 
    }
    else if (input$direction_type == "down")
    {
      temp1 = paste(input$hgsea_database,"_downregulated_gene_sets_edges",sep="")
      temp2 = paste(input$hgsea_database,"_downregulated_gene_sets_nodes",sep="")   
    }
    
    node_colours = default_two_tone_network_node_colours
    
    ggp = make_hypergeometric_gene_set_network_plot(get(temp1),get(temp2),node_colours,input$node_outer_max_size,input$node_inner_max_size,input$node_label_size,input$edge_colour,input$edge_transparency,input$edge_width)
    print(ggp)
  }
  
  else if (input$plot_type == "pde_hypergeometric_underenriched_gene_sets_barcharts") 
  {
    if (input$direction_type == "all")
    {
      temp1 = paste(input$hgsea_database,"_all_gene_sets",sep="")
      temp2 = paste(input$hgsea_database,"_all_signficant_genes_enriched_gene_sets",sep="")
    }
    else if (input$direction_type == "up")
    {
      temp1 = paste(input$hgsea_database,"_upregulated_gene_sets",sep="")
      temp2 = paste(input$hgsea_database,"_upregulated_enriched_gene_sets",sep="") 
    }
    else if (input$direction_type == "down")
    {
      temp1 = paste(input$hgsea_database,"_downregulated_gene_sets",sep="")
      temp2 = paste(input$hgsea_database,"_downregulated_enriched_gene_sets",sep="")   
    }  
    
    top_10_gene_sets = get_top10_hypergeometric_gene_sets_by_p_value(get(temp1),get(temp2),"underenrichment")  
    ggp <- make_hypergeometric_gene_sets_bar_chart(top_10_gene_sets,input$x_axis_label,input$y_axis_label,input$non_significant_colour,input$significant_colour,input$bar_outline_size,input$bar_transparency,input$legend_position,input$significant_name,input$non_significant_name,input$data_label_size)
    print(ggp)
  }
  
  else if (input$plot_type == "pde_IPA_upstream_regulators_bar_charts") 
  {
    if (input$direction_type == "enriched")
    {
      top_10_upstream_regulators = get_top10_IPA_upstream_regulators_function(get(paste(input$ureg_database,"_all_gene_sets",sep="")),get(paste(input$ureg_database,"_enriched_gene_sets",sep="")),"enriched")
      ggp = make_hypergeometric_gene_sets_bar_chart(top_10_upstream_regulators,input$x_axis_label,input$y_axis_label,input$non_significant_colour,input$significant_colour,input$bar_outline_size,input$bar_transparency,input$legend_position,input$significant_name,input$non_significant_name,input$data_label_size)
      
    }
    if (input$direction_type == "activated")
    {
      top_10_upstream_regulators = get_top10_IPA_upstream_regulators_function(get(paste(input$ureg_database,"_all_gene_sets",sep="")),get(paste(input$ureg_database,"_enriched_gene_sets",sep="")),"activated")
      ggp = make_IPA_upstream_regulators_bar_chart(top_10_upstream_regulators,input$x_axis_label,input$y_axis_label,input$non_significant_colour,input$significant_colour,input$bar_outline_size,input$bar_transparency,input$legend_position,input$significant_name,input$non_significant_name,input$data_label_size, "activated")
    }
    if (input$direction_type == "inhibited")
    {
      top_10_upstream_regulators = get_top10_IPA_upstream_regulators_function(get(paste(input$ureg_database,"_all_gene_sets",sep="")),get(paste(input$ureg_database,"_enriched_gene_sets",sep="")),"inhibited")
      ggp = make_IPA_upstream_regulators_bar_chart(top_10_upstream_regulators,input$x_axis_label,input$y_axis_label,input$non_significant_colour,input$significant_colour,input$bar_outline_size,input$bar_transparency,input$legend_position,input$significant_name,input$non_significant_name,input$data_label_size, "inhibited")
      
    }
    print(ggp)
  }
  
  else if (input$plot_type == "pde_IPA_upstream_regulators_boxplots") 
  {
    if (input$direction_type == "enriched")
    {
      top_10_upstream_regulators = get_top10_IPA_upstream_regulators_function(get(paste(input$ureg_database,"_all_gene_sets",sep="")),get(paste(input$ureg_database,"_enriched_gene_sets",sep="")),"enriched")
    }
    if (input$direction_type == "activated")
    {
      top_10_upstream_regulators = get_top10_IPA_upstream_regulators_function(get(paste(input$ureg_database,"_all_gene_sets",sep="")),get(paste(input$ureg_database,"_enriched_gene_sets",sep="")),"activated")
    }
    if (input$direction_type == "inhibited")
    {
      top_10_upstream_regulators = get_top10_IPA_upstream_regulators_function(get(paste(input$ureg_database,"_all_gene_sets",sep="")),get(paste(input$ureg_database,"_enriched_gene_sets",sep="")),"inhibited")
    }
    
    upstream_regulator = top_10_upstream_regulators[as.numeric(input$plot_number),]
    plot_title = upstream_regulator[["upstream_regulator"]]
    box_colours = default_sample_group_colours 	
    box_labels = default_sample_group_labels
    
    if (input$direction_type == "enriched")
    {
      ggp = make_hypergeometric_gene_set_boxplot(upstream_regulator,plot_title,input$box_transparency,input$box_line_thickness,box_colours,box_labels,input$x_axis_label,input$y_axis_label,input$legend_position)
    }
    else
    {
      ggp = make_IPA_upstream_regulator_boxplot(upstream_regulator,plot_title,input$box_transparency,input$box_line_thickness,box_colours,box_labels,input$x_axis_label,input$y_axis_label,input$legend_position)
    }
    print(ggp)
  }
  
  else if (input$plot_type == "mpde_distribution_of_expression_values") 
  {
    sample_index = match(input$sample,samples)
    plot_colour = default_samples_colours[sample_index]
    print(plot_colour)
    print(input$sample)
    ggp = make_distribution_of_expression_values_plot(input$sample,plot_colour,input$transparency,input$line_thickness,input$x_axis_label,input$y_axis_label,input$legend_position)
    print(ggp)
  }
  
  else if (input$plot_type == "mpde_pca_contribution_of_components") 
  {
    ggp = make_PCA_contribution_of_components_plot(input$x_axis_label,input$y_axis_label,input$dot_size,input$dot_transparency,input$dot_colour,input$line_type,input$line_colour,input$line_size)
    print(ggp)
  }
  
  else if (input$plot_type == "mpde_pca_scatter_plot") 
  {
    
    plot_sample_group_colours = default_sample_group_colours
    plot_sample_group_labels = default_sample_group_labels
    plot_sample_labels = default_sample_labels
    plot_sample_groupings = sample_groupings
    
    x_axis_label = input$component_x
    y_axis_label = input$component_y
    
    ggp = make_PCA_scatterplot(plot_sample_groupings,input$component_x,input$component_y,x_axis_label,y_axis_label,plot_sample_group_colours,plot_sample_group_labels,plot_sample_labels,input$dot_size,input$dot_transparency,input$legend_position,input$sample_label_size,input$show_proportion_of_variance)
    print(ggp)
  }
  
  else if (input$plot_type == "mpde_correlation_analysis_heatmap") 
  {
    colours = default_three_tone_heatmap_colours
    sample_names = default_sample_labels
    
    ggp = make_correlation_analysis_heatmap(colours,sample_names,input$cluster_x,input$cluster_y,input$distance_method,input$clustering_method,input$reorder_function)
    print(ggp)
  }
  
  else if (input$plot_type == "mpde_most_expressed_genes_violin_plots") 
  {
    violin_colours = default_sample_group_colours 
    violin_labels = default_sample_group_labels
    top_10_genes = get_top_10_genes_by_mean_expression(match(input$sample_group,sample_groups))
    gene = top_10_genes[as.numeric(input$plot_number)]
    
    ggp = make_gene_expression_violin_plot(normexp_matrix_transposed,gene,input$violin_transparency,input$violin_width,input$violin_line_thickness,violin_colours,violin_labels,input$trim_violin,input$jitter_dot_size,input$jitter_dot_colour,input$jitter_dot_width,input$summary_colour,input$summary_size,input$x_axis_label,input$y_axis_label,input$legend_position)
    print(ggp)
  }
  
  else if (input$plot_type == "mpde_number_of_significant_genes_bar_chart") 
  {
    comparison_labels = default_comparison_labels 
    direction_labels = c("up","down")
    bar_colours = default_two_tone_greyscale
    
    ggp = make_number_of_significant_genes_barchart(input$x_axis_label,input$y_axis_label,comparison_labels,direction_labels,bar_colours,input$legend_position,input$data_label_size,input$bar_outline_size)
    print(ggp)
  }
  
  else if (input$plot_type == "mpde_significant_genes_heatmap") 
  {
    colours = default_three_tone_heatmap_colours
    sample_names = default_sample_labels
    
    if (input$sig_any_all == "any") 
    {
      ggp = make_significant_genes_heatmap(normexp_matrix_sig_any_scaled,colours,sample_names,input$cluster_x,input$cluster_y,input$distance_method,input$clustering_method,input$reorder_function)
    }
    else if (input$sig_any_all == "all") 
    {
      ggp = make_significant_genes_heatmap(normexp_matrix_sig_all_scaled,colours,sample_names,input$cluster_x,input$cluster_y,input$distance_method,input$clustering_method,input$reorder_function)
    }
    print(ggp)
  }
  
  else if (input$plot_type == "mpde_fold_vs_fold_scatterplots") 
  {
    colours = c(default_significant_both_colour,default_significant_a_colour,default_significant_b_colour,default_non_significant_colour)
    x_axis_label = paste(input$comparison_1," log2fold",sep="")
    y_axis_label = paste(input$comparison_2," log2fold",sep="")
    ggp = make_fold_vs_fold_scatterplot(input$comparison_1,input$comparison_2,colours,input$dot_size,input$dot_transparency,input$significant_name,input$non_significant_name,input$x_axis_label,input$y_axis_label,input$legend_position,input$data_label_size)
    print(ggp)
  }
  
  else if (input$plot_type == "mpde_differential_expression_signature_metagene_violin_plot") 
  {
    violin_colours = default_sample_group_colours
    violin_labels = default_sample_group_labels
    
    signature_name = paste("signature_",input$signature_number,sep="")
    signature_metagene = data.frame(t(signature_summary[,samples]))
    
    ggp = make_meta_gene_violin_plot(signature_metagene,signature_name,input$violin_transparency,input$violin_width,input$violin_line_thickness,violin_colours,violin_labels,input$trim_violin,input$jitter_dot_size,input$jitter_dot_colour,input$jitter_dot_width,input$summary_colour,input$summary_size,input$x_axis_label,input$y_axis_label,input$legend_position)
    print(ggp)
  }
  
  else if (input$plot_type == "mpde_differential_expression_signatures_heatmap") 
  {
    colours = default_three_tone_heatmap_colours
    sample_names = default_sample_labels
    print(ggp)
  }
  
  else if (input$plot_type == "mpde_differential_expression_signature_hypergeometric_gene_sets_barchart") 
  {
    ##load(paste(project_path,input$biotype,"/mpde_workflows/",input$workflow_name,"/plots/differential_expression_signature/signature_hypergeometric_gene_sets_enrichment/",input$hgsea_database,"/Rdata/signature_",input$signature_number,"_enriched_gene_sets_barchart.Rdata",sep=""))
    print(ggp)
  }
  
})

# set plot height and width
autohw = "auto"

ggplotHeight <- reactive({
  if (is.null(input$plot_height))
    return(autohw)
  else
    heightIn <<- input$plot_height/72
  return(input$plot_height)
})

ggplotWidth <- reactive({
  if (is.null(input$plot_width))
    return(autohw)
  else
    widthIn <<- input$plot_width/72
  return(input$plot_width)
})



# rendering the reactive ggplot object
output$ggplotObject <- renderPlot ({
  if (is.null(input$plot_type))
    return("no plot selected")
  
  if (!is.null(input$plot_type))
    plotInput()
  
}, height = ggplotHeight, width = ggplotWidth)



# plot download handler
output$download_png <- downloadHandler(
  filename = function() {
    paste(input$workflow_type, input$plot_type, '.png', sep = .Platform$file.sep)
  },
  content = function(file) {
    ggsave(file, plot = plotInput(), width = widthIn, height = heightIn, dpi = "screen", device = "png", units = "in")
  }
)

output$download_jpeg <- downloadHandler(
  filename = function() {
    paste(input$workflow_type, input$plot_type, '.jpeg', sep = .Platform$file.sep)
  },
  content = function(file) {
    ggsave(file, plot = plotInput(), width = widthIn, height = heightIn, dpi = "screen", device = "jpeg", units = "in")
  }
)

output$download_svg = downloadHandler(
  filename = function() {
    paste(input$workflow_type, input$plot_type, '.svg', sep = .Platform$file.sep)
  },
  content = function(file) {
    svg(file, height=heightIn, width=widthIn)
    print(plotInput())
    dev.off()
  }
)
}