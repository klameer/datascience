library(shiny)
shinyUI(pageWithSidebar(
  headerPanel("Play around with the central limit theorem"),
  sidebarPanel(
    sliderInput("mu", "Population Mean: ", min=1, max=500, value=100),
    sliderInput("sigma", "Population SD: ", min=1, max=100, value=10),
    sliderInput("n", "Sample Size: ", min=1, max=500, value=50),
    sliderInput("numTrials", "Number of Trials", min=100, max=1000, value=500)
    
    ),
  mainPanel(
    plotOutput("distPlot"),
    helpText("This app lets you play around with a Central Limit Theorem model, 
             use the sliders to see what what multiple trials look like 
             and how they affect the model.")
    )
  ))