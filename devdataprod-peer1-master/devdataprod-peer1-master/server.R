library(shiny)
shinyServer(function(input, output){
  output$distPlot = renderPlot({
    numTrials = input$numTrials
    n = input$n
    mu = input$mu
    sigma = input$sigma
    xbar=rep(0,numTrials)
    for(i in 1:numTrials){xbar[i] = mean(as.integer(rnorm(n, mean=mu, sd=sigma)))}
    hist(xbar, prob=TRUE, breaks=100)  
    
  })
  
})