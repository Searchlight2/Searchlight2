###--- UI ---###
ui <- fluidPage(
  tags$head(tags$link(rel = "stylesheet", type = "text/css", href = "style.css")  ),
  tags$head(tags$link(rel = "shortcut icon", href = "sl2.png")),
  tags$div(id = "titlePanel",
           titlePanel("Searchlight 2"),
           downloadButton(outputId = "download_png", ".png"),
           downloadButton(outputId = "download_jpeg", ".jpeg"),
           downloadButton(outputId = "download_svg", ".svg")),
  
  # select file /biotype / workflow / subplot / theme UI 
  sidebarLayout(
    column(4, 
           id="sidebar",
           wellPanel(
             tags$h3("Load a Workflow"),
             tags$hr(),
             uiOutput("biotypeDropdown"),
             uiOutput("workflowTypeDropdown"),
             uiOutput("workflowNameDropdown"),
             uiOutput("plotDropdown"),
             uiOutput("subplotDropdown"),
             uiOutput("subplotUI")
           ),
           
           wellPanel(
             tags$h3("Modify Plot Specific Parameters"),
             tags$hr(),
             uiOutput("ui")
           ),
           
           wellPanel(
             tags$h3("Modify Plot Theme"),
             tags$hr(),
             
             tags$br(),
             tags$h4(),
             selectInput("th_predefined", "predefined theme", c("under construction", "theme_gray()" = "theme_gray()", "theme_bw()" = "theme_bw()")),
             
             tags$br(),
             tags$h4("Text"),
	     tags$hr(),
             selectInput("th_font_family", "font family", c("Arial", "Helvetica", "Times")),
             selectInput("th_font_face", "font face", c("plain" = "plain", "bold" = "bold", "italic" = "italic", "bold + italic" = "bold.italic")),
             textInput("th_text_colour", "text colour", "black"),
             numericInput("th_title_size", "title size", 20),
             numericInput("th_axis_title_size", "axis title size", 16),
             numericInput("th_axis_text_size", "axis text size", 14),
             
             tags$br(),
             tags$h4("Plot"),
	     tags$hr(),
             textInput("th_plot_fill", "plot fill", "white"),
             textInput("th_plot_colour", "plot colour", "gray"),
             
             tags$br(),
             tags$h4("Grid"),
	     tags$hr(),
             selectInput("th_panel_grid_linetype", "panel grid linetype", c("blank", "solid", "dashed", "dotted", "dotdash", "longdash", "twodash", "1F", "F1", "4C88C488", "12345678")),
             textInput("th_panel_grid_colour", "grid colour", "black"),
             numericInput("th_grid_size", "grid size", 1),
             
             tags$br(),
             tags$h4("Panel"),
	     tags$hr(),
             textInput("th_panel_background_flill", "panel fill", "white"),
             textInput("th_panel_background_colour", "panel colour", "blue"),
             selectInput("th_panel_background_linetype", "panel linetype", c("blank", "solid", "dashed", "dotted", "dotdash", "longdash", "twodash", "1F", "F1", "4C88C488", "12345678")),
             numericInput("th_panel_size", "panel size", 1),
             
             tags$br(),
             tags$h4("Legend"),
	     tags$hr(),
             textInput("th_legend_fill", "fill", "transparent"),
             textInput("th_legend_colour", "border", "black"),
             
             tags$br(),
             tags$h4("Key"),
             textInput("th_legend_key_fill", "key fill", "transparent"),
             textInput("th_legend_key_colour", "key colour", "NA"),
             id = "well")
    ),
    
    # ggplot UI
    column(8,
           wellPanel(
             id = "plotPanel", 
             plotOutput("ggplotObject") 
           )
    )
  )
)
