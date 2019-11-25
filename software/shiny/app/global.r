require(shiny)
require(shinyFiles)
require(fs)
require(shinycssloaders)
require(ggplot2)
require(amap)
require(reshape)
require(graphics)
require(dplyr)
library(GGally)
library(network)
library(sna)

# function to load plot specific env
LoadEnv <- function(RData, env = .GlobalEnv) {
  load(RData, env)
  return(env)
}
